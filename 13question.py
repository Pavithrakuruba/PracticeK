#  Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.0

# num=int(input("enter the leap year"))
# if num%4==0:
#     print()



# name=input("enter the name")
# n=""
# i=1
# while i<=len(name):
#     n+=name[-i]
#     # n.append(name[-i])
#     i=i+1
# print(n)


# num=[1,2,3,4,5,6,7,8]
# num1=[5,6,7,8,9,12,13]
# i=1
# n={}
# while i<len(num):
#     n.append(num+num1)
#     i=i+1
# print(n)    
    


# Code likho jisse 30 se 420 tak ke unn numbers ka sum calculate ho jo 8 
# ke multiple hai yaani wo numbers 8 ke table (paahade) mein aate hai.    


# i=30
# sum=0
# while i<=420:
#     if i*8:
#         sum=sum+i
#     i=i+1
# print(sum)        


# 11 logon ka weight input le aur fir average weight print kare.
#  Aur fir yeh bhi check kare ki kya Average weight 5 ka multiple (Yaani 5 se
# bhaag karne par shesh 0 bachta hai) hai ya nahi? Note: Isme aapko input
#  ka use karna padega. Aap loop ke andar raw input ka use kar ke 11 baar raw_input le sakte ho.
# Edit on Github


# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa
#  jaaye jaise ki niche Expected result me diya gaya hain or jisski bhi keys same 
#  hai unki values add ho jai. Example :- Input :- Output :- 


# Ek program likhiye jisse ki agar di hui key pehle se dictionary
#  me exist karti ho toh “exists “ print kare aur agar nahi karti ho
#   toh “not exists” print kare. Example :-


# dict={"name":"Raju", "marks":56}
# name=int(input("enter the name:"))
# if dict in name:
#     print("exist")
# else:
#     print("not exist")

# Ek program likhiye jo ki dictionaries ki values ka sum print
# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        }
# sum=0        
# for i in my_dict:
#     sum=sum+i
# print(sum)



# Ek program likhiye jo ki nested dictionary me se first key or
#  value ko remove kare. Example :- Input :- Output :- 

        

# name1={"name":"khusboo","age":"12","calss":"12"}
# name1.pop("name")
# print(name1)







# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS) 
# 
# 

# Do lists lekar ek dictionary banaiye jisme 
# pehli list ke elements keys ho aur dusri list
#  ke elements unn keys ki values ho. Example :- Input :-



# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# n=[]  
# i=0
# while i<len(list1):
#     n[list1[i]]==list2[i]
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

# Ek list lijiye aur uske andar dictionaries me keys and 
# values likhiye jaisa ki niche dikhaya gaya hai (Sample Data) 
# aur uske baad saare unique values ko ek list me print karaye
# . Example :- Input :-


# num=[
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ] 


# user se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye. Output :- 
# Edit on Github

         
# list1={"khusboo":12,"lilita":23,"kusum":45,"usha":47}





# my_list = [2, 3, 5, 7, 11]

# squared_list = [x**2 for x in my_list]
# print(squared_list)

    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]

# squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# # output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}



# pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]

# for p in pat:
#     pass
#     if (p == 0):
#         current = p
#         break
#     elif (p % 2 == 0):
#         continue
#     print(p)    # output => 1 3 1 3 1

# print(current)    # output => 0


# a="Hello World"[::-1]
# print(a)


a=20**10
print(a)
         