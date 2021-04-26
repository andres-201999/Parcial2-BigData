import json
import boto3
from urllib.parse import unquote_plus
from datetime import timedelta
from datetime import date
import datetime as dt
import os
s3 = boto3.client('s3')

hoy= dt.datetime.today()

agno=hoy.year
mes=hoy.month
dia=hoy.day

print('1')
key = 'headlines/raw/periodico=eltiempo/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/eltiempo.html'
nameBucket = 'punto2-parcial2'
DirDescarga = '/tmp/{}'.format(key.split('/')[-1])
print('2')

s3.download_file(nameBucket,key,DirDescarga)
print('3')
ArchivoSubido = 'news/raw/periodico=eltiempo/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/eltiempo.html'
print('4')
s3.upload_file(DirDescarga,nameBucket,ArchivoSubido)
print('subio archivo 1')

key1 = 'headlines/raw/periodico=publimetro/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/publimetro.html'
nameBucket = 'punto2-parcial2'
DirDescarga = '/tmp/{}'.format(key.split('/')[-1])

newkey1 = 'headlines/raw/periodico=publimetro/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/publimetro.html'
print('a')
print(newkey1)

s3.download_file(nameBucket,newkey1,DirDescarga)
print('b')
ArchivoSubido1 = 'news/raw/periodico=publimetro/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/publimetro.html'
s3.upload_file(DirDescarga,nameBucket,ArchivoSubido1)
print('Subio archivo 2')
