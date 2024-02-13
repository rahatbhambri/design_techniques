import mysql
import mysql.connector
from mysql.connector import pooling
import asyncio 
import aiomysql 



async def execute_query_async(pool, query, params=None):
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchall()
            #print(query, " done ", result)
            return result
    
    

async def main():
    # Create a connection pool
    pool = await aiomysql.create_pool(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        db='sys',
        minsize=1,
        maxsize=10
    )

    # Example query
    query1 = " \
    SELECT Row_id FROM store \
    where Row_id < 50 \
    FOR UPDATE \
    "
    query2 = " \
    SELECT Row_id FROM store \
    where Row_id < 50 \
    FOR UPDATE skip locked \
    "
    query3 = " \
    SELECT Row_id FROM store \
    where Row_id < 50 \
    FOR UPDATE skip locked \
    "
    query4 = " \
    SELECT Row_id FROM store \
    where Row_id < 50 \
    FOR UPDATE skip locked \
    "
    query5 = " \
    SELECT Row_id FROM store \
    where Row_id < 50 \
    FOR UPDATE skip locked \
    "

    query6 = " \
    SELECT Row_id FROM store \
    where Row_id < 100 \
    FOR UPDATE skip locked \
    "

    queries = [
    query1, query2, query3, query4, query5, query6
    ]
    
    tasks = [execute_query_async(pool, query) for query in queries]
    results = await asyncio.gather(*tasks)

    # Print results
    for query_result in results:
        print(query_result)
    
    # Close the connection pool
    pool.close()
    await pool.wait_closed()

# Run the asyncio event loop
asyncio.run(main())