from http import HTTPStatus
from flask import Flask, make_response, render_template

from app.src.api.blueprints.investor_bp import investor_bp
from app.src.api.blueprints.account_bp import account_bp
from app.src.api.blueprints.portfolio_bp import portfolio_bp

from app.src.api.blueprints.ui_bp import ui_bp

app = Flask(__name__) 

app.register_blueprint(investor_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(account_bp)
app.register_blueprint(ui_bp)



@app.route('/healthcheck', methods=['GET'])
def health_check():
    return render_template('healthcheck.html')

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port= 8080, debug=True)
