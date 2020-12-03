import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username txt, password txt)"
cursor.execute(create_table)

user = (1, 'sri', 'asdf')
insert_query = "INSERT INTO  users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'siri', 'xyz'),
    (3, 'anji', 'abc')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()




