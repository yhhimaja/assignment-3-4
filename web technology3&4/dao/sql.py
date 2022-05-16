# Investor SQL statements
investor_by_id = 'select name, address, status, id from investor where id = %s'
get_investors_by_name_sql = 'select name, address, status, id from investor where name = %s'
create_investor = 'insert into investor (name, address, status) values (%s, %s, %s)'
update_investor_name = 'update investor set name = %s where id = %s'
update_investor_address = 'update investor set address = %s where id = %s'
get_investor_by_id_sql = 'select id, name, address, status from investor where id=%s'
update_investor_status = 'update investor set status = %s where id = %s'
get_all_investors_sql = 'select id, name, address, status from investor'
delete_investor_by_id = 'delete from investor where id = %s'
get_investor_count = 'select count(*) as cnt from investor'
get_active_investor_count = 'select count(*) as cnt from investor where status = "Active"'


#Account SQL Statements
account_by_id = 'SELECT investor_id, balance, id FROM account WHERE id = %s'
get_account_by_investor_id_sql = 'SELECT investor_id, balance, id FROM account WHERE investor_id = %s'
create_accoount = 'INSERT into account (investor_id, balance) VALUES (%s, %s)'
update_account_investor_id = 'UPDATE account set investor_id = %s WHERE id = %s'
update_account_balance = 'UPDATE account set balance = %s WHERE id = %s'
Delete_account_id = 'DELETE FROM account WHERE id= %s'
get_all_accounts_sql = 'select id, investor_id, balance from account'


#Portfolio SQL Statements
portfolio_by_id = 'select account_id, ticker, quantity from portfolio where account_id = %s'
update_quantity = 'update portfolio set quantity = %s where ticker = %s and account_id = %s'
delete_investment = 'DELETE from portfolio where account_id = %s and ticker = %s and quantity = %s'
get_all_Portfolios_sql = 'select account_id, ticker, quantity from portfolio'
investment_by_ticker = 'select account_id, ticker, quantity from portfolio where ticker = %s'
add_to_portfolio = 'insert into portfolio (account_id, ticker, quantity) values (%s, %s, %s)'