class student():
  name="subitha"
  age=20

# getattr method

print(getattr(student, 'name'))
print(getattr(student, 'age'))
print(getattr(student, 'gender','No such  Attribute Found'))
# here we got attribute error, because we dont have any gender attribute with in the students variable.

# Dot notation 
print(student.name)
print(student.age)

#setattr method
setattr(student,'name','vedha')
print(student.name)

setattr(student,'gender','female')
print(getattr(student,'gender'))

student.city="salem"
print(student.city)

print(student.__dict__)

#delattr is used to delete the attributes

delattr(student,'city')
print(student.__dict__)
del student.gender
print(student.__dict__)

