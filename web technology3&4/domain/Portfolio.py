'''
Create a Portfolio class that mimics the portfolio object
'''
import typing as t

class Portfolio():
    def __init__(self, account_id: int, ticker: str, quantity: int, id: int = -1):
        self.id = id
        self.account_id = account_id
        self.ticker = ticker
        self.quantity = quantity
        

    def __str__(self): 
        return f'[id: {self.id}, account_id: {self.account_id}, ticker: {self.ticker}, quantity: {self.quantity}]'

    @staticmethod
    def from_dict(dict):
        if dict.get('account_id') is None or dict.get('ticker') is None or dict.get('quantity') is None: # all required attributes
            raise Exception(f'Can not create Portfolio object from dict {dict}: missing required attributes')
        else:
            return Portfolio(dict.get('account_id'), dict.get('ticker'), dict.get('quantity'))