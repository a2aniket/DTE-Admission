<<<<<<< HEAD
<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:28:08 2020

@author: sai
"""

from flask import Flask,render_template,request
import sys
import pickle
app=Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/all", methods=["GET", "POST"])
def all():
    if request.method == "POST":
        marks =request.form.get("marks")
        gender=request.form.get("gender")
        cast=request.form.get("cast")
        course=request.form.get("course")
        print(float(marks))
        print(int(gender))
        print(cast)
        print(int(course))
        model = pickle.load(open('../../data/Train Model/all/model {}.pkl'.format(cast), 'rb'))
        predict= model.predict([[float(marks),int(gender),int(course)]])
        
        
    return render_template("home.html", prediction=predict)

@app.route("/dist", methods=["GET", "POST"])
def dist():
    if request.method == "POST":
        marks =request.form.get("distmarks")
        dist=request.form.get("dist")
        gender=request.form.get("distgender")
        cast=request.form.get("distcast")
        course=request.form.get("distcourse")
        print(float(marks))
        print(dist)
        print(int(gender))
        print(cast)
        print(int(course))
        model = pickle.load(open('../../data/Train Model/dist/{}/model {}.pkl'.format(dist,cast), 'rb'))
        distprediction= model.predict([[float(marks),int(gender),int(course)]])
        
        
    return render_template("home.html", destprediction=distprediction)

app.run(debug=True)

=======
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:28:08 2020

@author: sai
"""

from flask import Flask,render_template,request
import sys
import pickle
app=Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/all", methods=["GET", "POST"])
def all():
    if request.method == "POST":
        marks =request.form.get("marks")
        gender=request.form.get("gender")
        cast=request.form.get("cast")
        course=request.form.get("course")
        print(float(marks))
        print(int(gender))
        print(cast)
        print(int(course))
        model = pickle.load(open('../../data/Train Model/all/model {}.pkl'.format(cast), 'rb'))
        predict= model.predict([[float(marks),int(gender),int(course)]])
        
        
    return render_template("home.html", prediction=predict)

@app.route("/dist", methods=["GET", "POST"])
def dist():
    if request.method == "POST":
        marks =request.form.get("distmarks")
        dist=request.form.get("dist")
        gender=request.form.get("distgender")
        cast=request.form.get("distcast")
        course=request.form.get("distcourse")
        print(float(marks))
        print(dist)
        print(int(gender))
        print(cast)
        print(int(course))
        model = pickle.load(open('../../data/Train Model/dist/{}/model {}.pkl'.format(dist,cast), 'rb'))
        distprediction= model.predict([[float(marks),int(gender),int(course)]])
        
        
    return render_template("home.html", destprediction=distprediction)

app.run(debug=True)

>>>>>>> b57ac0e1b1d7ce228cbe4871785b4dbb872aa985
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:28:08 2020

@author: sai
"""

from flask import Flask,render_template,request
import sys
import pickle
app=Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/all", methods=["GET", "POST"])
def all():
    if request.method == "POST":
        marks =request.form.get("marks")
        gender=request.form.get("gender")
        cast=request.form.get("cast")
        course=request.form.get("course")
        print(float(marks))
        print(int(gender))
        print(cast)
        print(int(course))
        model = pickle.load(open('../../data/Train Model/all/model {}.pkl'.format(cast), 'rb'))
        predict= model.predict([[float(marks),int(gender),int(course)]])
        
        
    return render_template("home.html", prediction=predict)

@app.route("/dist", methods=["GET", "POST"])
def dist():
    if request.method == "POST":
        marks =request.form.get("distmarks")
        dist=request.form.get("dist")
        gender=request.form.get("distgender")
        cast=request.form.get("distcast")
        course=request.form.get("distcourse")
        print(float(marks))
        print(dist)
        print(int(gender))
        print(cast)
        print(int(course))
        model = pickle.load(open('../../data/Train Model/dist/{}/model {}.pkl'.format(dist,cast), 'rb'))
        distprediction= model.predict([[float(marks),int(gender),int(course)]])
        
        
    return render_template("home.html", destprediction=distprediction)

app.run(debug=True)

>>>>>>> b57ac0e1b1d7ce228cbe4871785b4dbb872aa985
