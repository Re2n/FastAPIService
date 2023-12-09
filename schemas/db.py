import databases

sql_url = f'postgresql://admin:admin@database:5432/production'

database = databases.Database(sql_url)
