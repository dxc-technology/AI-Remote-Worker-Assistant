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
    _input = request.args['input']
    return _input

if __name__ == '__main__':
    #port = int(os.getenv('PORT'))
    #print("Starting app on port %d" % port)
    #app.run(debug=False, port=port, host='0.0.0.0')
    
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '1000'))
    except ValueError:
        PORT = 1000
    app.run(HOST, PORT)
    
'''if __name__ == '__main__':
    app.run(debug=True, port=1000)'''
