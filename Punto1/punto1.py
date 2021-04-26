import json
import pandas as pd 
import numpy as np 
import datetime as dt
import csv
from pandas_datareader import DataReader
from datetime import timedelta
from datetime import date
import boto3 
import time 


### Creamos las variables para poder restar un día
hoy= dt.datetime.today()
res= hoy  - timedelta(days=2)

#Renombramos con sus codigos
Avianca = 'AVHOQ'
CementosArgos = 'CMTOY'
Ecopetrol = 'EC'
GrupoAval = 'AVAL'

#Traer los datos del yahoo
AccionesAvianca = DataReader(Avianca,'yahoo',start=res)
AccionesCementosArgos = DataReader(CementosArgos,'yahoo',start=res)
AccionesEcopetrol = DataReader(Ecopetrol,'yahoo',start=res)
AccionesGrupoAval = DataReader(GrupoAval,'yahoo',start=res)

#Convertimos las acciones a un csv
AccionesAvianca.to_csv('AccionesAvianca.csv')
AccionesCementosArgos.to_csv('AccionesCementosArgos.csv')
AccionesEcopetrol.to_csv('AccionesEcopetrol.csv')
AccionesGrupoAval.to_csv('AccionesGrupoAval.csv')

# Subimos los archivos hacia el S3
#Asignamos la variable bucket al nombre de nuestro bucket
bucket='punto1-parcial2'

#Asignamos las variables para almacenarlas y separar dias, meses y años
year = date.today()
agno=year.year
print(agno)

month=date.today()
mes=month.month
print(mes)

day=date.today()
dia=day.day
print(dia)

###UPLOAD FILE AVIANCA
#Será la dirección donce irá nuestro archivo
NombreArchivo = 'stocks/empresa=avianca/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/AccionesAvianca.csv'
#Nombre de cómo quedará en el bucket
NombreObjeto = 'AccionesAvianca.csv'
#Llamamos al cliente de boto3
s3_client = boto3.client('s3')
response = s3_client.upload_file(NombreObjeto, bucket, NombreArchivo)
print("El archivo subió correctamente")

###UPLOAD FILE Cementos Argos
#Será la dirección donce irá nuestro archivo
NombreArchivo1 = 'stocks/empresa=CementosArgos/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/AccionesCementosArgos.csv'
#Nombre de cómo quedará en el bucket
NombreObjeto1 = 'AccionesCementosArgos.csv'
#Llamamos al cliente de boto3
s3_client = boto3.client('s3')
response = s3_client.upload_file(NombreObjeto1, bucket, NombreArchivo1)
print("El archivo subió correctamente")

#Realizamos el upload_File ECOPETROL

#Será la dirección donce irá nuestro archivo
NombreArchivo2 = 'stocks/empresa=Ecopetrol/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/AccionesEcopetrol.csv'
#Nombre de cómo quedará en el bucket
NombreObjeto2 = 'AccionesEcopetrol.csv'
response = s3_client.upload_file(NombreObjeto2, bucket, NombreArchivo2)
print("El archivo subió correctamente")

#Realizamos el upload_File GRUPO AVAL

#Será la dirección donce irá nuestro archivo
NombreArchivo3 = 'stocks/empresa=GrupoAval/agno='+str(agno)+'/mes='+str(mes)+'/dia='+str(dia)+'/AccionesGrupoAval.csv'
#Nombre de cómo quedará en el bucket
NombreObjeto3 = 'AccionesGrupoAval.csv'
response = s3_client.upload_file(NombreObjeto3, bucket, NombreArchivo3)
print("El archivo subió correctamente")