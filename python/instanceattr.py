class user:
  course='java'

o=user()

print(user.__dict__)
print(user.course)
print(o.__dict__)

print(o.course)
o.course="c++"
print(o.__dict__)
print(o.course)

o2=user()
print(o2.course)
