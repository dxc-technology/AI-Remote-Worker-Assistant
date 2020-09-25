#import flask
#import requests
import os
import json
import ast

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def home():
    #return render_template('index.html', svc='http://127.0.0.1:1000/')
    return render_template('index.html')

@app.route('/optimize')
def optimize():
    import pulp
    from pulp import LpVariable,LpProblem,LpStatus,LpMaximize,LpMinimize
    # Step 2 : Define the problem : Maximize the savings
    budget_2 = LpProblem("Monthly_Savings",LpMaximize)
    # Given monthly income 
    income = 8000
    # Minimum limit for each category
    monthly_min_home_utility = 10.0
    monthly_min_transportation = 10.0
    monthly_min_shopping_groceries = 10.0
    monthly_min_personal_family_care = 10.0
    monthly_min_restaurant_dinning = 10.0
    monthly_min_insurance = 10.0
    monthly_min_entertainment = 10.0
    monthly_min_travel = 10.0
    monthly_min_health = 10.0
    monthly_min_maintenance = 10.0
    # Maximum limit for each category
    mmonthly_home_utility = 500.0
    mmonthly_transportation = 120.0
    mmonthly_shopping_groceries = 200.0
    mmonthly_personal_family_care = 50.0
    mmonthly_restaurant_dinning = 200.0
    mmonthly_insurance = 500.0
    mmonthly_entertainment = 330.0
    mmonthly_travel = 250.0
    mmonthly_health = 200.0
    mmonthly_maintenance = 110.0
    # Actual expense for each category
    monthly_home_utility_spend = 460.0
    monthly_transportation_spend = 110.0
    monthly_shopping_groceries_spend = 100.0
    monthly_personal_family_care_spend = 35.0
    monthly_restaurant_dinning_spend = 140.0
    monthly_insurance_spend = 420.0
    monthly_entertainment_spend = 100.0
    monthly_travel_spend = 210.0
    monthly_health_spend = 70.0
    monthly_maintenance_spend = 100.0
    # will continue
    _input = request.args['input']
    
    return _input

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
    
    #import os
   # HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
       # PORT = int(os.environ.get('SERVER_PORT', '1000'))
   # except ValueError:
       # PORT = 1000
   # app.run(HOST, PORT)
    
'''if __name__ == '__main__':
    app.run(debug=True, port=1000)'''
