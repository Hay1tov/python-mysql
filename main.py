import mysql.connector
import setting

connection = mysql.connector.connect(
    host=setting.host,
    user=setting.user,
    password=setting.password,
    port=setting.port,
    # database=settings.db_name
)

cursor = connection.cursor()

cursor.execute("use education")

cursor.execute('''
create table if not exists student (
    id int auto_increment primary key,
    name varchar(64),
    grade int,
    age int
)
''')

cursor.execute("""insert into student (name, grade, age)
            values ('nurbek', 2, 17), ('sherbek', 3, 18);""")

cursor.execute('select * from student')

# cursor.execute("SHOW TABLES")

rows = cursor.fetchall()

print(rows)

cursor.close()
connection.close()


# educaiton db
# students table (id, name, grade, age)
# 10 students
# select all
# filter age increasing

