"""
# try block in python
try:
  a=10/0
except Exception as e:
  print(e)


try: 
  a=10/0
except Exception as e:
  print(e)
else:
  print(a)

  
try: 
  a=10/2
except Exception as e:
  print(e)
else:
  print(a)
finally:
  print("thank you")
  
  # types of exceptions:
  
  print(dir(locals()['__builtins__']))
  print(len(dir(locals()['__builtins__'])))
    
  
try:
  print(a)
except NameError as e:
  print("A is not Defined")

try:
  print(10/0)
except ZeroDivisionError as e:
  print("Denominator cant be zero")


try:
  a=int("subi")
except ValueError as e:
  print("please Enter numbers")


try:
  a=[10,20,30,40]
  print(a[10])
except IndexError as e:
  print("invalid index")

try:
  f=open("test.txt")
except FileNotFoundError:
  print("File is not Found")
else:
  print(f.read())
"""

try:
  a=10/2
  print(a)
  b=[10,20,30,40]
  print(b[10])
except ZeroDivisionError:
  print("Denominator cant be zero")
except IndexError:
  print("invalid index")
