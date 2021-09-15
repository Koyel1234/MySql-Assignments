#!/usr/bin/env python
# coding: utf-8

# In[1]:


# install neccessary library to connect MySQL with python
#pip install mysql-connector-python


# In[2]:


import mysql.connector as sql

#creating connection between MySQL and python
connection = sql.connect(
                            host = "localhost",
                            user = "root",
                            password = "123456789"
                        )


# In[3]:


#printing the connection
print(connection)


# In[4]:


cursor = connection.cursor()


# In[5]:


# to get all existing databases
cursor.execute('show databases')


# In[6]:


# to print all existing databases
for database in cursor:
    print(database)


# In[7]:


# No database named 'first2' is present. Create new database 'first2'
cursor.execute('create database first2')


# In[8]:


# use new database 'first2'
cursor.execute('use first2')


# In[9]:


# create tables in database 'first2'

# Table 'Sailors'
cursor.execute('create table Sailors('
     's_id varchar(5) primary key,'
     's_name varchar(20),'
     'rating int(2),'
     'age int(3))'
)


# In[10]:


cursor.execute('desc Sailors')


# In[11]:


cursor.fetchall()


# In[12]:


# Table 'Boats'
cursor.execute('create table Boats'
     '('          
     'b_id varchar(5) primary key,'
     'b_name varchar(10),'
     'colour varchar(10)'
     ')'
)


# In[13]:


cursor.execute('desc Boats')
cursor.fetchall()


# In[14]:


# Table 'Reserves'
cursor.execute('create table Reserves'
     '('
     's_id varchar(5) references Sailors,'
     'b_id varchar(5) references Boats,'
     'R_date date,'
     'day varchar(11)'
     ')'
)


# In[15]:


cursor.execute('desc Reserves')
cursor.fetchall()


# In[16]:


query="insert into Sailors (s_id, s_name, rating, age) values (%s,%s,%s,%s)"
values=[("s01","John",1,19),
       ("s02","Tapan",7,25),
       ("s03","Jack",4,30),
       ("s04","Tirthan",5,50),
       ("s05","Rabi",3,35),
       ("s06","Virat",2,16)]
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[17]:


cursor.execute('select * from Sailors')
cursor.fetchall()


# In[18]:


query="insert into Boats (b_id, b_name, colour) values (%s,%s,%s)"
values= [("b01","titanic","white"),  
  ("b02","alloha","red"),     
  ("b03","mona","black"),   
  ("b04","ujbhumi","red"),     
  ("b05","orion","black"),   
  ("b06","escape","white")] 
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[19]:


cursor.execute('select * from Boats')
cursor.fetchall()


# In[20]:


query="insert into Reserves (s_id, b_id, R_date, day) values (%s,%s,%s,%s)"
values= [("s01","b01","2019-03-23","monday"),
  ("s02","b01","2019-01-15","monday"), 
  ("s01","b06","2019-02-20","wednesday"),  
  ("s03","b01","2018-02-01","sunday"), 
  ("s04","b06","2019-08-05","tuesday"),
  ("s01","b02","2017-01-17","friday"),
  ("s02","b03","2016-10-08","thursday"),
  ("s06","b05","2019-12-09","friday")]
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[21]:


cursor.execute('select * from Reserves')
cursor.fetchall()


# In[22]:


cursor.execute('desc Sailors')
df_Sailors_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Sailors_structure


# In[23]:


cursor.execute('select * from Sailors')
df_Sailors_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Sailors_records


# In[24]:


cursor.execute('desc Boats')
df_Boats_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Boats_structure


# In[25]:


cursor.execute('select * from Boats')
df_Boats_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Boats_records


# In[26]:


cursor.execute('desc Reserves')
df_Reserves_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Reserves_structure


# In[27]:


cursor.execute('select * from Reserves')
df_Reserves_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Reserves_records


# In[28]:


# Query_1
# Find the ID, rating and age of sailors whose name is either "John" or "Jack" or "Rabi"
cursor.execute('select s_id, rating, age from Sailors where s_name in ("John","Jack","Rabi")')
df_query_1 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_1


# In[29]:


# Query_2
# List the name of sailors whose age lies between 18 and 30
cursor.execute('select s_name from Sailors where age>=18 and age<=30')
df_query_2 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_2


# In[30]:


# Query_3
# Find the name and age of Sailors whose name starts with "T" and end with "n" in descending order of age
cursor.execute('select s_name from Sailors where s_name like "T%n" order by age desc')
df_query_3 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_3


# In[31]:


# Query_4
# List the name of Sailors who reserve "white" color boats on Monday
cursor.execute('select s_name from Sailors, Boats, Reserves where Sailors.s_id=Reserves.s_id and Boats.b_id=Reserves.b_id and day="Monday" and colour="white"')
df_query_4 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_4


# In[32]:


# Query_5
# List the name of boats which are reserved by sailors with age greater than 25
cursor.execute('select b_name from Sailors, Boats, Reserves where Sailors.s_id=Reserves.s_id and Boats.b_id=Reserves.b_id and age>25')
df_query_5 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_5


# In[33]:


# Query_6
# Find the name of sailors who reserve "red" and "white" color boats
cursor.execute('select s_name from Sailors, Boats, Reserves where Sailors.s_id=Reserves.s_id and Boats.b_id=Reserves.b_id and colour="red" or colour="whte"')
df_query_6 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_6


# In[34]:


# Query_7
# List the name of sailors who reserve white or black colored boat order by boat ID
cursor.execute('select s_name from Sailors, Boats, Reserves where Sailors.s_id=Reserves.s_id and Boats.b_id=Reserves.b_id and (colour="white" or colour="red") order by boats.b_id')
df_query_7 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_7

