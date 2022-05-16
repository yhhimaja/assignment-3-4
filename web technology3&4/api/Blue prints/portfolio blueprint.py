# create portfolio blueprint
from http import HTTPStatus
import json
from flask import Blueprint, make_response, request
import app.src.dao.portfolio_dao as portfoliodao
from app.src.domain.Portfolio import Portfolio

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolio') 
@portfolio_bp.route('/', methods=['GET'])
def default():
    res = make_response()
    res.response=  'OK'
    return res

@portfolio_bp.route('/get-all-Portfolios', methods=['GET'])
def get_all():
    try:
        portfolios = portfoliodao.get_all_Portfolios()
        res = make_response()
        res.response = json.dumps([portfolio.__dict__ for portfolio in portfolios])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting all portfolios: {str(e)}'
        return error_res

@portfolio_bp.route('/get-portfolio-by-id/<account_id>', methods=['GET'])
def get_portfolio_by_id(account_id):
    try:
        portfolios = portfoliodao.get_portfolio_by_id(account_id)
        res = make_response()
        res.response = json.dumps([portfolio.__dict__ for portfolio in portfolios])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting portfolio with id {account_id}: {str(e)}'
        return error_res

@portfolio_bp.route('/get-portfolio-by-ticker/<ticker>', methods=['GET'])
def get_portfolio_by_ticker(ticker):
    try:
        portfolios = portfoliodao.get_portfolio_by_ticker(ticker)
        res = make_response()
        res.response = json.dumps([portfolio.__dict__ for portfolio in portfolios])
        res.headers['Content-Type'] = 'application/json'
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR # status 500
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while getting portfolio with ticker {ticker}: {str(e)}'
        return error_res
      
@portfolio_bp.route('/create', methods=['POST'])
def add_investment():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type is None or content_type != 'application/json':
            return ('Expected application/json content-type', HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            data = request.json
            portfolio = Portfolio.from_dict(data)
            portfoliodao.add_investment(portfolio)
            res = make_response()
            res.status = HTTPStatus.OK
            return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR 
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while creating a new portfolio: {str(e)}'
        return error_res


@portfolio_bp.route('/delete-portfolio/<account_id>/<ticker>/<quantity>', methods = ['DELETE'])
def delete_portfolio(account_id,ticker,quantity):
    try:
        portfoliodao.del_investment(account_id,ticker,quantity)
        res = make_response()
        res.status = HTTPStatus.OK
        return res
    except Exception as e:
        error_res = make_response()
        error_res.status = HTTPStatus.INTERNAL_SERVER_ERROR 
        error_res.headers['Content-Type'] = 'plain/text'
        error_res.response = f'Error while deleteing portfolio (ID: {account_id}): {str(e)}'
        return error_res