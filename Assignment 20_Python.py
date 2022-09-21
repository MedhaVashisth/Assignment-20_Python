#!/usr/bin/env python
# coding: utf-8

# In[3]:


test1 = 'This is a test of the emergency text system,'
filee = open('test.txt','w')
filee.write(test1)


# In[4]:


file2 = open('test.txt','r')
test2 = file2.readline()
test2


# In[5]:


if test1==test2:
    print('Both are same')


# In[6]:


import csv
rows =[ ['title','author','year'],
    ['The Weirdstone of Brisingamen','Alan Garner',1960],
    ['Perdido Street Station','China Miéville',2000],
    ['Thud!','Terry Pratchett',2005],
    ['The Spellman Files','Lisa Lutz',2007],
    ['Small Gods','Terry Pratchett',1992]]
with open('books.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)


# In[7]:


import sqlite3
conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('create table books(title varchar(20),author varchar(20), year int)')
conn.commit()


# In[8]:


import pandas as pd

read_books = pd.read_csv('books.csv',encoding='unicode_escape')
read_books.to_sql('books', conn, if_exists='append', index = False)


# In[9]:


c.execute('select title from books order by title asc')
print(c.fetchall())


# In[10]:


c.execute('select title, author,year from books order by year')


df = pd.DataFrame(c.fetchall(), columns=['title','author','year'])
df


# In[11]:


import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///books.db")
rows = engine.execute('select * from books')
for i in rows:
    print(i)


# In[12]:


get_ipython().system('pip install redis')


# In[15]:


import redis
conn = redis.Redis()
conn.delete('test')
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hgetall('test')


# In[14]:


conn.hincrby('test','count', 3)


# In[ ]:




