import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):
    print("Attempting to decode new message")
    logging.info(msg.get_body().decode('utf-8'))
    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    try:
        # Connect to PostGresDB
        conn = psycopg2.connect(
        host="udacitynanobm.postgres.database.azure.com",
        database="techconfdb",
        port="5432",
        user="adman@udacitynanobm",
        password="Udacity2020")
        cur=conn.cursor()

        # Get notification subject and message
        myQuery="select subject,message from public.notification where id={};".format(notification_id)
        cur.execute(myQuery)
        res=cur.fetchall()[0]
        notiSubject=res[0]
        notiMsg=res[1]

        # Get attendees first names and email
        myQuery="SELECT first_name,email from public.attendee;"
        cur.execute(myQuery)
        attendees=cur.fetchall()
        totalSent=0

        # Email each attendee
        for attendee in attendees:
            subject = '{}: {}'.format(attendee[0], notiSubject)
            # send_email(attendee[1], subject, notiMsg)
            totalSent+=1
        completeDate="'"+str(datetime.utcnow())+"'"
        totalSentMsg="'Notified {} attendees'".format(totalSent)
        
        # Update database with status and completion date
        myQuery="UPDATE public.notification SET status={},completed_date={} WHERE id={}".format(totalSentMsg,str(completeDate),notification_id)
        cur.execute(myQuery)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        cur.close()
        conn.close()