#!/usr/bin/env python
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/developer/')
def developer():
    return redirect(url_for('developer_apps'))

@app.route('/developer/apps/')
def developer_apps():
    return render_template('developer_apps.html')

@app.route('/developer/app/<int:app_id>')
def developer_app(app_id=-1):
    return render_template('developer_app_detail.html', app_id=app_id)

@app.route('/developer/users/')
def developer_users():
    return render_template('developer_users.html')

@app.route('/developer/user/<int:user_id>')
def developer_user(user_id=-1):
    return render_template('developer_user_detail.html', user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
