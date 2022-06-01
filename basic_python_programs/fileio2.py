import os
import shutil

# Create a directory 'test' and copy all files from current folder to 'test'
os.mkdir("test")
lst = os.listdir(".")
for f in lst:
	if(os.path.isfile(f)):
		shutil.copy(f, 'test')


# Change to test directory and list its contents
os.chdir("test")
print(os.getcwd())

os.chdir("..")
lst = os.listdir("test")
print (lst)


# Remove all .py files from test directory
os.chdir("test")
count = 0

def removefile(extension):
  for item in lst:
    if item.endswith(extension): 
      global count
      count += 1
      print(item)
      os.remove(item)

removefile(".py")

print("count of python files:", count)

# Go to parent directory and remove the test folder
os.chdir("..")
os.rmdir("test")
