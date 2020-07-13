#!/usr/bin/env python
# coding: utf-8

# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[2]:


7 ** 4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[5]:


s = "Hi there Sam!"


# In[8]:


s.split(" ")


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[5]:


planet = "Earth"
diameter = 12742


# In[2]:


print("The diameter of Earth is {} kilometers".format(12742))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[7]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[10]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[16]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[13]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d.get('k1')[3].get('tricky')[3].get('target')[3]


# ** What is the main difference between a tuple and a list? **

# In[15]:


# Tuple is immutable 


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[16]:


def domainGet(domainUrl):
    return domainUrl.split("@")[-1]


# In[19]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[22]:


def findDog(inputStr): 
    return 'dog' in inputStr


# In[24]:


findDog('Is there a nothing here?')


# In[25]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[27]:


def countDog(inputStr): 
    return inputStr.count('dog')


# In[28]:


countDog('This dog dog dog dog runs faster than the other dog dude!')


# In[29]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[34]:


seq = ['soup','dog','salad','cat','great']


# In[34]:


seq = ['soup','dog','salad','cat','great']
result = list(filter(lambda x: (x[0] == 's'), seq))
print(result)


# In[ ]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[35]:


def caught_speeding(speed, is_birthday):
    if is_birthday: speed -= 5 
    
    if (speed >= 81):
        return "Big Ticket"
    elif (61 <= speed <= 80): 
        return "Small ticket"
    else:
        return "No ticket"
    

        


# In[40]:


caught_speeding(81,True)


# In[41]:


caught_speeding(81,False)


# # Great job!
