#!/usr/bin/env python
# coding: utf-8

# In[3]:


#function

def test (a,b):
    print(a+b)
test(5,4)
test(10,20)
test(20,30)


# In[6]:


def test (a,b,c,d):
    print(a+b+c+d)
test(5,4,4,1)
test(10,20,2,1)
test(20,30,2,2)
def test (f,g):
    print(f*g)
test(1,2)


# In[17]:


def add(a,b):
    return(a+b)

a=add(5,4)
b=add(a,10)
c=add(b,20)

print(a)
print(b)
print(c)


# In[24]:


a ='hello'
def test():
    global a
    a = 'hi'
    return a
print(a)
a=test()
print(a)
    


# In[29]:


a ='hello'
def test():
    global a
    a='hi'
    print(a)
test()
print(a)


# In[30]:


a ='hello'
def test():
    
    
    a='hi'
    print(a)
test()
print(a)


# In[ ]:




