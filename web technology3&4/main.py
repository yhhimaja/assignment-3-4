import app.src.dao.portfolio_dao as pd
import app.src.dao.sql as sql
from app.src.dao.account_dao import del_account
from app.src.dao.account_dao import update_account_balance
from app.src.dao.account_dao import create_account
from app.src.dao.account_dao import get_account_by_id
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio

def main():
    d_Investment = Portfolio('2','DDD','66') #qty is required
    pd.del_investment(d_Investment)

#def main():
#    update_investment = Portfolio('222','BBB',2)
#    pd.update_quant(update_investment)

#def main():
#    new_invest = Portfolio('2','DDD','66')
#    pd.add_investment(new_invest)

#def main():
#    ticker = pd.get_portfolio_by_ticker('AAA')
#    print(ticker)

#def main():
#    account = pd.get_portfolio_by_id(1)
#    print(account)

#def main():
#    d_Account = Account(8,8) #Also Requires Balance
#    del_account(d_Account)

#def main():
#    update_Account = Account('5500','2')
#    update_account_balance(update_Account)

#def main():
#    new_Account = Account('7','8','9')
#    create_account(new_Account)

#def main():
#    account = get_account_by_id(2)
#    print(account)

if __name__ == '__main__':
    main()