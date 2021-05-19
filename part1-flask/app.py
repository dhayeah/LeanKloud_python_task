from flask import Flask, render_template, request, redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hello123'
app.config['MYSQL_DB'] = 'task'

mysql = MySQL(app)

@app.route("/")
def home():
    cur=mysql.connection.cursor() 
    cur.execute("select * from todo")
    data=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("index.html",computers=data)

@app.route("/add", methods=["POST"])
def add():
    tname=request.form.get("task")
    due=request.form.get("due")
    status=request.form.get("status")
    cur = mysql.connection.cursor()
    cur.execute("insert into todo(tname,due,status) values(%s, %s,%s)",(tname,due,status))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))


@app.route("/update", methods=["POST"])
def update():
    status=request.form.get("status")
    id=request.form.get("id")
    cur = mysql.connection.cursor()
    cur.execute("update todo set status=%s where id=%s",(status,id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route("/due" ,methods=["GET"])
def due():
    duedate=request.args.get("due_date")
    cur=mysql.connection.cursor() 
    print(duedate)
    cur.execute("select * from todo where due = %s",(duedate,))
    data=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("due.html",computers=data)

@app.route("/overdue",methods=["GET"])
def overdue():
    cur=mysql.connection.cursor() 
    cur.execute("select * from todo where due <= CURDATE()")
    data=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("due.html",computers=data)

@app.route("/finished",methods=["GET"])
def finished():
    cur=mysql.connection.cursor() 
    cur.execute("select * from todo where status='finished'")
    data=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("due.html",computers=data)


if __name__ == '__main__':
    app.run(debug=True)
