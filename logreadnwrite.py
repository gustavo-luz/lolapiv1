import csv
import pandas
import time
from time import sleep

df = pandas.read_csv('D://windows//Documents//BET//new_api//lolapiv1//log.csv')
#print(df)
#valor = df['time'][0]
#print(valor)

print(df['time'][0])
cs = 2

if cs < 4:
    df['time'][0] = 0
elif cs == 4:
    df['time'][0] = 105
elif cs > 4:
    df['time'][0] = df['time'][0] + 10

#se for menor que 4, escreve 0 no tempo
print(df['time'][0])

df.to_csv('D://windows//Documents//BET//new_api//lolapiv1//log.csv')
















"""
# se fosse fazer com txt
#escrevendo, fazer isso se o cs do jg for igual a 4
new_file=open("D://windows//Documents//BET//new_api//lolapiv1//log.txt",mode="w",encoding="utf-8")
new_file.write("105")
new_file.close()

my_file=open("D://windows//Documents//BET//new_api//lolapiv1//log.txt","r")
print(my_file.read())
strlida = my_file.read()
print(strlida)
print(type(strlida))
print(len(strlida))
#print(int(strlida))


# https://www.datacamp.com/community/tutorials/reading-writing-files-python
#The read() method just outputs the entire file if the number of bytes (n) is not given in the argument.
# If you execute my_file.read(3), you will get back the first three characters of the file
"""