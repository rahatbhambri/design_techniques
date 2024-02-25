import pymysql
from pymongo import MongoClient
import time
import pymysqlpool

# MySQL connection settings
mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_user = 'root'
mysql_password = ''
mysql_db = 'sys'
mysql_table = 'cdc_tracking'
# Create a connection pool
pool = pymysqlpool.ConnectionPool(host=mysql_host, port=mysql_port, user=mysql_user,
                      password=mysql_password, database=mysql_db, name="mypool", 
                      size=5, autocommit = True)  # Adjust pool_size as needed


# MongoDB connection settings
mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'config'
mongo_collection = 'cdc'


# Connect to MongoDB
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db]
mongo_coll = mongo_db[mongo_collection]

# Function to capture changes from MySQL and write to MongoDB
def capture_and_write_changes():
    # Execute query to select new changes from MySQL
    connection = pool.get_connection()
    mysql_cursor = connection.cursor()

    mysql_cursor.execute(f"SELECT * FROM {mysql_table} WHERE status = 'new';")
    new_changes = mysql_cursor.fetchall()
    
    # Transform data if necessary
    transformed_data = []
    for change in new_changes:
        # Example transformation: Convert to dictionary
        transformed_data.append({
            'id': change[0],
            'name': change[1],
            'description': change[2]
            # Add more fields as needed
        })
    
    # Write transformed data to MongoDB
    if len(transformed_data) > 0:
        
        #print("added data", transformed_data)
        mongo_coll.insert_many(transformed_data)
    
        # Update status in MySQL to mark changes as processed
        ids = [change[0] for change in new_changes]
        mysql_cursor.executemany("UPDATE {} SET status = 'processed' WHERE id = %s".format(mysql_table), ids)
        #mysql_conn.commit()

# Main loop to continuously capture and write changes
while True:
    capture_and_write_changes()
    time.sleep(2)
    # Add delay or use triggers/events to capture changes more efficiently
