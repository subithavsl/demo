# Delete file in python:
import os

if os.path.exists("test1.txt"):
  os.remove("test1.txt")
else:
  print("File Not Found")

