from django.shortcuts import render, redirect
from datetime import datetime
import os
import boto3
import psycopg2
import sys
import gspread
sa = gspread.service_account(filename='bakedbuddyApp/data/google_sa.json')

def index(request):
    context = {}

    if 'RDS_DB_NAME' in os.environ:
            ENDPOINT = 'aa1x8zrds8ywkka.chakzrlo7bqa.us-west-2.rds.amazonaws.com'
            AWS_PROFILE = os.environ.get('AWS_PROFILE')
            session = boto3.Session(profile_name=AWS_PROFILE)
            client = session.client('rds', region_name='us-west-2')
            
            engine = 'django.db.backends.postgresql_psycopg2'
            REGION = 'us-west-2'
            DBNAME = os.environ['RDS_DB_NAME']
            USER = os.environ['RDS_USERNAME']
            PASSWORD = os.environ['RDS_PASSWORD']
            HOST = os.environ['RDS_HOSTNAME']
            PORT = os.environ['RDS_PORT']

            token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

            try:
                conn = psycopg2.connect(host=HOST, port=PORT, database=DBNAME, user=USER, password=PASSWORD, sslrootcert="SSLCERTIFICATE")
                cur = conn.cursor()
                cur.execute("""SELECT now()""")
                query_results = cur.fetchall()
                print("------------------------ find me ------------------------------------------- find me")
                print(query_results)
                context['aws_profile'] = "code is working"

            except Exception as e:
                print("Database connection failed due to {}".format(e))
                context['aws_profile'] = "Database connection failed due to {}".format(e) 


    # aws_profile = os.environ.get('AWS_PROFILE')
    # print(aws_profile)
    # session = boto3.Session(profile_name=aws_profile)
    # context['aws_profile'] = aws_profile

    return render(request, "bakedbuddyApp/slash.html", context)

def daily_deals(request):
    context = {}

    index_sheets = sa.open("Index")
    tacoma_dispensaries = index_sheets.worksheet('Tacoma')
    dispensaries_list = tacoma_dispensaries.get_all_records()
    
    context['tacoma_daily_deals_list'] = dispensaries_list

    return render(request, "bakedbuddyApp/daily-deals.html", context)

def product_type(request, product_type):
    context = {}
    # context["product_type"] = product_type
    context["deals_list"] = []
    # TODO Move this to a more scalable form.
    # deals_list = product_type_json(product_type)
    # Get Tacoma dispensaries with daily deals
    # with open('bakedbuddyApp/data/DEALS_DATA.json') as json_file:
    #     data = json.loads(json_file.read())
    #     context["deals_list"] = data[product_type]

    return render(request, "bakedbuddyApp/product-type.html", context)

def dispensary(request, dispensary_id):
    context = {}

    # Get day of the week
    current_date = datetime.today().weekday()# Get day of the week
    context['current_date'] = current_date

    # Creates the dispensary
    # 
    # Gets data from Google Sheets API (2 seperate sheets)
    deals_sheet = sa.open(dispensary_id)

    partnership_sheet = deals_sheet.worksheet('Sheet')
    partnership_data = partnership_sheet.get_all_records()
    dispensary_dict = partnership_data[0]

    sheet_name = dispensary_id + '?details'
    details_sheet = sa.open(sheet_name)
    google_details_sheet = details_sheet.worksheet('google_place_details')
    details_data = google_details_sheet.get_all_records()
    dispensary_dict.update(details_data[0])

    context["dispensary"] = dispensary_dict
    return render(request, "bakedbuddyApp/dispensary.html", context)


