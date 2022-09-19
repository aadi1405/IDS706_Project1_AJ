from databricks import sql
import os

def querydb(query= "SELECT * FROM hive_metastore.default.netflix_titles"):
    with sql.connect (
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result


def query_year(_c2):
    
    query = f"SELECT _c7 FROM hive_metastore.default.netflix_titles WHERE _c2= '{_c2}';"

    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
        for row in result:
            print(row)

def query_desc(name):
    
    query = f"SELECT _c11 FROM hive_metastore.default.netflix_titles WHERE _c2= '{name}'; "

    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
        for row in result:
            print(row)

def query_age(age):
    if age<21:
        print(" Only movies and shows for under 21 year olds is allowed, here is a list")
        query = "SELECT _c2 FROM hive_metastore.default.netflix_titles WHERE _c8= 'PG-14' or _c8='PG-13'; "
    else:
        print("Any movie is allowed as you are old enough, here is a list")
        query = "SELECT _c2 FROM hive_metastore.default.netflix_titles; "

    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
        for row in result:
            print(row)

def query_director(director):
    query = f"SELECT _c2 FROM hive_metastore.default.netflix_titles WHERE _c3 LIKE '%{director}%'; "
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
        for row in result:
            print(row)
            
    return result