from app import app
from flask import render_template
from models.orders_list import order

@app.route('/orders')
def index():
    return render_template("index.html", title = "Orders", order = order)

@app.route('/orders/2')
def get():
    return render_template("order.html", title = "Orders", order = order[2])

@app.route('/orders/1')
def get():
    return render_template("order.html", title = "Orders", order = order[1])