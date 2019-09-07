import sqlite3
import time

database_name = "Menu"


def open_database_connection(database_name):
    conn = sqlite3.connect(database_name)
    return conn


def open_database_cursor(conn):
    c = conn.cursor()
    return c


conn = open_database_connection(database_name)
c = open_database_cursor(conn)


# Create database if not already created
def create_table_extended(table_name):
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(
                    name TEXT,
                    restaurant TEXT,
                    type_of_item TEXT,
                    calories INTEGER,
                    protein INTEGER,
                    carbs INTEGER,
                    total_fat INTEGER,
                    saturated_fat INTEGER,
                    trans_fat INTEGER,
                    cholesterol INTEGER,
                    sodium INTEGER,
                    sugar INTEGER,
                    fiber INTEGER,
                    oz REAL,
                    price REAL,

                    calories_from_fat INTEGER,
                    calories_from_protein INTEGER,
                    calories_from_carbs INTEGER,
                    protein_efficiency REAL,
                    fat_efficiency REAL,
                    carbs_efficiency REAL,
                    price_efficiency REAL,
                    sodium_ratio REAL,
                    cholesterol_ratio REAL,
                    sugar_ratio REAL,
                    fiber_ratio REAL,
                    protein_per_dollar REAL,
                    far_per_dollar REAL,
                    carbs_per_dollar REAL,
                    sugar_per_oz REAL)''')

def insert_item_extended(table_name, item, conn=conn, c=c):
    with conn:
        exists = get_item_by_name_and_restaurant(table_name=table_name, name=item.name, restaurant=item.restaurant, c=c)
        if exists:
            remove_item(table_name=table_name, name=item.name, restaurant=item.restaurant, conn=conn, c=c)

        c.execute(f'''INSERT INTO {table_name} VALUES (:name, 
                                                       :restaurant, 
                                                       :type_of_item, 
                                                       :calories, 
                                                       :protein, 
                                                       :carbs,
                                                       :total_fat,
                                                       :saturated_fat,
                                                       :trans_fat,
                                                       :cholesterol,
                                                       :sodium,
                                                       :sugar,
                                                       :fiber,
                                                       :oz,
                                                       :price,

                                                       :calories_from_fat,
                                                       :calories_from_protein,
                                                       :calories_from_carbs,
                                                       :protein_efficiency,
                                                       :fat_efficiency,
                                                       :carbs_efficiency,
                                                       :price_efficiency,
                                                       :sodium_ratio,
                                                       :cholesterol_ratio,
                                                       :sugar_ratio,
                                                       :fiber_ratio,
                                                       :protein_per_dollar,
                                                       :fat_per_dollar,
                                                       :carbs_per_dollar,
                                                       :sugar_per_oz)''',
                  {'name': item.name,
                   'restaurant': item.restaurant,
                   'type_of_item': item.type_of_item,
                   'calories': item.calories,
                   'protein': item.protein,
                   'carbs': item.carbs,
                   'total_fat': item.total_fat,
                   'saturated_fat': item.saturated_fat,
                   'trans_fat': item.trans_fat,
                   'cholesterol': item.cholesterol,
                   'sodium': item.sodium,
                   'sugar': item.sugar,
                   'fiber': item.fiber,
                   'oz': item.oz,
                   'price': item.price,
                   'calories_from_fat': item.calories_from_fat,
                   'calories_from_protein': item.calories_from_protein,
                   'calories_from_carbs': item.calories_from_carbs,
                   'protein_efficiency': item.protein_efficiency,
                   'fat_efficiency': item.fat_efficiency,
                   'carbs_efficiency': item.carbs_efficiency,
                   'price_efficiency': item.price_efficiency,
                   'sodium_ratio': item.sodium_ratio,
                   'cholesterol_ratio': item.cholesterol_ratio,
                   'sugar_ratio': item.sugar_ratio,
                   'fiber_ratio': item.fiber_ratio,
                   'protein_per_dollar': item.protein_per_dollar,
                   'fat_per_dollar': item.fat_per_dollar,
                   'carbs_per_dollar': item.carbs_per_dollar,
                   'sugar_per_oz': item.sugar_per_oz})

# Create database if not already created
def create_table_with_price(table_name):
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                    name TEXT,
                    restaurant TEXT,
                    type_of_item TEXT,
                    calories INTEGER,
                    protein INTEGER,
                    carbs INTEGER,
                    fat INTEGER,
                    price REAL,

                    calories_from_fat INTEGER,
                    calories_from_protein INTEGER,
                    calories_from_carbs INTEGER,
                    protein_efficiency REAL,
                    fat_efficiency REAL,
                    carbs_efficiency REAL,
                    protein_per_dollar REAL,
                    far_per_dollar REAL,
                    carbs_per_dollar REAL,
                    price_efficiency REAL)''')

def insert_item_with_price(table_name, item, conn=conn, c=c):
    with conn:
        exists = get_item_by_name_and_restaurant(table_name=table_name, name=item.name, restaurant=item.restaurant, c=c)
        if exists:
            remove_item(table_name=table_name, name=item.name, restaurant=item.restaurant, conn=conn, c=c)

        c.execute(f'''INSERT INTO {table_name} VALUES (:name, 
                                                       :restaurant, 
                                                       :type_of_item, 
                                                       :calories, 
                                                       :protein, 
                                                       :carbs,
                                                       :fat,
                                                       :price,

                                                       :calories_from_fat,
                                                       :calories_from_protein,
                                                       :calories_from_carbs,
                                                       :protein_efficiency,
                                                       :fat_efficiency,
                                                       :carbs_efficiency,
                                                       :protein_per_dollar,
                                                       :fat_per_dollar,
                                                       :carbs_per_dollar,
                                                       :price_efficiency)''',
                  {'name': item.name,
                   'restaurant': item.restaurant,
                   'type_of_item': item.type_of_item,
                   'calories': item.calories,
                   'protein': item.protein,
                   'carbs': item.carbs,
                   'fat': item.fat,
                   'price': item.price,

                   'calories_from_fat': item.calories_from_fat,
                   'calories_from_protein': item.calories_from_protein,
                   'calories_from_carbs': item.calories_from_carbs,
                   'protein_efficiency': item.protein_efficiency,
                   'fat_efficiency': item.fat_efficiency,
                   'carbs_efficiency': item.carbs_efficiency,
                   'protein_per_dollar': item.protein_per_dollar,
                   'fat_per_dollar': item.fat_per_dollar,
                   'carbs_per_dollar': item.carbs_per_dollar,
                   'price_efficiency': item.price_efficiency})

# Create database if not already created
def create_table_without_price(table_name):
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                    name TEXT,
                    restaurant TEXT,
                    type_of_item TEXT,
                    calories INTEGER,
                    protein INTEGER,
                    carbs INTEGER,
                    fat INTEGER,

                    calories_from_fat INTEGER,
                    calories_from_protein INTEGER,
                    calories_from_carbs INTEGER,
                    protein_efficiency REAL,
                    fat_efficiency REAL,
                    carbs_efficiency REAL)''')

def insert_item_without_price(table_name, item, conn=conn, c=c):
    with conn:
        exists = get_item_by_name_and_restaurant(table_name=table_name, name=item.name, restaurant=item.restaurant, c=c)
        if exists:
            remove_item(table_name=table_name, name=item.name, restaurant=item.restaurant, conn=conn, c=c)

        c.execute(f'''INSERT INTO {table_name} VALUES (:name, 
                                                       :restaurant, 
                                                       :type_of_item, 
                                                       :calories, 
                                                       :protein, 
                                                       :carbs,
                                                       :fat,

                                                       :calories_from_fat,
                                                       :calories_from_protein,
                                                       :calories_from_carbs,
                                                       :protein_efficiency,
                                                       :fat_efficiency,
                                                       :carbs_efficiency)''',
                  {'name': item.name,
                   'restaurant': item.restaurant,
                   'type_of_item': item.type_of_item,
                   'calories': item.calories,
                   'protein': item.protein,
                   'carbs': item.carbs,
                   'fat': item.fat,

                   'calories_from_fat': item.calories_from_fat,
                   'calories_from_protein': item.calories_from_protein,
                   'calories_from_carbs': item.calories_from_carbs,
                   'protein_efficiency': item.protein_efficiency,
                   'fat_efficiency': item.fat_efficiency,
                   'carbs_efficiency': item.carbs_efficiency})

def get_item_by_name_and_restaurant(table_name, name, restaurant, c=c):
    c.execute(f'SELECT * FROM {table_name} WHERE name =:name AND restaurant=:restaurant', {'name': name,
                                                                                           'restaurant': restaurant})
    return c.fetchone()


def get_items_by_name(table_name, name, c=c):
    c.execute(f'SELECT * FROM {table_name} WHERE name =:name', {'name': name})
    return c.fetchall()


def get_items_from_restaurant(table_name, restaurant, c=c):
    c.execute(f'SELECT * FROM {table_name} WHERE restaurant =:restaurant', {'restaurant': restaurant})
    return c.fetchall()

def get_items_by_type(table_name, type_of_item, c=c):
    c.execute(f'SELECT * FROM {table_name} WHERE type_of_item =:type_of_item', {'type_of_item': type_of_item})
    return c.fetchall()

def update_attribute(table_name, name, restaurant, attribute_type, attribute_value, conn=conn, c=c):
    with conn:
        c.execute(f'''UPDATE {table_name} SET {attribute_type} = :attribute
                    WHERE name = :name AND restaurant = :restaurant''',
                  {'name': name,
                   'restaurant': restaurant,
                   'attribute': attribute_value})


def remove_item(table_name, name, restaurant, conn=conn, c=c):
    with conn:
        c.execute(f'DELETE from {table_name} WHERE name = :name AND restaurant= :restaurant',
                  {'name': name,
                   'restaurant': restaurant})


def close_database_connection(conn=conn):
    conn.close()


def close_cursor_connection(c=c):
    c.close()


#create_table("Food_Items")