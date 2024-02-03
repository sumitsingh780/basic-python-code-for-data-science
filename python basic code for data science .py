#!/usr/bin/env python
# coding: utf-8

# # DAY 01 OF 75 DAYS CHALLENGE
# 

# In[1]:


print ("hello world ")



# In[2]:


print (2+5)


# # python comments

# In[ ]:


#this is comments 
#print("hello world")


# In[3]:


""" multilinecomment """


# # variables & operators

# In[4]:


a =5               # a,b ,c, is a variables
b = 10 
c = 16
print (a+b+c)


# In[5]:


a , b ,c = "alpha","beta","gamma"
print(a,b,c)


# # python output variables

# In[6]:


a = 3
b =3
print (a+b)


# # data type

# In[8]:


x = 2
y =4.5
z="welcome to indore"
print (x,type(x))
print (y,type(y))
print (z,type(z))


# In[9]:


b =[2,4,56,7,88,7,4,4,66,7]
print(type(b))


# In[10]:


b =(2,4,56,7,88,7,4,4,66,7)
print(type(b))


# In[13]:


s ={2,4,56,7,88,7,4,4,66,7}
print(type(s))


# In[14]:


get_ipython().run_line_magic('whos', '')


# # operators in python 

# In[21]:


a = 3
b= 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


# In[20]:


a ="hello"
b = "world"
print(a+" "+b)


# In[30]:


a = True 
b = False
print(a and b)
print(not(a))
print(a or b)



# # built in functions 

# abs() function

# In[31]:


x = abs(-7.25)
print(x)


# binary function 

# In[32]:


a = 20
print (bin(a))


# bytes functions

# In[33]:


a =5
print(bytes(a))


# chr funtion

# In[39]:


x = chr(97)
print(x)


# complex function

# In[40]:


x = complex(3,5)
print(x)


# In[41]:


y= complex(2.3,4.6)
print(y)


# float function 

# In[45]:


x =float(3)
print(x)


# int function 

# In[46]:


x = int(3.54)
print(x)


# str function 

# In[48]:


x = str("345")
print(x,type(x))


# help function

# In[49]:


help(float)


# input function 

# In[50]:


name = input("enter your name :-")
print("my name is ", name)


# In[51]:


print (2+2)


# # control flow statements 

# conditional statements 

# In[54]:


marks = eval ( input("enter your marks:-"))
if marks>60:
    print ( " passed with a grade ")
elif marks >50:
    print ( " passes with b grade")
elif marks>40 :
    print ( " passes with c grade")
elif marks>33:
    print ( " passes with d grade")
else :
    print ( "fail ")
    


# In[59]:


x =input("enter students name :-")
a =int (input("enter your hindi marks :-"))
b =int (input("enter your english marks :-"))
c =int (input("enter your social science marks :-"))
d =int (input("enter your science marks :-"))
e =int (input("enter your math marks :-"))
f = (( a+b+c+d+e)/5)
print ( "your percentage is", f)

if f>60:
    print ( " passed with a grade ")
elif f >50:
    print ( " passes with b grade")
elif f>40 :
    print ( " passes with c grade")
elif f>33:
    print ( " passes with d grade")
else :
    print ( "fail ")
    


# In[64]:


x = int (input("enter number:-"))
if x>0 :
    print('positive')
else:
    print ("negative")


# In[72]:


# enter city  and get famous monuments 
x = input('enter city name :-')
if x == "delhi" :
   print ("red fort")
elif x == "agra" :
   print ("tajmahal")
elif x == "ayodhya" :
   print ("rammandir")
elif x == "prayagraj" :
   print ("sangam")
elif x == "jaipur" :
   print ("hawamahal")
elif x == "uttrakhand" :
   print ("nainitaal")
elif x == "nepal" :
   print ("pashupatinath")
elif x == "gujrat":
   print ("somnath")
elif x == 'punjab' :
   print ("golden temple")
elif x == 'mumbai' :
   print ("gateway of india")    
elif x == 'hydrabad' :
   print ("charminaar")
else :
   print("welcome to karachi")   


# # concepts of loops in python

#  while loops

# In[77]:


a = 6
i= 1
while i <= a :
    print (i)
    i= i+1


# In[83]:


x= int(input("enter number :-"))
i = 1
while i<=10:
    print(x*i)
    i = i + 1


# In[94]:


x = input ("enter your word ")
i =1
while i <= 10 :
    print (x)
    i =i +1


# # using else statement in the whileloop

# In[96]:


x = input ("enter your word ")
i =1
while i <= 10 :
    print (x)
    i =i +1
else :  
    print ("out of number ")


# # for loop  concept 

# In[102]:


fruits =[ "mango","banana" , "apple"]
for x in fruits :
    print(x)


# In[103]:


for i in "banana":
    print(i)


# In[107]:


for x in range (22):
    print(x)


# # user defined function

# In[108]:


def sumit():
       print ("welcome to my world")
       


# In[109]:


sumit()


# In[114]:


def contact():
    print("contact details of school")
    print("email of school")
    print("govt excellence higher secondary  school")
    print("jay shree ram")


# In[115]:


for i in range (4):
    a = input("enter student name:- ")
    b =int(input("enter english marks:-"))
    c =int(input("enter hindi marks":-))
    d =int(input("enter maths marks":-))
    contact()


# In[121]:


def function(fname):
    print(fname + " " + "patel")


# In[122]:


function("amit")
function("sumit")


# # elctricity bill

# In[123]:


def bill():
    print ( "la
           st date : 12/12/2024")
    print(" late fine /- 1000")


# In[132]:


a = input("enter your name :-")
n = int(input("enter your bill :-"))
print("your total bill is :- ", n * 10,'RS/--')
bill()


       


# # STRINGS
# 
# 

# In[134]:


A = " welcome to my world"
print(A,type(A))


# In[147]:


a =""" Our Crop Disease Detection and Advisory System project is a cutting-edge initiative aimed at revolutionizing 
agriculture and ensuring food security for a growing global population. We are a dedicated team of experts in agriculture,
technology, and data science who have come together to address the critical challenges faced by farmers in detecting and 
managing crop diseases effectively.

In a world where climate change and evolving pathogens threaten crop health, our project leverages advanced 
technologies to provide farmers with real-time solutions. Our system combines the power of image recognition, data analysis, and AI-driven algorithms to swiftly identify and diagnose crop diseases. By harnessing the potential of smartphones and other portable devices, we enable farmers to easily capture images of diseased crops and receive immediate, accurate feedback on the condition.

Our vision extends beyond mere disease detection. We believe in proactive agricultural practices, and as
such, our project provides actionable insights and recommendations to mitigate crop diseases. Farmers receive 
personalized advisory information on crop protection measures, including suitable pesticides, cultural practices, and even weather forecasts. We understand that each farm is unique, and our system tailors its advice to individual farm conditions.

Moreover, we are committed to the principles of sustainability and environmental stewardship. Our advisory system
promotes the responsible use of resources, minimizing the need for excessive chemical applications and fostering
environmentally friendly farming practices.

In collaboration with agricultural organizations, local communities, and government bodies, we aim to democratize 
access to vital information and tools that can enhance crop yields and livelihoods. By providing a platform that 
bridges the digital divide, we empower farmers, particularly in remote and underserved regions, to make informed
decisions and secure their agricultural investments.

Our Crop Disease Detection and Advisory System project is not just a technological marvel; it's a commitment to a
more resilient and food-secure world. We are driven by the belief that when we support our farmers, we strengthen 
our communities and ensure a sustainable future for generations to come. """

print(a)
print(len(a))


# # indexing and slicing in string

# In[155]:


a = "hello students"
print (a[6])
print (a[6 :9])
print (a[6:])
print (a[:6])
print(len(a))
print(a.lower())
print(a.upper())
print(a.title())
print(a.replace("hello","bhago"))
print(a.replace("s","p"))
b =a.find("s")
print(b)


# 
# # list concept in python

# In[157]:


mylist =["apple","banna","mango"]
print(mylist)
print(type(mylist))


# In[159]:


mylist =["apple","banna","apple",22,22.45]
print(mylist)


# In[160]:


print(len(mylist))


# In[161]:


print(mylist[2])


# In[162]:


print(mylist[1:4])


# In[163]:


print(mylist[1:4:2])


# # change item in list 

# In[166]:


mylist =["apple","banna","apple",22,22.45]
mylist[1]="ram"
print(mylist)


# # change a range of item values

# In[167]:


a= [33,56,774,36,"sumit",46,883,74]
a[2:5]= "amit"
print(a)


# In[169]:


a.append("sumit")
print(a)


# In[170]:


a.remove("sumit")
print(a)


# In[180]:


s= [22,3454,66,3,5,26,63,56,646,]
print(len(s))
a = 0
for i in range(9):
    a = a+s[i]
    i =i+1
print("the sum is :-", a)   


# # tuples concepts

# In[187]:


a  = (22,44,55,667,77,"sumit",[22,454,677,33])
print (a)
print(type(a))


# In[188]:


b = (2,)
print(b)
print(type(b))


# # tuple constructor

# In[192]:


a = tuple(("ram","shyam","geeta",343,66,34,334,56,343))
print(a)
print(type(a))
print(a[5])     #indexing
print(a[3:7])    #slicing


# # reverse tuple

# In[195]:


a = tuple(("ram","shyam","geeta",343,66,34,334,56,343))
print(a[::-1])


# 
# # append in tupple ( also perform another task with same process like reverse etc)

# In[196]:


a = (22,334,556,778,33)
b = list(a)
b.append("sumit")
print(b)


# In[197]:


a = (22,444,42,556,67,44,66)
b = (22,334,556,778,33)
c = a + b
print(c)


# In[198]:


b = (22,334,556,778,33)
c = b*5
print(c)


# # dictionary 

# In[211]:


a = {
    "name":"sumit",
    "father name" : " sanatkumar singh ",
       "name":"sumit",
    "number":123
}
print(a["name"])


# In[212]:


print(len(a))


# # dict constructor 

# In[218]:


dict={
    "name":"sumit",
    "father name" : " sanatkumar singh ",
       "name":"sumit",
    "number":123
}
print(dict)


# In[219]:


a = {
    "name":"sumit",
    "father name" : " sanatkumar singh ",
       "name":"sumit",
    "number":123
}
print(a.get("name"))


# In[225]:


a["name"] = "amit"              #ADD
print(a["name"])
print(a)


# In[226]:


a.pop("name")                    #delate
print(a)


# In[227]:


a.clear()                         #clear
print(a)


# In[ ]:




