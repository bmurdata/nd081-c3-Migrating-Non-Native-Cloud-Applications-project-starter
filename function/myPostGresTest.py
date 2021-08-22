import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


try:
    notification_id=5
    conn = psycopg2.connect(
    host="udacitynanobm.postgres.database.azure.com",
    database="techconfdb",
    port="5432",
    user="adman@udacitynanobm",
    password="Udacity2020")
    cur=conn.cursor()
    myQuery="select subject,message from public.notification where id={};".format(notification_id)

    cur.execute(myQuery)
    res=cur.fetchall()[0]
    notiSubject=res[0]
    notiMsg=res[1]

    myQuery="SELECT first_name,email from public.attendee;"
    cur.execute(myQuery)
    attendees=cur.fetchall()
    totalSent=0
    for attendee in attendees:
        subject = '{}: {}'.format(attendee[0], notiSubject)
        # send_email(attendee[1], subject, notiMsg)
        totalSent+=1
    completeDate="'"+str(datetime.utcnow())+"'"
    totalSentMsg="'Notified {} attendees'".format(totalSent)
    myQuery="UPDATE public.notification SET status={},completed_date={} WHERE id={}".format(totalSentMsg,str(completeDate),notification_id)
    cur.execute(myQuery)
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

    # TODO: Get notification message and subject from database using the notification_id

    # TODO: Get attendees email and name

    # TODO: Loop through each attendee and send an email with a personalized subject

    # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified

finally:
    cur.close()
    conn.close()