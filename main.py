import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist = ["Luffy","zoro","sanji","Namii","usopp","brook","zimbei","Franky","Chopper","Robin"]
print(random.choice(mylist))
random.shuffle(mylist)