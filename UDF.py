# Default parameter function in python :


def user(name,city="salem"):
    print(name,"is from",city)

user("ram","namakkal")
user("sam")


# passing a List as an Argument in Function python


def total(marks):
    return sum(marks)
print("Total:",total([55,73,95,82,11,26]))


#recursive function python

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

print("factorial:",factorial(5))

#Lambda Function python


c=lambda a:a+50
print(c(5))

c=lambda a,b:a*b
print(c(2,3))



