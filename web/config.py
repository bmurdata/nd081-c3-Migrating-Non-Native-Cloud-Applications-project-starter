import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="udacitynanobm.postgres.database.azure.com"  # PostGres server 
    POSTGRES_USER="adman@udacitynanobm" # PostGres Admin
    POSTGRES_PW="Udacity2020"   # PostGres Admin pw
    POSTGRES_DB="techconfdb"   # Postgres DB in the server
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://notificationquene.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=3jXlsh3sgQm4jvvnph+ng0Pe2ew3yeuOi9AofAWpsT0=' #Notficiation Quene
    SERVICE_BUS_QUEUE_NAME ='notificationquene'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False