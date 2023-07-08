import mysql.connector

connection = 
mysql.connector.connect(host='127.0.0.1',username='root',passwd='Gupta6969',database='students') #it returns the connection after authenticating the username and password

cursor = connection.cursor()                    #it acts a pointer to the database which we have connected to

cursor.execute("select * from student")         #it stores the result of the command executed

for i in cursor:                                #it is used to print the result stored in 8th line
    print(i,'all')

cursor.execute("select * from student where name='nimit'")

for i in cursor:
    print(i,'name')

try:
    sql = "INSERT INTO student (name, college) VALUES (%s, %s)" # it is the practical implementation how commands canbe run and exectued and make changes in original database 
    values = [('Nitish', 'thapar')]
    cursor.executemany(sql, values)

    connection.commit()

except mysql.connector.Error as error:
    connection.rollback()

try:
    sql = "delete from student where name = 'Nitish'"    # it is the practical implementation how commands canbe run and exectued and make changes in original database 
    values = [('Nitish', 'thapar')]
    cursor.execute(sql)

    connection.commit()

except mysql.connector.Error as error:
    connection.rollback()

cursor.close()
connection.close()
