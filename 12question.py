# 6.
# Take input of age of 3 people by user and determine oldest and youngest among them.
fistman=input("enter the fistman")
secondman=input("enter the secondman")
thirdman=input("enter the thrdman")
if fistman<=secondman and fistman<=thirdman:
    print("oldest",fistman)
elif secondman>=thirdman and secondman>=fistman:
    print("oldest",secondman)
elif thirdman>=fistman and thirdman>=secondman:
    print("oldest",thirdman)
else:
    print("oldest")

