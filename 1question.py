# Store three integers in x, y and z. Print their sum.
# def sum():
#     x=int(input("enter the number:"))
#     y=int(input("enter the number:"))
#     z=int(input("enter the number:"))
#     num=x+y+z
#     print(num)
# sum()


# num=[12,34,67,89,90,88,44,33,22,11,22]
# n=num[0]
# i=0
# while i<len(num):
#     if num[i]>n:
#         n=num[i]
#     i=i+1
# print(n)
# n.remove(num)
# k=num[0]
# j=0
# while j<len(num):
#     if num[i]>k:
#         k=num[i]
#     j=j+1
# print(j) 



# Check whether 1000 is greater than or equal to 4000. If yes, print "barabar ya bada hai".
#  Else print "nahi hai". Complete the print statements in this question.
# content

# num1=int(input("enter the number1:"))
# num2=int(input("enter the number2"))
# if num1>=num2:
#     print("bada hai")
# else:
#     print("braber hai")

# Create a flowchart that checks whether the sum of 44 and 200 is equal to 123.


# num1=int(input("enter the number1:"))
# num2=int(input("enter the nuber2:"))
# num3=int(input("enter the number3:"))
# num4=num1+num2
# if num3==num4:
#     print("equel")
# else:
#     print("not equel") 



# If this number is less than 10 then print "10 se chota hai". 
# If is greater than 10 and lesser than 20 then print "20 se chota hai".
#  Else if it is greater than 20 then print "20 se bada hai". Complete the 
#  flowchart as per the above instructions.
# content       




# num=int(input("enter the number:"))
# if num<10:
#     print("10 se chota hai")
# if num<20:
#     print("chota hai")
# else:
#     print(" 20 bada hai")


# Create a flowchart to take a number as input from the user. Convert 
# this input to integer. Check if it is equal to varx.

# If the number is equal to varx, print "Equal" else print "Not equal".

# varx=int(input("enter the number:"))
# vary=int(input("enter the number:"))
# if varx*vary:
#     print("diveble")
# else:
#     print("not divible")


# Create a flowchart to take two numbers as input from the user. 
# Print the number which is greater.
# content

# For example, if user enters 100 and 30, then print 100 as it is greater.

# Submit the flowchart and code for this question.


# num1=int(input("enter the number1:"))
# num2=int(input("enter the number2:"))
# if num1<=num2:
#     print("greater number1")
# else:
#     print("greater number
    
# Create a flowchart that takes a number as user input. Check if this 
# number is divisible by 5 and 15 both.
# content

# Hint: You will need to use nested if-else for this question.

# Submit flowchart as well as code.


num=int(input("enter the number:"))
if num%5==0 or num%15==0:
    print("number is divible by 5 and 15 both")
else:
    print("number is not divible by 5 and 15 both")    


# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS) 





# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person) 





 
# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.keys():
#     print(x) 


# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
#     }
# print(len(meal)) 



# Ek program likhiye jisse ki agar di hui key pehle se dictionary
# me exist karti ho toh “exists “ print kare aur agar nahi karti 
# ho toh “not exists” print kare. Example :-



# num={"khusboo":12,"dipak":13,"rani":34,"pooja":44}
# for i in num:
#     if "khusboo" in num:
#       print("exist")
#     else:  
#         print("not exise")
            



# num={"kiran":12,"yaari":14,"priya":44,"latt":99}
# sum=0
# for i in num:
#     sum=sum+num[i]
# print(sum)


# Dic= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#   	3:{    
#         "A" : 'WELCOME',
#         "b" : 'To',
#         "c": 'DHARAMSALA'
#         }
#     }
# Dic.pop("c")
# print(Dic)


# Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys 
# ho aur dusri list ke elements unn keys ki values ho. Example :- Input :-
 
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# n={}  
# i=0
# while i<len(list1):
#     n[list1[i]]=list2[i]
#     i=i+1
# print(n)    




# Ek program likhiye jo dictionary me se duplicate keys hata de. Example :- Input :-
 
# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"green",
#     "bat":3
#     }
# n={}     
# for i in dic:
#     n.update(dic)
# print(n) 


a=12
name="khusboo"
print(name+","+ + "main stat huaa hai")




# Ek list lijiye aur uske andar dictionaries me keys and values likhiye 
# jaisa ki niche dikhaya gaya hai (Sample Data) aur uske baad saare unique
# values ko ek list me print karaye. Example :- Input :-
 
# list1=[
#     {"first":"1"}, 
#     {"second": "2"}, 
#     {"third": "1"}, 
#     {"four": "5"}, 
#     {"five":"5"}, 
#     {"six":"9"},
#     {"seven":"7"}
# ] 
# n=[]
# for i in list1:
#     for j in i:
#         n.append(i[j])
# print(n)  



# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye. Output

# name={"khusboo":12,"gunjan":23,"kusum":33,"pooja":55}
# n={}
# i=1
# while i<len(name):
#     i=i+1
# print(name) 



# MISSISSIPPI" iss word me har letter ki occurrency count karke ek 
# dictionary me store karaye. Jisme letter dictionary ki keys aur 
# occurrency Uss dictionary ki values hongi. Example:- Output :
# 


# dict1="MISSISSIPPI"
# n={}
# i=1
# count=0
# while i<len(dict1):




# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai. Input 
# :- Output :-
# num={"khusboo":12,"neha":34,"usha":22}
# for i in range(len(num)):
#     print(i)




# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# for i in my_dict:
#     print(max(my_dict))



# stats = {'a':1000, 'b':3000, 'c': 100}
# max_key = None
# if bool(stats):
#    max_key = max(stats, value=stats.get)
# print(max_key)


# Given two numbers, write a Python code to find the Maximum of these two numbers.


# def max():
#     num=int(input("enter the number:"))
#     num1=int(input("enter the number:"))
#     if num>=num1:
#         print(num, "it is greater number")
#     elif num1>=num:
#         print(num1,"it is greater number:")
#     else:
#         print("invited")
# max()            



# Given two numbers, write a Python code to find the Minimum of these two numbers.
# def min():
#     num=int(input("enter the number:"))
#     num1=int(input("enter the nuber:"))
#     if num<=num1:
#         print(num,"it is min number:")
#     elif num1<=num:
#         print(num1,"it is min number:")
#     else:
#         print("invited") 
# min()


# Python program to check whether the string is Symmetrical or Palindrome
# def student():
#     n=[]
#     i=0
#     while i<=10:
#         num=int(input("enter the number:"))
#         n.
#         i=i+1
# student()  




# def student():
#     n=[]
#     i=0
#     while i<=5:
#         n


# def student():
#     n=[]
#     i=0
#     while i<=5:
#         name=input("enter the name of student")
#         n.append(name)
#         i=i+1
#     print(n)
# student()        



# add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le 
# aur fir unka sum print karta hai. Arguments ka naam number1 aur number2 hona chaiye. Input :-
 

# def add_numbers():
#     num=int(input("enter the number:"))
#     num1=int(input("enter the number:"))
#     b=num+num1
#     print(b)
# add_numbers()   



# Yeh question 2 parts mein hai. Dono parts ka code same file mein likh ke submit karein.
# Question (Part 1)

# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare 
# "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi toh print kare
#  "Dono numbers even nahi hai"

    
# def check_numbers():
#     num=int(input("enter the number:"))
#     if num%2==0:
#         print("it is even number")
#     else:
#         print("it is not even number")
# check_numbers() 




        

# list_change naam ka ek function ka code likho jo 2 lists jisme integers arguments ki 
# tarah le aur fir unn lists ki woh items jo same index number (kram) pe hain unko multiply 
# kar ke ek nayi list return karvaye. Aapko multiply karne ke liye calculator function ka use 
# karna hai. Normal tareeke se multiply nahi kar sakte ho. Jaise agar hum function ko aise call karenge
#  toh:
 
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5]) 

# Yahan multiple_list ki yeh value honi chaiye:
 
# [10, 200, 150, 100] 

# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka 
# parameter lega aur 0 se limit tak ke beech ke sabhi even aur odd numbers ko
#  label ke saath print karega jaisa ki niche dikhaya gaya hai. For example :- Input:- Output :-
# Edit on Github




# my_list = [[10,20,30],[40,50,60],[70,80,90]]

# flattened = [x for temp in my_list for x in temp]
# # output => [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(flattened)



# my_list=[[1,2,3],[7,8,9,9],[56,8,9,6,]]
# num=[x in for b in my_list for x in b ]



# num=int(input("enter the number:"))
# for i in num:
#     if num%2==0:
#         print("even nuber")
#     else:
#         pass    








# Ek program banao jo 1 se 100 tak ke beech mein woh numbers print kare jo 7 se divide ho jaate hain. 
# Aapki output mein yeh aana chaiye.

# i=0
# while i<=100:
#     if i%7==0:
#         print(i)
#     i=i+1



# Ek program likho jo loop ka use kar ke 1 se leke 100 tak saare numbers ka sum print kare.
#  Aapke program ko pehle 1 se 100 ke beech mein saare numbers ka sum calculate karna hai. 
#  1+2+3+4 +5+6+7....+95+96+97+98+99+100 
# Fir uss sum ko print karana hai.


# i=0
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
# print(sum) 




# Ek loop banao jo user se 10 numbers ko input le. Input lene ke baad unn saare
#  numbers ka sum print kare. Yeh program kuch aise chalega. Har baar input() 
#  ka use kar ke user se ek number input lega. Final line mein isne Total Sum:
#   417 print kara hai. Yeh isiliye print kia hai kyunki 10+16+9+10+56+78+98+43+21+76 ka sum 417 hai.


# i=10
# sum=0
# while i<=417:
#     sum=sum+i
# print(sum)    
    