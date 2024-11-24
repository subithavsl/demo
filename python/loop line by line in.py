#loop line by line in python file concept:

try:
  file=open("subi.txt","r")
  for line in file:
    print(line)
  
except FileNotFoundError:
  print("error: FileNotFound")
else:
  file.close()