import psycopg2

def table():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="PostgreSQL1036",host="localhost",port="5432")
    cursor = conn.cursor()
    cursor.execute('''create table testing(Name text , ID int , Age int);''')
    print('Table created successfully')

    conn.commit()
    conn.close()

    print("Connection Success!!")

# table()




def data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="PostgreSQL1036",host="localhost",port="5432")
    cursor = conn.cursor()
    cursor.execute('''insert into testing(Name, ID , Age ) values ('Sam', 213 ,24);''')
    print('Data added successfully')

    conn.commit()
    conn.close()

# data()



def extract():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="PostgreSQL1036",host="localhost",port="5432")
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchone()
    print(show)

    conn.commit()
    conn.close()

# extract()

def add_data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="PostgreSQL1036",host="localhost",port="5432")
    cursor = conn.cursor()

    name= input('Enter the name:')
    id = input('Enter the ID:')
    age = input('Enter the age:')

    query = ''' insert into employees(Name,id,age) values (%s,%s,%s)'''
    cursor.execute(query,(name,id,age))
    
    print('Data added succesfully')

    conn.commit()
    conn.close()

add_data()
