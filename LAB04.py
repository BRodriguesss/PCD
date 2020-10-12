#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1) Ask the user to insert this name and age. Then calculate his birth year.

name=input("Whats your name? ")
age=input("Whats your age? ")

from datetime import date
today = date.today()
today.year


# In[ ]:


age = 25
birthyear = today.year - age
print (birthyear)


# In[ ]:


#2) Ask the user to insert a text. The program will always answer "yes". The conversation will be closed when the user says "bye",

text= ''
text=input("Insert text: ")
while text!= 'bye':
    print("yes")
    text=input("Insert text: ")


# In[ ]:


#3) Create a function for a greeting.

def greet():
    print("Hello!")


# In[ ]:


#4) Call greeting function at the beginning of the conversation.

greet()
text =""
text = input("Insert text: ")
while text != "bye" :
    print("yes")
    text = input("Insert text: ")


# In[ ]:


#5) Improve your chatbot

def greetUser(name):
    "" "Show a custom message." ""
    print("Hello," + name + "!")


# In[ ]:


greetUser(name)

