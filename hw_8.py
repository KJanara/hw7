import sqlite3

def create_connection(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except sqlite3.Error as e:
    print(e)
  return conn


def create_table(conn, sql):
  try:
    cursor = conn.cursor()
    cursor.execute(sql)
  except sqlite3.Error as e:
    print(e)

def insert_countries(conn,  countries):
  sql = '''INSERT INTO  countries (title)
  VALUES (?)
  '''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, countries)
    conn.commit()
  except sqlite3.Error as e:
    print(e)

def select_all_countries(conn):
  sql = '''SELECT * FROM countries'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql)

    rows_list = cursor.fetchall()
    for row in rows_list:
      print(row)
  except sqlite3.Error as e:
    print(e)

def select_all_cities(conn):
  sql = '''SELECT * FROM cities'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql)

    rows_list = cursor.fetchall()
    for row in rows_list:
      print(row)
  except sqlite3.Error as e:
    print(e)


def select_all_employees(conn):
  sql = '''SELECT * FROM employees'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql)

    rows_list = cursor.fetchall()
    for row in rows_list:
      print(row)
  except sqlite3.Error as e:
    print(e)


def display_cities(conn):
  sql = '''SELECT title FROM cities'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql)

    rows_list = cursor.fetchall()
    for row in rows_list:
      print(row)
  except sqlite3.Error as e:
    print(e)


def display_employees_by_city(conn, city_id):
  sql = '''        SELECT employees.first_name, employees.last_name, \
  countries.title, cities.title, cities.area
        FROM employees
        JOIN cities ON employees.city_id = cities.c_id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.c_id = ?'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, city_id)

    rows_list = cursor.fetchall()
    for row in rows_list:
      print(row)
  except sqlite3.Error as e:
    print(e)

sql_create_countries_table = '''
CREATE TABLE countries(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR NOT NULL )
'''

sql_create_cities_table ='''CREATE TABLE cities (
c_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR NOT NULL,
area FLOAT DEFAULT 0,
country_id INTEGER REFERENCES countries(id)
);'''


sql_create_employees_table ='''CREATE TABLE employees (
    e_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    city_id INTEGER REFERENCES cities(c_id)
)'''
connection = create_connection('hw8.db')
print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
display_cities(connection)
if connection is not None:
  # print('Successfully connected!')
  # create_table(connection, sql_create_countries_table)
  # create_table(connection, sql_create_cities_table)
  # create_table(connection, sql_create_employees_table)
  # select_all_countries(connection)
  # select_all_cities(connection)
  # select_all_employees(connection)
  while True:
    try:
      city_id = input("Введите id выбранного города")
      if city_id == 0:
        break
      display_employees_by_city(connection, city_id)
    except ValueError:
      print("Введите целое число.")
  connection.close()
