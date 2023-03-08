import csv
import pandas
import time
from time import sleep
import datetime

df = pandas.read_csv('D://windows//Documents//BET//new_api//lolapiv1//log.csv')
#print(df)
#valor = df['time'][0]
#print(valor)

print(df['time'][0])
cs = 5

if cs < 4:
    df['time'][0] = 0

elif cs == 4:
    df['time'][0] = 105
elif cs > 4:
    df['time'][0] = df['time'][0] + 10

#se for menor que 4, escreve 0 no tempo
print(df['time'][0])
#print(df['time'][0] // 60)
#print(df['time'][0] % 60)
print(df['time'][0] // 60, ":",df['time'][0] % 60)


df.to_csv('D://windows//Documents//BET//new_api//lolapiv1//log.csv')


