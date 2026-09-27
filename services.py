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


async def rent(item_id, telegram_id):
    conn = await get_connection()
    try:
        item = await conn.fetchrow("""
            SELECT * from items where item_id = $1 and is_rented = FALSE
            """,item_id)
        await conn.execute("""
            INSERT INTO rentals(telegram_id, item_id) VALUES($1, $2)
            """,str(telegram_id),item_id)
        await conn.execute("""
            UPDATE items set is_rented = TRUE WHERE item_id = $1
            """,item_id)
    except Exception as error:
        print("Rent error:", error)
    finally:
        await conn.close()


async def return_item(item_id, telegram_id):
    conn = await get_connection()
    try:
        rental = await conn.fetchrow("""
            SELECT * from rentals where item_id = $1 and telegram_id = $2 and returned_at IS NULL
            """,item_id,str(telegram_id))
        await conn.execute("""
            UPDATE rentals set returned_at = NOW() where rental_id = $1
            """,rental["rental_id"])
        await conn.execute("""
            UPDATE items set is_rented = FALSE where item_id = $1
            """,item_id)
    except Exception as error:
        print("Return item error:", error)
    finally:
        await conn.close()

async def my_rentals(telegram_id):
    conn = await get_connection()
    try:
        rentals = await conn.fetch("""
            SELECT rentals.item_id, items.name from rentals JOIN items ON rentals.item_id = items.item_id where rentals.telegram_id = $1
            and rentals.returned_at IS NULL
            """,str(telegram_id))
        return rentals
    except Exception as error:
        print("Error in my rentals:", error)
    finally:
        await conn.close()