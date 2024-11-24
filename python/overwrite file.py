# overwrite a file in python :
try:
  file=open("subi.txt","w")
  file.write("this is subi from soorai")
  file.close()
  
  file=open("subi.txt","r")
  for line in file:
    print(line)
  
except FileNotFoundError:
  print("error: FileNotFound")
else:
  file.close()