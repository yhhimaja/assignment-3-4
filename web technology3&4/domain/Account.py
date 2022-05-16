'''
Create an Account class that mimics the account table
'''

import typing as t
from unicodedata import decimal

class Account():
    def __init__(self, investor_id: int, balance: float, id: int = -1):
        self.id = id
        self.investor_id = investor_id
        self.balance = balance

    def __str__(self): 
        return f'[id: {self.id}, investor_id: {self.investor.id}, balance: {self.balance}]'
    @staticmethod
    def from_dict(dict):
        if dict.get('investor_id') is None or dict.get('balance') is None:
            raise Exception(f'Can not create Account object from dict {dict}: missing required attributes')
        else:
            return Account(dict.get('investor_id'), dict.get('balance'))