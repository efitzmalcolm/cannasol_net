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
                'α-Pinene': row[7],
                'β-Pinene': row[8],
                'Terpinolene': row[9],
                'Geraniol': row[10],
                'α-Terpinene': row[11],
                'γ-Terpinene': row[12],
                'Camphene': row[13],
                'Linalool': row[14],
                'd-Limonene': row[15],
                'Citral': row[16],
                'Myrcene': row[17],
                'α-Terpineol': row[18],
                'Citronellol': row[19],
                'dl-Menthol': row[20],
                '1-Borneol': row[21],
                '2-Piperidone': row[22],
                'β-Caryophyllene': row[23],
                'α-Humulene': row[24],
                'Caryophyllene Oxide': row[25],
            }
            with open("log.txt", "w", encoding="utf-8") as text_file:
                print(results.keys(), file=text_file)
            for r, v in results.items():
                if '<' not in v:
                    value = float(v.replace("%", ""))
                    with open("log1.txt", "w", encoding="utf-8-sig") as text2:
                        print(r, file=text2)
                    with open("log2.txt", "w", encoding="utf-8-sig") as text3:
                        print(Terpene.objects.filter(name=r).query, file=text3)
                    TerpeneResult.objects.create(
                        terpene=Terpene.objects.get(name=r),
                        qa_sample=sample,
                        result=value,
                    )
