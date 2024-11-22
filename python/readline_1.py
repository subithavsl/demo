# readline and readlines in python:
try:
    file=open("subi.txt","r")
    print(file.readline())
    print(file.readline(6))
    print(file.readlines())
    
except FileNotFoundError:
  print("errr: FileNotFound")
else:
  file.close()