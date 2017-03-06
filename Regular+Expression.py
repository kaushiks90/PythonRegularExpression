
# coding: utf-8

# In[5]:

import re 


# #### Find atleast 1 word which starts with a

# In[21]:

s="abc cvg  rty acc"
var=re.compile('^a\w*')
result=var.match(s)
if result:
    print result.group()


# In[22]:

###Find all the words which starts with a


# In[58]:

s="abc cvg  rty acc"
var=re.findall('^[a]\w*',s)
print var


# ####Find all the digits in the string   s="Kin3423gs Ne32423ver die234234"

# In[44]:

s="Kin3423gs Ne32423ver die234234"
#numbers=re.findall('[0-9]+',s)
numbers=re.findall('\d+',s)
print numbers


# In[62]:

type(False)


# In[63]:

type('Data Science')


# In[66]:

s=False
isinstance(s,bool)


# In[80]:

lis=[0,1,2,3,4,5,6,7,7]
lis[0:3]=["Guido", "Van", "Rossum"]
lis.remove(7)
lis


# In[30]:

s = 'my 1st string!!'


# In[11]:

match=re.search(r'my',s)
print match.group()


# In[13]:

match =re.search(r'st',s)
print match.group()


# In[15]:

match=re.search(r'sta',s)
print match.group()


# In[32]:

match=re.search(r'\w\w\w',s)
print match.group()


# In[23]:

match=re.search(r'\W',s)
print match.group()


# In[31]:

match=re.search(r'\W\W',s)
print match.group()


# In[34]:

match=re.search(r'\s',s)
print match.group()


# In[35]:

match=re.search(r'\s\s',s)
print match.group()


# In[40]:

match=re.search(r'..t',s)
print match.group()


# In[43]:

match=re.search(r'\s\St',s)
print match.group()


# In[45]:

match=re.search(r'\bst',s)
print match.group()


# In[46]:

ss = 'sid is missing class'


# In[48]:

match=re.search(r'miss\w+',ss)
print match.group()


# In[51]:

match=re.search(r'is\w+',ss)
print match.group()


# In[54]:

match=re.search(r'is\w*',ss)
print match.group()


# In[56]:

sss = '<h1>my heading</h1>'


# In[59]:

match=re.search(r'<.+>',sss)
print match.group()


# In[63]:

match=re.search(r'<.+?>',sss)
print match.group()


# In[65]:

match=re.search(r'</.+?>',sss)
print match.group()


# In[66]:

ssss = 'sid is missing class'


# In[69]:

match=re.search(r'^miss',ssss)
print match.group()


# In[71]:

match=re.search(r'..ss',ssss)
print match.group()


# In[73]:

match=re.search(r'..ss$',ssss)
print match.group()


# In[75]:

match=re.search(r'miss\w+',ssss)
print match.group()


# In[77]:

k='my email is john-doe@gmail.com'


# In[83]:

match=re.search(r'\w+@\w+',k)
print match.group()


# In[86]:

match=re.search(r'[\w-]+@[\w.]+\w+',k)
print match.group()


# In[88]:

ks='Name: Cindy, 30 years old'


# In[97]:

match=re.search(r'\d+(?= years? old)',ks)
print match.group()


# In[103]:

match=re.search(r'(?<=Name: )\w+',ks)
print match.group()


# In[104]:

cs = 'emails: nicole@ga.co, joe@gmail.com, PAT@GA.CO'


# In[109]:

match=re.findall(r'\w+@ga\.co',cs)
print match


# In[112]:

match=re.findall(r'\w+@ga\.co',cs,re.I)
print match


# In[114]:

ps='emails: joe@gmail.com, bob@gmail.com'


# In[117]:

match=re.findall(r'[\w]+@[\w.-]+',ps)
print match


# In[122]:

re.findall(r'([\w]+)@', ps)

