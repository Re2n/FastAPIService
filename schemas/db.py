import databases

sql_url = f'postgresql://admin:admin@localhost:5431/production'

database = databases.Database(sql_url)
