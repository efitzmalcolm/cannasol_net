import csv
import sys
from datetime import datetime
from django.db import transaction
from strains.models import *


lab_name = 'Testing Technologies'
lab_id = '3430-15'

with transaction.atomic():
    with open("C:/Users/admin/Desktop/terpenes.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                strain = Strain.objects.get(name=row[5])
            except Strain.DoesNotExist:
                strain = Strain.objects.create(
                    name=row[5],
                    brand=Brand.objects.get(name='CannaSol Farms'),
                )
            try:
                sample = qaSample.objects.get(sample_id=row[3].replace(" ", ""))
            except qaSample.DoesNotExist:
                sample = qaSample.objects.create(
                    lab_name=lab_name,
                    date_received=datetime.strptime(
                        row[1], '%m/%d/%Y').strftime('%Y-%m-%d'),
                    date_reported='2015-12-22',
                    sample_type=row[6],
                    strain=strain,
                    lab_id=lab_id,
                    sample_id=row[3].replace(" ", ""),
                    lot_id=row[2].replace(" ", "",),
                )

            for k, v in Terpene.row_map.items():
                if '<' not in row[v]:
                    value = float(row[v].replace("%", ""))
                    TerpeneResult.objects.create(
                        terpene=Terpene.objects.get(name=k),
                        qa_sample=sample,
                        result=value,
                    )
