# Append mode fine in python:
try:
  file=open("python.txt","a")
  file.write("vedha is my soul")
  file.close()
  
  
  file=open("python.txt","r")
  print(file.read())
  

except FileNotFoundError:
  print("error: FileNotFound")
else:
  file.close()
  