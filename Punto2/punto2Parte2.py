print('0')
import json
import os
import boto3
import datetime as dt
from datetime import date
from datetime import timedelta
#Iniciamos el ciente de boto3
print('1')
s3 = boto3.client('s3')
print('2')
#asignamos variables de dia,mes,año
hoy= dt.datetime.today()

agno=hoy.year
mes=hoy.month

dia=hoy.day

# TODO implement
key = 'headlines/raw/periodico=eltiempo/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/eltiempo.html'
print(key)
print('3')
nameBucket = 'punto2-parcial2'
print('4')
#Indsicamos la direccion de descarga
DirDescarga = '/tmp/{}'.format(key.split('/')[-1])
print('5')
#Descargamos el archivo
s3.download_file(nameBucket,key,DirDescarga)
print('6')
#Leemos el archivo
LeerArchivo = open(DirDescarga,'r')
print('7')
lineas = LeerArchivo.readlines()
print('8')
 #Variables que almacenarán los datos requeridos
CatPeriodico = ''
CabeceraPeriodico = ''
LinkPeriodico = ''
#Indicamos la categoria el titulo o link
for i in lineas:
    if 'category' in i:
        CatPeriodico = i.replace(',',' ').split('category')[1]
        break
for i in lineas:
    if '<title>' in i:
        CabeceraPeriodico = i.replace(',',' ')
        break
for i in lineas:
    if 'canonical' in i:
        aux = i.split(' ')
        for j in aux:
            if 'href="https://www/' in j:
                LinkPeriodico = j.split('"')[1]
        break
#Creamos un archivo con los datos que necesitamos
archivo = open('/tmp/prueba.txt','w')
archivo.write('category,headline,link\n{},{},{}'.format(CatPeriodico,CabeceraPeriodico,LinkPeriodico))
archivo.close()

#Subimos el archivo
upload_path='headlines/final/periodico='+key.split('/')[-1].split('.')[0]+'/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/eltiempo.csv'
s3.upload_file('/tmp/prueba.txt',nameBucket,upload_path)
print('Ya subió el archivo')

key1 = 'headlines/raw/periodico=publimetro/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/publimetro.html'
print('9')
nameBucket = 'punto2-parcial2'
print('10')
#Indsicamos la direccion de descarga
DirDescarga = '/tmp/{}'.format(key1.split('/')[-1])
print('11')
#Descargamos el archivo
s3.download_file(nameBucket,key1,DirDescarga)
print('12')
#Leemos el archivo
LeerArchivo = open(DirDescarga,'r')
print('13')
lineas = LeerArchivo.readlines()
print('14')
 #Variables que almacenarán los datos requeridos
CatPeriodico = ''
CabeceraPeriodico = ''
LinkPeriodico = ''
#Indicamos la categoria el titulo o link
for i in lineas:
    if 'category' in i:
        CatPeriodico = i.replace(',',' ').split('category')[1]
        break
for i in lineas:
    if '<title>' in i:
        CabeceraPeriodico = i.replace(',',' ')
        break
for i in lineas:
    if 'canonical' in i:
        aux = i.split(' ')
        for j in aux:
            if 'href="https://www/' in j:
                LinkPeriodico = j.split('"')[1]
        break
#Creamos un archivo con los datos que necesitamos
archivo = open('/tmp/prueba.txt','w')
archivo.write('category,headline,link\n{},{},{}'.format(CatPeriodico,CabeceraPeriodico,LinkPeriodico))

archivo.close()

#Subimos el archivo
upload_path='headlines/final/periodico=publimetro/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/publimetro.csv'
s3.upload_file('/tmp/prueba.txt',nameBucket,upload_path)
print('Ya subió el archivo 2')
archivo.close()

