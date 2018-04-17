import mysql.connector
import mysql

def showTasks():
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='userdb')
    cursor = connection.cursor()

    sql= 'SELECT description FROM tasks'

    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    print(result)

    return result

def addTask(arg):
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='userdb')
    cursor = connection.cursor()

    sql= 'INSERT into tasks(description) VALUES (%s)'

    cursor.execute(sql,(arg,))
    cursor.commit()
    cursor.close()
    connection.close()

def removeTask(task):
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='userdb')
    cursor = connection.cursor()

    sql = 'DELETE from tasks WHERE description=%s'

    cursor.execute(sql, (task,))
    cursor.commit()
    cursor.close()
    connection.close()

def removeAll(task):
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='userdb')
    cursor = connection.cursor()

    sql = "DELETE * from tasks WHERE description LIKE '%s'"

    cursor.execute(sql, (task,))
    cursor.commit()
    cursor.close()
    connection.close()
