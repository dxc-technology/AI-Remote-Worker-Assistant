#import flask
from flask import request
import os
import json
import ast
import pulp
from flask_cors import CORS
from pulp import LpVariable,LpProblem,LpStatus,LpMaximize,LpMinimize
    

from flask import Flask, render_template, request, redirect, url_for,jsonify
app = Flask(__name__)

app.secret_key='N@twestkey1_2907!'
cors = CORS(app)
authenticated = False

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

@app.route('/optimize', methods=['GET', 'POST'])
def optimize():
    # Step 2 : Define the problem : Maximize the savings
    budget_2 = LpProblem("Monthly_Savings",LpMaximize)
    # Given monthly income 
    income = 8000
    # Minimum limit for each category
    monthly_min_home_utility = 10.0
    # Console.Log(monthly_min_home_utility)
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
    #_input = request.args['input']
#     monthly_home_utility_spend = 460.0
#     monthly_transportation_spend = 110.0
#     monthly_shopping_groceries_spend = 100.0
#     monthly_personal_family_care_spend = 35.0
#     monthly_restaurant_dinning_spend = 140.0
#     monthly_insurance_spend = 420.0
#     monthly_entertainment_spend = 100.0
#     monthly_travel_spend = 210.0
#     monthly_health_spend = 70.0
#     monthly_maintenance_spend = 100.0
    
    monthly_home_utility_spend = float(request.args['monthly_home_utility_spend'])
    monthly_transportation_spend = float(request.args['monthly_transportation_spend'])
    monthly_shopping_groceries_spend =float(request.args['monthly_shopping_groceries_spend'])
    monthly_personal_family_care_spend = float(request.args['monthly_personal_family_care_spend'])
    monthly_restaurant_dinning_spend = float(request.args['monthly_restaurant_dinning_spend'])
    monthly_insurance_spend = float(request.args['monthly_insurance_spend'])
    monthly_entertainment_spend = float(request.args['monthly_entertainment_spend'])
    monthly_travel_spend = float(request.args['monthly_travel_spend'])
    monthly_health_spend = float(request.args['monthly_health_spend'])
    monthly_maintenance_spend = float(request.args['monthly_maintenance_spend'])
    # Define the decision variables
    home_utility_perct_adjustment = LpVariable("Home_Utilities",0,0.2)
    transportation_perct_adjustment = LpVariable("Transportation",0,0.20)
    shopping_groceries_perct_adjustment = LpVariable("Shopping_Groceries",0,0.20)
    personal_family_care_perct_adjustment = LpVariable("Personal_Family_Care",0,0.20)
    restaurant_dinning_perct_adjustment = LpVariable("Restaurant_Dining",0,0.20)
    insurance_perct_adjustment = LpVariable("Insurance",0,0.20)
    entertainment_perct_adjustment = LpVariable("Entertainment",0,0.20)
    travel_perct_adjustment = LpVariable("Travel",0,0.20)
    health_perct_adjustment = LpVariable("Health",0,0.20)
    maintenance_perct_adjustment = LpVariable("Maintenance",0,0.20)
    savings = LpVariable("Savings")
    budget_2 += savings
    # compute the minimum percent on the actuals 
    mthly_home_utility_der = monthly_home_utility_spend * (1 - home_utility_perct_adjustment)
    mthly_transportation_der = monthly_transportation_spend * (1 - transportation_perct_adjustment)
    mthly_shopping_groceries_der = monthly_shopping_groceries_spend * (1 - shopping_groceries_perct_adjustment)
    mthly_personal_family_care_der = monthly_personal_family_care_spend * (1 - personal_family_care_perct_adjustment)
    mthly_restaurant_dinning_der = monthly_restaurant_dinning_spend * (1 - restaurant_dinning_perct_adjustment)
    mthly_insurance_der = monthly_insurance_spend * (1 - insurance_perct_adjustment)
    mthly_entertainment_der = monthly_entertainment_spend * (1 - entertainment_perct_adjustment)
    mthly_travel_der = monthly_travel_spend * (1 - travel_perct_adjustment)
    mthly_health_der = monthly_health_spend * (1 - health_perct_adjustment)
    mthly_maintenance_der = monthly_maintenance_spend * (1 - maintenance_perct_adjustment)
    # Adjustment for each category can go beyond the minimum of each category
    budget_2 += mthly_home_utility_der >= monthly_min_home_utility
    budget_2 += mthly_transportation_der >= monthly_min_transportation
    budget_2 += mthly_shopping_groceries_der  >= monthly_min_shopping_groceries
    budget_2 += mthly_personal_family_care_der >= monthly_min_personal_family_care
    budget_2 += mthly_restaurant_dinning_der >= monthly_min_restaurant_dinning
    budget_2 += mthly_insurance_der >= monthly_min_insurance
    budget_2 += mthly_entertainment_der >= monthly_min_entertainment
    budget_2 += mthly_travel_der  >= monthly_min_travel
    budget_2 += mthly_health_der >= monthly_min_health
    budget_2 += mthly_maintenance_der >=monthly_min_maintenance
    # Adjustment for each category should not go beyond the maximum of each category
    budget_2 += mthly_home_utility_der <= mmonthly_home_utility
    budget_2 += mthly_transportation_der <= mmonthly_transportation
    budget_2 += mthly_shopping_groceries_der  <= mmonthly_shopping_groceries
    budget_2 += mthly_personal_family_care_der <= mmonthly_personal_family_care
    budget_2 += mthly_restaurant_dinning_der <= mmonthly_restaurant_dinning
    budget_2 += mthly_insurance_der <= mmonthly_insurance
    budget_2 += mthly_entertainment_der <= mmonthly_entertainment
    budget_2 += mthly_travel_der  <= mmonthly_travel
    budget_2 += mthly_health_der <= mmonthly_health
    budget_2 += mthly_maintenance_der <=mmonthly_maintenance
    # sum of monthly expenses times the adjustment should be within the income
    budget_2 += mthly_home_utility_der + mthly_transportation_der + mthly_shopping_groceries_der + mthly_personal_family_care_der+ mthly_restaurant_dinning_der + mthly_insurance_der + mthly_entertainment_der + mthly_travel_der +mthly_health_der + mthly_maintenance_der + savings <= income
    # solve the problem
    status = budget_2.solve(pulp.PULP_CBC_CMD(keepFiles=True))
    #LpStatus[status]
    # Display values of the variables 
    minimized_home_utility = monthly_home_utility_spend * (1 - pulp.value(home_utility_perct_adjustment))
    minimized_transportation = monthly_transportation_spend * (1 - pulp.value(transportation_perct_adjustment))
    minimized_shopping_groceries = monthly_shopping_groceries_spend * ( 1 - pulp.value(shopping_groceries_perct_adjustment))
    minimized_personal_family_care = monthly_personal_family_care_spend * ( 1 - pulp.value(personal_family_care_perct_adjustment))
    minimized_restaurant_dinning = monthly_restaurant_dinning_spend * (1 - pulp.value(restaurant_dinning_perct_adjustment))
    minimized_insurance = monthly_insurance_spend * (1 - pulp.value(insurance_perct_adjustment))
    minimized_entertainment = monthly_entertainment_spend * ( 1 - pulp.value(entertainment_perct_adjustment))
    minimized_travel = monthly_travel_spend * ( 1 - pulp.value(travel_perct_adjustment))
    minimized_health = monthly_health_spend * ( 1 - pulp.value(health_perct_adjustment))
    minimized_maintenance = monthly_maintenance_spend  * ( 1 - pulp.value(maintenance_perct_adjustment))
    r = {
        "minimized_home_utility": minimized_home_utility,
        "minimized_transportation": minimized_transportation,
        "minimized_shopping_groceries": minimized_shopping_groceries,
        "minimized_personal_family_care": minimized_personal_family_care,
        "minimized_restaurant_dinning": minimized_restaurant_dinning,
        "minimized_insurance": minimized_insurance,
        "minimized_entertainment": minimized_entertainment,
        "minimized_travel": minimized_travel,
        "minimized_health": minimized_health,
        "minimized_maintenance": minimized_maintenance,
    }
    #return _input
    #json = dumps(r)
    #return json
    return jsonify(r)

   
if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
    
    # import os
    # HOST = os.environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(os.environ.get('SERVER_PORT', '1000'))
    # except ValueError:
    #     PORT = 1000
    # app.run(HOST, PORT, debug=True)

    
'''if __name__ == '__main__':
    app.run(debug=True, port=1000)'''
