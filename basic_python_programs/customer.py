import io
import os

filein = open('customer.txt', 'r')

for line in filein: 
  line = line.rstrip(os.linesep)
  data = line.split(',')
  print(data, data[0], data[3])

filein.close()
