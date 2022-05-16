import typing as t
from mysql.connector import MySQLConnection
from .dbutils import get_db_cnx
from app.src.domain.Investor import Investor
import app.src.dao.sql as sql


def get_investor_by_id(id: int) -> t.Optional[Investor]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.investor_by_id, (id,))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Investor(rs['name'], rs['address'], rs['status'], rs['id'])
    except Exception as e:
        print(f'Unable to retrieve investor by Id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_all_investors() -> t.List[Investor]: # if no investors are created empty list will be there in database
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True) # results will return as dict
        cursor.execute(sql.get_all_investors_sql)
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            investors = []
            for row in rs:
                investors.append(Investor(row.get('name'), row.get('address'), row.get('status'), row.get('id')))
            return investors
    except Exception as e:
        print(f'An exception occurred while trying to get a list of all investors: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_investors_by_name(name: str) -> t.List[Investor]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_investors_by_name_sql, (name, ))
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            investors = []
            for row in rs:
                investors.append(Investor(row['name'], row['address'], row['status'], row['id']))
        return investors
    except Exception as e:
        print(f'Unable to retrieve investors named {name}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def create_investor(investor: Investor) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_investor, (investor.name, investor.address, investor.status))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create a new investor: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def update_investor_name(id: int, name: str) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_investor_name, (name, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update investor name: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_investor_address(id: int, address: str) -> t.Optional[Investor]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_investor_name, (address, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update investor address: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_investor_status(id: int, status: str) -> None:
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_investor_status, (status, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update investor status: str(e)')
    finally:
        cursor.close()
        db_cnx.close()


def get_investor_count(include_inactive) -> int:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        if include_inactive:
            query = sql.get_investor_count 
        else:
            query = sql.get_active_investor_count
        cursor.execute(query)
        rs = cursor.fetchone()
        investor_count = rs['cnt']
        return investor_count
    except Exception as e:
        print(f'An exception occurred while trying to get a count of all investors: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close() 
        
def delete_investor_by_id(id: int) -> None: 
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.delete_investor_by_id, (id,))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to delete investor: str(e)')
    finally:
        cursor.close()
        db_cnx.close()

