import os.path

from django.core.management.base import BaseCommand
import pandas as pd
from Connections.models import *
from datetime import datetime

def format_date(dat):
    if dat is None:
        return dat
    else:
        date_obj = datetime.strptime(dat, "%d-%m-%y")
        return date_obj.strftime("%Y-%m-%d")

class Command(BaseCommand):

    def handle(self, *args, **options):
        df = pd.read_csv('electricity_board_case_study.csv')
        df.replace(pd.NA, None, inplace=True)
        for index,row in df.iterrows():
            try:
                reviewer = Reviewer.objects.get(name=row['Reviewer_Name'])
            except Exception as e:
                reviewer = Reviewer.objects.create(name=row['Reviewer_Name'])
            try:
                address = Address.objects.get(district=row['District'],state=row['State'],pincode=row['Pincode'])
            except Exception as e:
                address = Address.objects.create(district=row['District'],state=row['State'],pincode=row['Pincode'])
            application_dict = {'name':row['Applicant_Name'],'gender':row['Gender'],'address_id':address.id,'ownership':row['Ownership'],
                    "govt_id":row['GovtID_Type'],"govt_id_number":row['ID_Number'],"category":row['Category'],"load":row['Load_Applied (in KV)'],
                    "date":format_date(row['Date_of_Application']),"approval_date":format_date(row['Date_of_Approval']),'status':row['Status'],
                    'reviewer_id':reviewer.id,'comment':row['Reviewer_Comments']}
            application = Application.objects.filter(name=row['Applicant_Name'])
            if application.exists():
                application = application.update(**application_dict)
            else:
                application = Application.objects.create(**application_dict)
