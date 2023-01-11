from celery import shared_task
from project import settings
import csv
import pandas as pd
from .models import Product
from django.http import HttpResponse

@shared_task(bind=True)
def data_from_csv_to_model(self,file):
    l=[]
    df = pd.read_csv(file,delimiter='|')
    for index, row in df.iterrows():
        foo = Product(title = row['title'],category = row['category'], price = row['price'],desc = row['desc'])
        l.append(foo)
    Product.objects.bulk_create(l)
    return "Processing"

            
            


