from connection import get_connection


async def add_item(name):
    conn = await get_connection()
    try:
        await conn.execute("""
            INSERT INTO items(name) VALUES($1)
            """,name)
    except Exception as error:
        print("Add item error:", error)
    finally:
        await conn.close()


async def show_items():
    conn = await get_connection()
    try:
        items = await conn.fetch("""
            SELECT * FROM items where is_rented = false
            """)
    except Exception as error:
        print("Show items error:", error)
    finally:
        await conn.close()