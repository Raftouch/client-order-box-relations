print("Hello 🙂")

import sqlite3

connection = sqlite3.connect("data/customizable_storage_boxes.db")

cursor = connection.cursor()

create_table_clients = '''CREATE TABLE IF NOT EXISTS clients (
    client_id VARCHAR(6) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255))'''

create_table_orders = """CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    client_id VARCHAR(6),
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (client_id) REFERENCES clients(client_id))"""

create_table_order_boxes = """CREATE TABLE IF NOT EXISTS order_boxes (
    order_box_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    box_id INTEGER,
    quantity INTEGER NOT NULL,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (box_id) REFERENCES boxes(box_id))"""

create_table_boxes = """CREATE TABLE IF NOT EXISTS boxes (
    box_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER,
    color_id INTEGER,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    length INTEGER NOT NULL,
    surface DECIMAL(10, 2),
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id),
    CHECK (width <= 1000 AND height <= 1000 AND length <= 1000))"""

create_table_materials = """CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(100) NOT NULL)"""

create_table_colors = """CREATE TABLE IF NOT EXISTS colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL)"""

create_table_material_colors = """CREATE TABLE IF NOT EXISTS material_colors (
    material_color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER,
    color_id INTEGER,
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id))"""

create_table_pricing = """CREATE TABLE IF NOT EXISTS pricing (
    pricing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER,
    color_id INTEGER,
    quantity INTEGER NOT NULL,
    base_price DECIMAL(10, 2),
    final_price DECIMAL(10, 2),
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id))"""

cursor.execute(create_table_clients)
cursor.execute(create_table_orders)
cursor.execute(create_table_order_boxes)
cursor.execute(create_table_boxes)
cursor.execute(create_table_materials)
cursor.execute(create_table_colors)
cursor.execute(create_table_material_colors)
cursor.execute(create_table_pricing)

connection.commit()

print("tables created successfully")
print("***************************")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("there are following tables in the database:")
for table in tables:
    print(table[0])

connection.close()