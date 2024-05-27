from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/animal1')
def carpincho():
    return render_template("animal1.html")

@app.route('/animal2')
def erizo():
    return render_template("animal2.html")

@app.route('/animal3')
def ardilla():
    return render_template("animal3.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='comenta', port=3307 )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
