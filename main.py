#-------------------------------------------XX Importing Excel Data XX---------------------------------------#
import numpy as np
import pandas as pd
data = pd.read_excel('PlacementDataset.xlsx')
data = data.rename(columns={' Placed': 'placed'})
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

#-------------------------------------------XX Training the Algorithm XX---------------------------------------#
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,random_state=100)

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=4, random_state=0)
regr.fit(X_train, y_train)
score_rf = regr.score(X_test,y_test)
print("random forest score = {}%".format(score_rf*100))


#--------------------------------------XX Data Base XX------------------------------------------------------#

import sqlite3
conn = sqlite3.connect('db1',check_same_thread=False)
cur = conn.cursor()

# -------------------------------------------XX Flask Framework XX---------------------------------------#

from datetime import date
from flask import Flask, render_template, redirect, request ,flash ,url_for,session
app = Flask(__name__)
app.secret_key = 'Im God'


#-------------------------------------------XX Student Pages XX---------------------------------------#
def get_current_user():
    user = None
    if 'user' in session:
        user = session['user']
        conn = sqlite3.connect('db1',check_same_thread=False)
        cur = conn.cursor()
        cur.execute('select * from register where uname="%s"'%(user))
        userr = cur.fetchall()
        user = userr[0][1]
    return user

def get_date():
    dt = None
    today = date.today()
    dt = today.strftime("%d/%m/%y")
    return dt


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        psw = request.form['psw']
        cur.execute('select * from register where uname="%s" and psw="%s"'%(uname,psw))
        ck = cur.fetchall()
        if uname == 'admin' and psw == 'admin':
            return redirect(url_for('admin_home'))
        else:
            pass
        if len(ck)==0:
            flash('Credentials Did not Match','Warning')
        else:
            cur.execute('select uname from register where uname="%s"'%(uname))
            usr = cur.fetchone() 
            us = usr[0]
            session['user'] = usr[0]       
            flash( ' Welcome  '+'{}'.format(us) )
            return redirect(url_for('st_home'))  
    return render_template('login.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        unamee = request.form['uname']
        fnamee = request.form['fname']
        emaill = request.form['email']
        psww = request.form['psw']
        cpsww = request.form['cpsw']
        print('Username = {} Full Name = {} Email = {} Password = {} Confirm Password = {}'.format(unamee,fnamee,emaill,psww,cpsww))
        if psww == cpsww :
            pass
        else:
            flash("Passwords Don't Match","Warning")
            return redirect(url_for('register'))
        try:
            cur.execute('insert into register (uname,fname,email,psw,cpsw) values ("{}","{}","{}","{}","{}")'.format(unamee,fnamee,emaill,psww,cpsww))
            conn.commit()
            flash('You Have Been Registered!!!',"Success")
            return redirect(url_for('login'))
        except:
            flash('User Exists','Warning')
    return render_template('register.html')

@app.route('/st_home')
def st_home():
    if not session.get('user'):
        return render_template('login.html')
    else:
        # 
        return render_template('st_home.html')

@app.route('/c_quiz',methods=['POST','GET'])
def c_quiz():
    user = get_current_user()
    dt = get_date()
    if request.method == 'POST':
        ans1 = request.form['question1']
        ans2 = request.form['question2']
        ans3 = request.form['question3']
        ans4 = request.form['question4']
        ans5 = request.form['question5']
        ans6 = request.form['question6']
        ans7 = request.form['question7']
        ans8 = request.form['question8']
        ans9 = request.form['question9']
        ans10 = request.form['question10']
        count=0
        if ans1 == "ans1":
            count+=1
        if ans2 == "ans2":
            count+=1
        if ans3 == "ans3":
            count+=1
        if ans4 == "ans4":
            count+=1
        if ans5 == "ans5":
            count+=1
        if ans6 == "ans6":
            count+=1
        if ans7 == "ans7":
            count+=1
        if ans8 == "ans8":
            count+=1
        if ans9 == "ans9":
            count+=1
        if ans10 == "ans10":
            count+=1
        percentage = (count/10)*100
        output = int (percentage)
        print(output)
        print(dt)
        try:
            cur.execute('create table {}'.format(user)+' (id integer primary key autoincrement,date varchar(10) unique,uname varchar(10),c int,python int,java int,avg int)')
            conn.commit()
        except:
            pass
        try:
            cur.execute('insert into {}'.format(user)+'(date,uname,c) values ("{}","{}",{})'.format(dt,user,output))
            conn.commit()
        except:
            flash('You Have Already Taken Test Today','Warning')
            return redirect(url_for('st_home'))
        return redirect(url_for('python'))    
    return render_template('c_quiz.html')

@app.route('/python',methods=['POST','GET'])
def python():
    user = get_current_user()
    dt = get_date()
    if request.method == 'POST':
        ans1 = request.form['question1']
        ans2 = request.form['question2']
        ans3 = request.form['question3']
        ans4 = request.form['question4']
        ans5 = request.form['question5']
        ans6 = request.form['question6']
        ans7 = request.form['question7']
        ans8 = request.form['question8']
        ans9 = request.form['question9']
        ans10 = request.form['question10']
        count=0
        if ans1 == "ans1":
            count+=1
        if ans2 == "ans2":
            count+=1
        if ans3 == "ans3":
            count+=1
        if ans4 == "ans4":
            count+=1
        if ans5 == "ans5":
            count+=1
        if ans6 == "ans6":
            count+=1
        if ans7 == "ans7":
            count+=1
        if ans8 == "ans8":
            count+=1
        if ans9 == "ans9":
            count+=1
        if ans10 == "ans10":
            count+=1
        percentage = (count/10)*100
        output = int (percentage)
        cur.execute('update "{}"'.format(user)+'set python = "%s" where date = "%s"'%(output,dt))
        return redirect(url_for('java'))
    return render_template('python.html')

@app.route('/java',methods=['POST','GET'])
def java():
    user = get_current_user()
    dt = get_date()
    if request.method == 'POST':
        ans1 = request.form['question1']
        ans2 = request.form['question2']
        ans3 = request.form['question3']
        ans4 = request.form['question4']
        ans5 = request.form['question5']
        ans6 = request.form['question6']
        ans7 = request.form['question7']
        ans8 = request.form['question8']
        ans9 = request.form['question9']
        ans10 = request.form['question10']
        count=0
        if ans1 == "ans1":
            count+=1
        if ans2 == "ans2":
            count+=1
        if ans3 == "ans3":
            count+=1
        if ans4 == "ans4":
            count+=1
        if ans5 == "ans5":
            count+=1
        if ans6 == "ans6":
            count+=1
        if ans7 == "ans7":
            count+=1
        if ans8 == "ans8":
            count+=1
        if ans9 == "ans9":
            count+=1
        if ans10 == "ans10":
            count+=1
        percentage = (count/10)*100
        output = int (percentage)
        cur.execute('update "{}"'.format(user)+'set java = "%s" where date = "%s"'%(output,dt))
        cur.execute('select c,python,java from "{}"'.format(user)+'where date="%s"'%(dt))
        avg_a = cur.fetchall()
        avg1 = (avg_a[0][0] + avg_a[0][1] + avg_a[0][2]) / 3
        avg = round(avg1)
        cur.execute('update "{}"'.format(user)+'set avg = "%s" where date = "%s"'%(avg,dt))
        cur.execute('select * from "{}"'.format(user))
        total = cur.fetchall()
        print(total)
        name = total[0][2]
        dte = total[0][1]
        c_score = total[0][3]
        pyt = total[0][4]
        jv = total[0][5]
        avr = total[0][6]
        cur.execute('insert into quiz (date,name,c,python,java,avg) values ("{}","{}",{},{},{},{})'.format(dte,name,c_score,pyt,jv,avr))
        conn.commit()
        flash('Your Scores have been Recorded')
        return redirect(url_for('st_home'))
    return render_template('java.html')

@app.route('/scores')
def scores():
    user = get_current_user()
    cur.execute('select * from "{}"'.format(user))
    total = cur.fetchall()
    
    return render_template('scores.html',total=total)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return home()

#------------------------------------------------XX Admin Pages XX ---------------------------------------------#

def get_student():
    user = None
    if 'user' in session:
        user = session['user']
        conn = sqlite3.connect('db1',check_same_thread=False)
        cur = conn.cursor()
        cur.execute('select * from quiz where name="%s"'%(user))
        user = cur.fetchall()
    return user
        

@app.route('/admin_home',methods=['POST','GET'])
def admin_home():
    if request.method == 'POST':
        name = request.form['name']
        dat = request.form['dte']
        try:
            cur.execute('select * from quiz where name="%s" and date="%s"'%(name,dat))
            dis = cur.fetchall()
            session['user'] = dis[0][2]
            return redirect(url_for('details'))
        except:
            flash('Not Found','Warning')    
    return render_template('admin_home.html')



@app.route('/details',methods=['POST','GET'])
def details():
    user = get_student()
    if request.method == 'POST':
        coding = request.form['Coding']
        aptitude = request.form['aptitude']
        Technical = request.form['Technical']
        Communication = request.form['Communication']
        Core = request.form['Core']
        Puzzle = request.form['Puzzle']
        English = request.form['English']
        Management = request.form['Management']
        Presentation = request.form['Presentation']
        Academic = request.form['Academic']
        Projects = request.form['Projects']
        Internships = request.form['Internships']
        Training = request.form['Training']
        Backlog = request.form['Backlog']
        res = regr.predict([[coding, aptitude, Technical, Communication,
                             Core,
                             Puzzle,
                             English,
                             Management,
                             Presentation,
                             Academic,
                             Projects,
                             Internships,
                             Training,
                             Backlog]])
        print('take it', res)
        session['user'] = res[0]
        return redirect(url_for('predict'))
    return render_template('details.html',user=user)
    
@app.route('/predict')
def predict():
    res = session['user']
    return render_template('predict.html',res=res)

@app.route('/ad_logout')
def ad_logout():
    session.pop('user', None)
    return home()


if __name__ == '__main__':
    app.run(debug=True)
    
