# 1/14/22 avh - ds stands for data_service
import sqlite3
import modules.data_service.data_service_core as data_service_core


def get_row_by_user(user_id):
    """
    Select user_game_data by user
    :param user_id:
    :return: the user_game_data row
    """
    conn = data_service_core.get_connection()
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM user_game_data WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    return row


def update_credit(user_id, credit):
    """
    update credit
    :param user_id:
    :param credit:
    """
    sql = ''' UPDATE user_game_data
              SET credit = ?
              WHERE user_id = ?'''
    conn = data_service_core.get_connection()
    cur = conn.cursor()
    cur.execute(sql, (credit, user_id))
    conn.commit()

# 1/14/22 evh - updates the inventory numbers into the database


def update_inventory(user_id, inventory_r, inventory_c, inventory_y, inventory_g):
    """
    update inventory
    :param user_id:
    :param inventory_r:
    :param inventory_c:
    :param inventory_y:
    :param inventory_g:
    """
    sql = ''' UPDATE user_game_data
              SET inventory_r = ?,
              inventory_c = ?,
              inventory_y = ?,
              inventory_g = ?
              WHERE user_id = ?'''
    conn = data_service_core.get_connection()
    cur = conn.cursor()
    cur.execute(sql, (inventory_r, inventory_c, inventory_y, inventory_g, user_id))
    conn.commit()
