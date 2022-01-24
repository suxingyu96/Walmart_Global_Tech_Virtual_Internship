import pandas as pd

# a = pd.read_csv("/Users/suxingyu/Downloads/forage-walmart-task-4-main/data/shipping_data_1.csv")
# b = pd.read_csv("/Users/suxingyu/Downloads/forage-walmart-task-4-main/data/shipping_data_2.csv")

# merged = a.merge(b, on='shipment_identifier')
# merged.to_csv("output.csv", index=False)

# pd.DataFrame("output.csv").groupby(['shipment_identifier','product']).sum().reset_index()

df=pd.read_csv("/Users/suxingyu/Downloads/forage-walmart-task-4-main/output.csv")
# df.groupby(['shipment_identifier','product']).sum().reset_index()
# df['product_quantity'] = df.groupby(['shipment_identifier', 'product'])['tmp'].transform('sum')
# new_df=df.drop_duplicates(subset=['shipment_identifier', 'product'])
df.drop_duplicates(subset=['shipment_identifier', 'product'])
df.to_csv("output.csv", index=False)