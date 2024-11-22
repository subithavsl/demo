# Read a text file in python:
try:
    file=open("subi.txt","r")
    print(file.read())
except FileNotFoundError:
  print("errr: FileNotFound")
else:
  file.close()