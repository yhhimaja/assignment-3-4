# create account blueprint
# Create/Update/Delete/GET
# minimum endpoints:

from http import HTTPStatus
import json
from flask import Blueprint, make_response, request
import app.src.dao.account_dao as accountdao
from app.src.domain.Account import Account

account_bp = Blueprint('account', __name__, url_prefix='/account') 

@account_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res

@account_bp.route('/get-all-accounts', methods=['GET'])
def get_all():
    try:
        accounts = accountdao.get_all_accounts()
        res = make_response()
        res.response = json.dumps([account.__dict__ for account in accounts])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR 
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting all accounts: {str(e)}'
        return error_res

@account_bp.route('/get-account-by-id/<investor_id>', methods=['GET'])
def get_account_by_id(investor_id):
    try:
        account = accountdao.get_account_by_id(investor_id)
        res = make_response()
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        res.response = json.dumps(account.__dict__)
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR 
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting account with id {investor_id}: {str(e)}'
        return error_res
      
@account_bp.route('/create', methods=['POST'])
def create_account():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            account = Account.from_dict(data)
            accountdao.create_account(account)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR 
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new account: {str(e)}'
        return error_res

@account_bp.route('/update-balance/<investor_id>/<new_balance>', methods=['PUT'])
def update_account_balance(investor_id, new_balance):
    try:
        accountdao.update_account_balance(investor_id, new_balance)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while updating account (investor_id: {investor_id}) balance: {str(e)}'
        return error_res

@account_bp.route('/delete-account/<investor_id>', methods = ['DELETE'])
def delete_account(investor_id):
    try:
        accountdao.del_account(investor_id)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR 
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing account (ID: {investor_id}) address: {str(e)}'
        return error_res