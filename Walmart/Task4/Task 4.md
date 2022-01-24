Task 4

code in pythoon

```python
import pandas as pd
import sqlite3
con = sqlite3.connect('/Users/suxingyu/Downloads/forage-walmart-task-4-main/shipment_database.db')
cur = con.cursor()

df= pd.read_csv('/Users/suxingyu/Downloads/forage-walmart-task-4-main/output.csv')   

df.columns = df.columns.str.strip()

df.to_sql("MyTable", con)

af= pd.read_csv('/Users/suxingyu/Downloads/forage-walmart-task-4-main/data/shipping_data_0.csv')   

af.columns = af.columns.str.strip()

af.to_sql("MyTable", con, if_exists='append')

con.close()
```

