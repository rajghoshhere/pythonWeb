# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:26:26 2020

@author: rghosh
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)