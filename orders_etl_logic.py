import pandas as pd
import sqlalchemy
orders_table = 'C:\Users\gabri\OneDrive\Documents\Portfolio Projects\ETL_Python_SQL\H+ Sport orders.xlsx'
engine = db.create_enginge('postgresql://postgres:zN1bX8vd13Y5SgIK@nasally-balanced-earwig.data-1.use1.tembo.io:5432/postgres')

def main():
    orders = pd.read_excel(orders_table, sheet_name='data')

    orders = orders[["OrderID", "Date", "TotalDue", "Status", "CustomerID", "SalespersonID"]]

    orders.to_sql('orders', engine,
                  if_exists='replace',
                  index=False)
    
    print("ETL script executed successfully")