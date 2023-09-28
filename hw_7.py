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


def insert_products(conn, products):
  sql = '''INSERT INTO products
  (product_title, price, quantity)
  VALUES (?, ?, ?)
  '''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, products)
    conn.commit()
  except sqlite3.Error as e:
    print(e)


def update_products_quantity(conn, products):
  sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, products)
    conn.commit()
  except sqlite3.Error as e:
    print(e)


def update_products_price(conn, products):
  sql = '''UPDATE products SET price = ? WHERE id = ?'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, products)
    conn.commit()
  except sqlite3.Error as e:
    print(e)


def delete_products(conn, id):
  sql = '''DELETE FROM products WHERE id = ?'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
  except sqlite3.Error as e:
    print(e)


def select_all_products(conn):
  sql = '''SELECT * FROM products'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql)

    rows_list = cursor.fetchall()
    for row in rows_list:
      print(row)
  except sqlite3.Error as e:
    print(e)


def choose_products(conn):
  sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(cursor.fetchall())

  except sqlite3.Error as e:
    print(e)


def search_products(conn, products):
  sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
  try:
    cursor = conn.cursor()
    cursor.execute(sql, ("%"+products+"%",))
    conn.commit()
    print(cursor.fetchall())

  except sqlite3.Error as e:
    print(e)



connection = create_connection('hw.db')

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL ,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0)
'''


if connection is not None:
  print('Successfully connected!')
  # create_table(connection, sql_create_products_table)

  # insert_products(connection, ('Coca-cola', 110.0, 10))
  # insert_products(connection, ('Zero cola', 100.0, 10))
  # insert_products(connection, ('Pepsi', 120.0, 10))
  # insert_products(connection, ('Кефир', 90.0, 5))
  # insert_products(connection, ('Био кефир ванильный', 100.0, 5))
  # insert_products(connection, ('Био кефир клубничный ', 110.0, 10))
  # insert_products(connection, ('Рис ташкенский', 150.0, 3))
  # insert_products(connection, ('Рис узгенсикй', 160.0, 6))
  # insert_products(connection, ('Творог с изюмом', 80.0, 8))
  # insert_products(connection, ('Творог с ванилью', 85.0, 8))
  # insert_products(connection, ('Творог с киви', 85.0, 8))
  # insert_products(connection, ('Шоро тан', 110.0, 14))
  # insert_products(connection, ('Шоро максым', 100.0, 14))
  # insert_products(connection, ('Шоро бозо', 115.0, 14))
  # insert_products(connection, ('Шоро чалап', 115.0, 14))


  select_all_products(connection)
  # update_products_price(connection,(125, 5))
  # update_products_quantity(connection, (5, 11))
  # delete_products(connection,10)
  # choose_products(connection)
  # search_products(connection, 'Шоро' )
  connection.close()
