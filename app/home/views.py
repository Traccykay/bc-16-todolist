from flask import render_template
from flask_login import login_required

from app.models import Card, Item, List
from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    lists = List.query.all()
    return render_template('home/dashboard.html', title="Dashboard", lists=lists)

"""@home.route('/addlist')
@login_required
def addlist():
    my_list=ListForm()
    if my_list.validate_on_submit():
        a_list = List(name=my_list.list_name.data)
        db.session.add(a_list)
        db.session.commit()

        return redirect(url_for('home.dashboard'))
    return render_template('home/dashboard.html', my_list=my_list)"""
