import os
import MySQLdb
import smtplib
import random
import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file
from database import db_connect,inc_reg,ins_loginact
# Import Libraries
import numpy as num
import pandas as pd
 
 
import sys
import io
import json
 

# def db_connect():
#     _conn = MySQLdb.connect(host="localhost", user="root",
#                             passwd="root", db="assigndb")
#     c = _conn.cursor()

#     return c, _conn


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")
    
@app.route("/1.html")
def admin():
    return render_template("1.html")

@app.route("/men.html")
def men():
    return render_template("men.html")

@app.route("/women.html")
def women():
    return render_template("women.html")

@app.route("/user.html")
def ins():
    return render_template("user.html")


@app.route("/increg.html")
def increg():
    return render_template("increg.html")





@app.route("/ihome.html")
def ihome():
    return render_template("ihome.html")




@app.route("/index")
def index():
    return render_template("index.html") 




# -------------------------------Registration-----------------------------------------------------------------    




@app.route("/inceregact", methods = ['GET','POST'])
def inceregact():
   if request.method == 'POST':    
      
      status = inc_reg(request.form['username'],request.form['password'],request.form['email'],request.form['mobile'])
      
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("increg.html",m1="failed")


@app.route("/menact", methods = ['GET','POST'])
def menact():
   if request.method == 'POST':    
      
      chest = int(request.form['chest'])
      shoulders = int(request.form['shoulders'])
      dlength = float(request.form['dlength'])
      dsize = int(request.form['dsize'])
      ashoulder = float(request.form['ashoulder'])
      slength = float(request.form['slength'])
      dcolour = request.form['dcolour']  
      Category = request.form['Category']

      print(Category)
      Features_labels = pd.read_csv("fd.csv")
      
      DatasetFeatureNames = ['chest', 'sholders', 'length', 'size', 'across sholder', 'sleeve length', 'colour','Category','Label']
         
      featuredata_X = Features_labels.iloc[:, :-1].values
      Labeldata_y= Features_labels.iloc[:, 8].values
      from sklearn.preprocessing import LabelEncoder
      trainx=LabelEncoder()      
      featuredata_X[:,7]=trainx.fit_transform(featuredata_X[:,7])
      from sklearn.model_selection import train_test_split
      X_train, X_test, y_train, y_test = train_test_split(featuredata_X, Labeldata_y,test_size=0.2, random_state=69)  
      from sklearn.linear_model import LogisticRegression
      LRmodel = LogisticRegression(solver='lbfgs')
      LRmodel.fit(X_train, y_train)
      color=0
      if dcolour == 'white':
         color=0
         var=Category+'mone'
      if dcolour == 'Black':
         color=1
         var=Category+'mtwo'
      if dcolour == 'medium':
         color=2
         var=Category+'mthree'
      import numpy as np
      check = np.array([chest,shoulders, dlength, dsize, ashoulder, slength, color, Category]).reshape(1, -1)
      check[:,7]=trainx.fit_transform(check[:,7])
      pred = LRmodel.predict(check[[0]])
      print(var)
      if pred == 1:
       return render_template("1.html",m1="sucess",da=var)
      elif pred == 2 :
       return render_template("2.html",m1="failed",da=var)
      else:
       return render_template("3.html",m1="failed",da=var)

@app.route("/mewomenactnact", methods = ['GET','POST'])
def womenact():
   if request.method == 'POST':    
      
      bust = int(request.form['bust'])
      waist = int(request.form['waist'])
      hip = int(request.form['hip'])
      shoulders = float(request.form['shoulders'])
      slevers = float(request.form['slevers'])
      dsize =  request.form['dsize']
      dcolour = request.form['dcolour']
      wDatasetFeatureNames = ['Bust', 'waist', 'hip', 'sholders', 'slevers', 'size','colour', 'Label']
      wFeatures_labels=pd.read_csv("fd1.csv")
       
      wfeaturedata_X = wFeatures_labels.iloc[:, :-1].values
      wLabeldata_y= wFeatures_labels.iloc[:, 7].values
      from sklearn.preprocessing import LabelEncoder
      wtrainx=LabelEncoder()
      wfeaturedata_X[:,5]=wtrainx.fit_transform(wfeaturedata_X[:,5])      
      from sklearn.model_selection import train_test_split
      X_wtrain, X_wtest, y_wtrain, y_wtest = train_test_split(wfeaturedata_X, wLabeldata_y,test_size=0.2, random_state=69)
      from sklearn.linear_model import LogisticRegression
      wLRmodel = LogisticRegression(solver='lbfgs')
      wLRmodel.fit(X_wtrain, y_wtrain)
      color=0
      if dcolour == 'white':
         color=0
         var=dsize+'wone'
      if dcolour == 'Black':
         color=1
         var=dsize+'wtwo'
      if dcolour == 'medium':
         color=2
         var=dsize+'wthree'
      import numpy as np
      print(var)       
      check1 = np.array([bust,waist, hip, shoulders, slevers, dsize, color]).reshape(1, -1)
      check1[:,5]=wtrainx.fit_transform(check1[:,5])
      pred = wLRmodel.predict(check1[[0]])
      if pred == 1:
       return render_template("w1.html",m1="sucess",da=var) 
      elif pred == 2 :
       return render_template("w2.html",m1="failed",da=var)
      else:
        return render_template("w3.html",m1="failed",da=var)





      
# #-------------------------------ADD_END---------------------------------------------------------------------------
# # -------------------------------Loginact-----------------------------------------------------------------







@app.route("/inslogin", methods=['GET', 'POST'])       
def inslogin():
    if request.method == 'POST':
        status = ins_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("ihome.html", m1="sucess")
        else:
            return render_template("user.html", m1="Login Failed")
        



# # -------------------------------Loginact End-----------------------------------------------------------------


   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
