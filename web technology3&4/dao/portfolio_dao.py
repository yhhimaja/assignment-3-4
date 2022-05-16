'''
Create CRUD functions for the portfolio data table. Example: get_portfolio_by_id
'''
import typing as t
from mysql.connector import MySQLConnection
from .dbutils import get_db_cnx
from app.src.domain.Portfolio import portfolio
import app.src.dao.sql as sql


def get_portfolio_by_id(id: int) -> t.Optional[portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.portfolio_by_id, (id,))
        rs = cursor.fetchone()
        if rs is None:
            return None
        return portfolio(rs['account_id'], rs['ticker'], rs['quantity'],rs['id'])
    except Exception as e:
        print(f'Unable to retrieve portfolio by Id {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_all_Portfolios() -> t.List[Portfolio]:
    try:
        db_cnx: MySQLConnection = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.get_all_Portfolios_sql)
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            Portfolios = []
            for row in rs:
                Portfolios.append(Portfolio(row.get('account_id'), row.get('ticker'), row.get('quantity')))
            return Portfolios
    except Exception as e:
        print(f'An exception occurred while trying to get a list of all Portfolios: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def get_portfolio_by_ticker(ticker: str) -> t.Optional[Portfolio]:
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor(dictionary=True)
        cursor.execute(sql.investment_by_ticker, (ticker,))
        rs = cursor.fetchall()
        if len(rs) == 0:
            return []
        else:
            Portfolios = []
            for row in rs:
                Portfolios.append(Portfolio(row.get('account_id'), row.get('ticker'), row.get('quantity')))
            return Portfolios
    except Exception as e:

        print(f'An exception occurred while getting Portfolio with ticker {id}: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

def del_investment(account_id : int, ticker : str, quantity : int):
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.delete_investment, (account_id,ticker, quantity ))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to delete investment: {str(e)}')
    finally: 
        cursor.close()
        db_cnx.close() 

def add_investment(portfolio:Portfolio) -> None:
    try:
        db_cnx = get_db_cnx()
        cursor = db_cnx.cursor()
        cursor.execute(sql.add_to_portfolio, (portfolio.account_id, portfolio.ticker, portfolio.quantity))
        db_cnx.commit()
    except Exception as e:
        print(f'Unable to create new investment: {str(e)}')
    finally:
        cursor.close()
        db_cnx.close()

