import pandas as pd
customers_data = {
    'customers_id':[10,20,30,40],
    'name':['ABC','PQR','LMN','XYZ'],
    'city':['Mumbai','Tokyo','Frankfrut','Johannesberg']    
}
customers_df = pd.DataFrame(customers_data)
orders_data ={
    'order_id':[101,102,103,104],
    'customers_id':[10,20,30,40],
    'amount':[450.0,320.5,101.99,500.0]   
}
orders_df = pd.DataFrame(orders_data)
print("Customer Dataframe: ")
print(customers_data)
print("Order Dataframe: ")
print(orders_df)
inner_join = pd.merge(customers_df, orders_df, on='customers_id',how='inner')
print("------INNER JOIN------")
print(inner_join)
left_join = pd.merge(customers_df, orders_df, on='customers_id',how='left')
print("------LEFT JOIN------")
print(left_join)
right_join = pd.merge(customers_df, orders_df, on='customers_id',how='right')
print("------RIGHT JOIN-----")
print(right_join)
outer_join = pd.merge(customers_df, orders_df, on='customers_id',how='outer')
print("------OUTER JOIN------")
print(outer_join)
**
