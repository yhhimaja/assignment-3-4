from flask import Blueprint, render_template

from app.src.dao.investor_dao import get_all_investors, get_investor_count

ui_bp = Blueprint('ui',__name__, url_prefix='/ui')

@ui_bp.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@ui_bp.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@ui_bp.route('/investors', methods = ['GET'])
def investors():
    investor_count = get_investor_count(True)
    active_investor_count = get_investor_count (False)
    investors = get_all_investors()
    return render_template('investors.html', payload = {
        'investor_count': investor_count,
        'active_investor_count': active_investor_count,
        'investors': investors 
        })