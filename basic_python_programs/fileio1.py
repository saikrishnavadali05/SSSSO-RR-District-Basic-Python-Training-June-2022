import io
print (io.DEFAULT_BUFFER_SIZE)

filein = open('first.py')
fileout = open('firstold.py', 'w')

print(type(filein))

def read():
  print(filein.read())
  filein.seek(0,0)

def readlines():
  print(filein.readlines())
  position = filein.seek(0, 0);

def readline():
  for line in filein:  
    fileout.write(line)
  position = filein.seek(0, 0);

read()
readlines()
readline()

position = filein.tell();
print("File position 1:", position)

def readchars(n):
  str = filein.read(n);
  position = filein.tell();
  print("File position 2:", str, " ", position)

readchars(20)

print(filein.mode)
print(filein.closed)
print(filein.name)
                 
filein.close()
fileout.close()

print(filein.closed)