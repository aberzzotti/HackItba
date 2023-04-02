import MySQLdb
from flask import Flask, render_template, request,session

from utilities.mail import sendEmail
from utilities.scrap_argprop import scrapingArgenProp
from utilities.scrap_clarinprop import scrapingClarinProp
from utilities.properati import properatiWebScraping
app = Flask(__name__)
app.secret_key = "vivi"


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/menu')
def menu():
  return render_template('index.html')

@app.route('/crearUsuario', methods=['GET', 'POST'])
def crearUsuario():
  if (request.method == "POST"):
    session['usuario'] = str(request.form['nombre'])
    return render_template("pagina.html")
  else:
    return render_template("crearUsuario.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
  if (request.method == "POST"):
    session['usuario'] = str(request.form['nombre'])
    print(session['usuario'])
    return render_template("pagina.html")
  else:
    return render_template("login.html")


@app.route('/pagina', methods=['GET', 'POST'])
def pagina():
  return render_template("pagina.html")


@app.route('/barrios', methods=['GET'])
def barrios():

  return "HOLA"

@app.route('/user', methods=['POST'])
def user():
 

  return render_template("pagina.html")

@app.route('/mail', methods=['POST'])
def mail():
    cantAmb = str(request.form["cant"])
    barrio = request.form["barrio"]
    precioMin = str(request.form["min"])
    precioMax = str(request.form["max"])
    print(session['usuario'])
    email = str(session['usuario'])
    user = str(session['usuario']) 
    resultsProperati = properatiWebScraping(cantAmb, precioMin, precioMax, barrio)
    resultsArgen = scrapingArgenProp(cantAmb, barrio, precioMin, precioMax)
    resultsClarin = scrapingClarinProp(cantAmb, barrio, precioMin, precioMax)
    results = resultsProperati + resultsArgen + resultsClarin
    print(results)
    try:
        if len(results)>0:
            sendEmail("Alquileres disponibles!", email, results, user )
    except Exception as ex:
        print(ex)
    return "hola"


app.run(host='0.0.0.0', port=8000)
