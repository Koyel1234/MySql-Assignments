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
                            password = "*****" #write your own password in place of asterisks
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


# No database named 'first4' is present. Create new database 'first4'
cursor.execute('create database first4')


# In[8]:


# use new database 'first4'
cursor.execute('use first4')


# In[9]:


# create tables in database 'first4'

# Table 'Book'
cursor.execute('create table Book'
     '('
     'Book_id varchar(7) primary key,'
     'Title varchar(20),'
     'Author varchar(20),'
     'Subject varchar(20),'
     'Price int(6)'
     ')'
)


# In[10]:


cursor.execute('desc Book')


# In[11]:


cursor.fetchall()


# In[12]:


# Table 'Borrower'
cursor.execute('create table Borrower'
     '('
     'B_id varchar(5) primary key,'
     'B_name varchar(20) not null,'
     'Addr varchar(10),'
     'Contact bigint(15),'
     'Age int(3)'
     ')'
)


# In[13]:


cursor.execute('desc Borrower')
cursor.fetchall()


# In[14]:


# Table 'Borrows'
cursor.execute('create table Borrows'
     '('
     'Book_id varchar(7) references Book,'
     'B_id varchar(5) references Borrower,'
     'Date_of_issue date,'
     'Date_of_return date,'
     'Fine int(5)'
     ')'

)


# In[15]:


cursor.execute('desc Borrows')
cursor.fetchall()


# In[16]:


query="insert into Book(Book_id,Title,Author,Subject,Price) values (%s,%s,%s,%s,%s)"
values=[("bk01","Initial Mathamatics","Patra","Mathematics","800"),
  ("bk02","Funda of Stats","Matariya","Statistics","800"),  
  ("bk03","Computer A B C D","Sinha","Computer Science","720"), 
  ("bk04","Calculas Analysis","Abel","Mathematics","650"),  
  ("bk05","Maths Analysis","Rudin","Mathematics","330"),  
  ("bk06","Computer Fundamental","Simona","Computer Science","470")]
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[17]:


cursor.execute('select * from Book')
cursor.fetchall()


# In[18]:


query="insert into Borrower (B_id,B_name,Addr,Contact,Age) values (%s,%s,%s,%s,%s)"
values= [("bo01","Saheb","Kolkata",9847752101,25),  
  ("bo02","Smita","Asam",7454845210,30),  
  ("bo03","Aman","Kolkata",9899845120,55),  
  ("bo04","Kabita","Kolkata",8958412561,45),  
  ("bo05","Sima","Krishnagar",8899747152,65), 
  ("bo06","Ananta","Bidhanpur",9932254125,20)  
] 
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[19]:


cursor.execute('select * from Borrower')
cursor.fetchall()


# In[20]:


query="insert into Borrows (Book_id,B_id,Date_of_issue,Date_of_return,Fine) values (%s,%s,%s,%s,%s)"
values= [("bk05","b02","2019-05-14","2019-06-21",31),
 ("bk04","b01","2018-07-14","2018-07-30",9), 
 ("bk05","b03","2019-05-14","2019-06-21",62), 
 ("bk02","b06","2018-11-22","2019-01-21",53), 
 ("bk05","b02","2019-05-15","2019-06-21",30),
 ("bk05","b02","2019-10-19","2019-10-26",0)]
cursor.executemany(query,values)
print('Row inserted', cursor.lastrowid)


# In[21]:


cursor.execute('select * from Borrows')
cursor.fetchall()


# In[22]:


cursor.execute('desc Book')
df_Book_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Book_structure


# In[23]:


cursor.execute('select * from Book')
df_Book_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Book_records


# In[24]:


cursor.execute('desc Borrower')
df_Borrower_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Borrower_structure


# In[25]:


cursor.execute('select * from Borrower')
df_Borrower_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Borrower_records


# In[26]:


cursor.execute('desc Borrows')
df_Borrows_structure = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Borrows_structure


# In[27]:


cursor.execute('select * from Borrows')
df_Borrows_records = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_Borrows_records


# In[28]:


# Query_1
# Find out the books with maximum price
cursor.execute('select * from Book where price in(select max(price) from Book)')
df_query_1 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_1


# In[29]:


# Query_2
# Find out the books of Computer Science with maximum price
cursor.execute('select * from Book where subject like "Computer Science" and price in(select max(price) from book where subject like "Computer Science")')
df_query_2 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_2


# In[30]:


# Query_3
# Find out the total number of books under each subject in the above database
cursor.execute('select subject, count(Book_id) "Total no. of books" from Book group by subject')
df_query_3 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_3


# In[31]:


# Query_4
# Find out the total number of books priced above 500 under each subject in the database
cursor.execute('select subject, count(Book_id) "Total no. of books where price>500" from Book where price>500 group by subject')
df_query_4 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_4


# In[32]:


# Query_5
# Find out the subject of the book for which more than or equal to two books exists in the database
cursor.execute('select subject "Subject for which >=2 books exists in the database", count(book_id) from book group by subject having count(Book_id)>=2')
df_query_5 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_5


# In[33]:


# Query_6
# Display the average age of borrowers whose name starts with 'S'
cursor.execute('select avg(age) "Average age of borrowers with name starting with S" from borrower where b_name like "S%"')
df_query_6 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_6


# In[34]:


# Query_7
# Display borrower name who lives in Kolkata
cursor.execute('select b_name from borrower where addr="kolkata"')
df_query_7 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_7


# In[35]:


# Query_8
# Display the title of books whose author's name is of 5 characters
cursor.execute('select title from book where author like "_____"')
df_query_8 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_8


# In[36]:


# Query_9
# Display the title of Books whose author's name's 3rd letter is 't'
cursor.execute('select title from book where author like "__t%"')
df_query_9 = pd.DataFrame.from_records(cursor.fetchall(), columns = [desc[0] for desc in cursor.description])
df_query_9

