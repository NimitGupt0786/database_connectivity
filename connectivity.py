import mysql.connector

connection = 
mysql.connector.connect(host='127.0.0.1',username='root',passwd='Gupta6969',database='students')

cursor = connection.cursor()

cursor.execute("select * from student")
for i in cursor:
    print(i,'all')

cursor.execute("select * from student where name='nimit'")
for i in cursor:
    print(i,'name')

try:
    sql = "INSERT INTO student (name, college) VALUES (%s, %s)"
    values = [('Nitish', 'thapar')]
    cursor.executemany(sql, values)

    connection.commit()

except mysql.connector.Error as error:
    connection.rollback()

try:
    sql = "delete from student where name = 'Nitish'"
    cursor.execute(sql)

    connection.commit()

except mysql.connector.Error as error:
    connection.rollback()

cursor.close()
connection.close()
