'''
Create CRUD functions for the account data table. Example: get_account_by_id
'''
'''
Create CRUD functions for the account data table. Example: get_account_by_id
'''
import typing as t
from mysql.connector import MySQLConnection
from .dbutils import get_db_cnx
from app.src.domain.Account import Account
import app.src.dao.sql as sql


def get_account_by_id(id: int) -> t.Optional[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.account_by_id, (id,))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return Account(rs['investor_id'], rs['balance'],rs['id'])
    except Exception as e:
        print(f'Unable to retrieve account by Id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_account_by_investor_id(id: int) -> t.List[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_account_by_investor_id_sql, (id, ))
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            account = []
            for row in rs:
                account.append(account(row['investor_id'], row['balance'],row['id']))
        return account
    except Exception as e:
        print(f'Unable to retrieve account named {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_all_accounts() -> t.List[Account]: # will be the empty list if no accounts are created in the database
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True) 
        cursor.execute(sql.get_all_accounts_sql)
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            accounts = []
            for row in rs:
                accounts.append(Account(row.get('investor_id'), row.get('balance'), row.get('id')))
            return accounts
    except Exception as e:
        print(f'An exception occurred while trying to get a list of all accounts: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close() # to prevent any memory leaks

def create_account(account: Account) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.create_account, (account.investor_id, account.balance,))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create a new account: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def update_account_investor_id(id: int, investor_id: str) -> None:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_account_investor_id, (investor_id, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update account investor_id: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()

def update_account_balance(id: int, balance: str) -> t.Optional[Account]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.update_account_balance, (balance, id))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to update account balance: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close()
