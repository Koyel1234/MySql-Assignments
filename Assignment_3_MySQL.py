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


# No database named 'first3' is present. Create new database 'first3'
cursor.execute('create database first3')


# In[8]:


# use new database 'first3'
cursor.execute('use first3')


# In[9]:


# create tables in database 'first3'

# Table 'Doctor'
cursor.execute('create table Doctor'
      '('
      'DocId varchar(5) primary key,'
      'Dname varchar(20) not null,'
      'Specialist varchar(15),'
      'experience int(2)'
      ')'
)


# In[10]:


cursor.execute('desc Doctor')


# In[11]:


cursor.fetchall()


# In[12]:


# Table 'Room'
cursor.execute('create table Room'
      '('
      'RID varchar(5) primary key,'
      'Rate int(8) not null,'
      'Floor_no int(2),'
      'date date'
      ')'
)


# In[13]:


cursor.execute('desc Room')
cursor.fetchall()


# In[14]:


# Table 'Patient'
cursor.execute('create table Patient'
      '('
      'PID varchar(5) primary key,'
      'Pname varchar(20) not null,'
      'RID varchar(5) references Room,'
      'DocId varchar(5) references Doctor,'
      'age int(3),'
      'sex varchar(6),'
      'phone bigint(12)'
      ')'
)


# In[15]:


cursor.execute('desc Patient')
cursor.fetchall()


# In[16]:


query="insert into Doctor(DocId,Dname,Specialist,experience) values(%s,%s,%s,%s)"
values=[("d01","Dr.Supratik","surgery",15),
  ("d02","Dr.Liza","medicine",5),  
  ("d03","Dr.Somen","surgery",7),  
  ("d04","Dr.Debesh","medicine",8),  
  ("d05","Dr.Ashok","medicine",10),  
  ("d06","Dr.Dipa","child",9),  
  ("d07","Dr.Sikha","child",18)]
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[17]:


cursor.execute('select * from Doctor')
cursor.fetchall()


# In[18]:


query="insert into Room (RID,Rate,Floor_no,date) values (%s,%s,%s,%s)"
values= [("R01",1550,1,"2019-01-25"),
  ("R02",1800,2,"2018-12-22"),
  ("R03",1300,4,"2019-05-31"),
  ("R04",1420,1,"2019-06-30"),
  ("R05",1870,3,"2017-11-22"), 
  ("R06",2500,4,"2019-03-15")] 

cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[19]:


cursor.execute('select * from Room')
cursor.fetchall()


# In[20]:


query="insert into Patient (PID,Pname,RID,DocId,age,sex,phone) values (%s,%s,%s,%s,%s,%s,%s)"
values= [("p01","Rusha Dey","R05","d01",48,"female",9845785825),
 ("p02","Rima Biswas","R02","d03",55,"female",7455489865),
 ("p03","Tanmoy Mondal","R03","d02",28,"male",9814552414), 
 ("p04","Binoya Chanda","R04","d04",30,"female",9988578585),
 ("p05","Riju Dey","R01","d06",5,"male",9814552825), 
 ("p06","Diya Sarkar","R02","d06",2,"female",8478995825), 
 ("p07","Anjan Bera","R03","d07",8,"male",7745100125), 
 ("p08","Dipan Dey","R05","d06",7,"male",7885566321)]
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[21]:


cursor.execute('select * from Patient')
cursor.fetchall()


# In[22]:


cursor.execute('desc Doctor')
df_Doctor_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Doctor_structure


# In[23]:


cursor.execute('select * from Doctor')
df_Doctor_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Doctor_records


# In[24]:


cursor.execute('desc Room')
df_Room_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Room_structure


# In[25]:


cursor.execute('select * from Room')
df_Room_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Room_records


# In[26]:


cursor.execute('desc Patient')
df_Patient_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Patient_structure


# In[27]:


cursor.execute('select * from Patient')
df_Patient_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Patient_records


# In[28]:


# Query_1
# Give the patient names who are admitted under the doctor specialist in "Medicine" and whose room charge is not between 
# Rs. 1500-2000
cursor.execute('select Pname from Doctor d,Room r,Patient p where d.DocId=p.DocId and r.RID=p.RID and specialist like "Medicine" and Rate not between 1500 and 2000')
df_query_1 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_1


# In[29]:


# Query_3
# Find the total number of child patients
cursor.execute('select count(*) "Total no. of child patient" from Doctor d,Patient p where d.DocId=p.DocId and specialist like "child"')
df_query_3 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_3


# In[30]:


# Query_4
# Find details of female patients under "surgery" whose age is greater than 45
cursor.execute('select * from Patient p, Doctor d where d.DocId=p.DocId and sex like "female" and specialist like "surgery" and age>45')
df_query_4 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_4


# In[31]:


# Query_2
# Increase the rate of room by 5% for the 4th floor

# Before increment
cursor.execute('select RID,rate from Room where floor_no=4')
df_query_2_a = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_2_a


# In[32]:


# After increment
cursor.execute('select RID,rate*105/100 "Rate after increment" from Room where floor_no=4')
df_query_2_b = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_2_b


# In[33]:


# Together with increment
cursor.execute('select RID,rate,rate*105/100 "Rate after increment" from Room where floor_no=4')
df_query_c = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_c

