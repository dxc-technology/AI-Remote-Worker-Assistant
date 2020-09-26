#import flask
from flask import request
import os
import json
import ast
import pulp
from flask_cors import CORS
from pulp import LpVariable,LpProblem,LpStatus,LpMaximize,LpMinimize, value, lpSum
import ast


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
    # define the limits of a reasonable adjustment
    no_adjustment = 0
    hardship = .15

    monthly_income = float(request.args['income'])
    spending_categories = ast.literal_eval(request.args['categories'])
    spending = ast.literal_eval(request.args['spending'])
    spending_minimum = ast.literal_eval(request.args['min'])

    # create adjustment factor variables for each spending category
    adjustment_factor_variable = {}
    for category in spending_categories:
        variable = LpVariable(category, no_adjustment, hardship)
        adjustment_factor_variable.update({category: variable})

    # define the linear optimization problem
    monthly_adjustments = LpProblem("total_adjustments", LpMinimize)

    # the objective is to minimize the total adjustments needed
    factors = []
    for category in spending_categories:
        factors.append(adjustment_factor_variable[category])
    monthly_adjustments += lpSum(factors)

    # the adjustments cannot take us below a minimum standard of living
    for category in spending_categories:
        monthly_adjustments += spending[category] * (1 - adjustment_factor_variable[category]) >= spending_minimum[
            category]

    # we must live within our means
    linear_factors = []
    for category in spending_categories:
        linear_factors.append(spending[category] * (1 - adjustment_factor_variable[category]))

    monthly_adjustments += lpSum(linear_factors) <= monthly_income

    # find budget adjustments that work
    status = monthly_adjustments.solve()
    successfully_optimized = status > 0

    # Return values of the variables
    new_budget = {}
    if successfully_optimized:
        for category in spending_categories:
            adjustment = value(adjustment_factor_variable[category])
            new_budget[category] = spending[category] * (1 - adjustment)
    else:
        new_budget = {}

    return jsonify(new_budget)


if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    host = str(os.getenv('HOST'))

    app.run(port=port, host=host)

