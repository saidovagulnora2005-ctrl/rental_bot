from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

async def get_connection():
    try:
        conn = await asyncpg.connect(
            host = "localhost",
            user = "postgres",
            database = "rental_db",
            password = os.getenv("SQL_PASSWORD"),
            port = 5432
        )
        return conn
    except Exception as error:
        print("Connection error: ",error)
    

async def init_table():
    conn = await get_connection()
    try:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS items(
            item_id serial primary key,
            name varchar(50),
            is_rented boolean default false
        );
        CREATE TABLE IF NOT EXISTS rentals(
            rental_id serial primary key,
            telegram_id varchar,  
            item_id int references items(item_id),
            rented_at timestamp default now(),
            due_date timestamp default now(),
            returned_at timestamp,
            late_fee int default 0
        );
    """)
        print("Tables created successfully!")
    except Exception as error:
        print("Error in creating tables: ",error)
    finally:
        await conn.close()