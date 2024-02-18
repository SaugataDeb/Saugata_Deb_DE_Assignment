import sqlite3
import pandas as pd

def connect_to_database():
    return sqlite3.connect("/Users/saugatadeb/Desktop/Saugata_DE_Assignment/de_assignment.db")  # Replace with your database name

def de_assignment_sql_solution(connection):
    query = """
    SELECT c.customer_id, c.age, i.item_name, COALESCE(SUM(o.quantity), 0) AS total_quantity
    FROM customers c
    LEFT JOIN sales s ON c.customer_id = s.customer_id
    LEFT JOIN orders o ON s.sales_id = o.sales_id
    LEFT JOIN items i ON o.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35
    GROUP BY c.customer_id, c.age, i.item_name
    HAVING total_quantity > 0
    """

    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def de_assignment_pandas_solution(connection):
    customers_df = pd.read_sql_query("SELECT * FROM customers;", connection)
    sales_df = pd.read_sql_query("SELECT * FROM sales;", connection)
    items_df = pd.read_sql_query("SELECT * FROM items;", connection)
    orders_df = pd.read_sql_query("SELECT * FROM orders;", connection)

    merged_df = pd.merge(customers_df, sales_df, on='customer_id')
    merged_df = pd.merge(merged_df, orders_df, on='sales_id')
    merged_df = pd.merge(merged_df, items_df, on='item_id')

    filtered_df = merged_df[(merged_df['age'] >= 18) & (merged_df['age'] <= 35) & (merged_df['quantity'] > 0)]
    return filtered_df.groupby(['customer_id', 'age', 'item_name'], as_index=False).agg({'quantity': 'sum'})

def save_to_csv(data, filename):
    data.to_csv(filename, sep=';', index=False)

def main():
    connection = connect_to_database()

    
    sql_result = de_assignment_sql_solution(connection)
    save_to_csv(pd.DataFrame(sql_result, columns=['Customer', 'Age', 'Item', 'Quantity']), 'saugata_deb_sql_output.csv')

    
    pandas_result = de_assignment_pandas_solution(connection)
    save_to_csv(pandas_result, 'saugata_de_assignment.csv')

    connection.close()

if __name__ == "__main__":
    main()
