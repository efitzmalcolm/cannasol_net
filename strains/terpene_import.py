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

            results = {
                u'α-Pinene': row[7],
                u'β-Pinene': row[8],
                u'Terpinolene': row[9],
                u'Geraniol': row[10],
                u'α-Terpinene': row[11],
                u'γ-Terpinene': row[12],
                u'Camphene': row[13],
                u'Linalool': row[14],
                u'd-Limonene': row[15],
                u'Citral': row[16],
                u'Myrcene': row[17],
                u'α-Terpineol': row[18],
                u'Citronellol': row[19],
                u'dl-Menthol': row[20],
                u'1-Borneol': row[21],
                u'2-Piperidone': row[22],
                u'β-Caryophyllene': row[23],
                u'α-Humulene': row[24],
                u'Caryophyllene Oxide': row[25],
            }
            with open("log.txt", "w") as text_file:
                print(results.keys(), file=text_file)
            for r, v in results.items():
                if '<' not in v:
                    value = float(v.replace("%", ""))
                    with open("log1.txt", "w") as text2:
                        print(r, file=text2)
                    with open("log2.txt", "w", encoding="utf-8") as text3:
                        print(Terpene.objects.filter(name=r).query, file=text3)
                    TerpeneResult.objects.create(
                        terpene=Terpene.objects.get(name=r),
                        qa_sample=sample,
                        result=value,
                    )
