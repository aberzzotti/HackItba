import MySQLdb
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/menu')
def menu():
  return render_template('index.html')


@app.route('/crearUsuario', methods=['GET', 'POST'])
def crearUsuario():
  if (request.method == "POST"):
    return render_template("pagina.html")
  else:
    return render_template("crearUsuario.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
  if (request.method == "POST"):
    return render_template("pagina.html")
  else:
    return render_template("login.html")


@app.route('/pagina', methods=['GET', 'POST'])
def pagina():
  return render_template("pagina.html")


@app.route('/barrios', methods=['GET'])
def barrios():
  host = "186.18.137.196"
  user = "DB_2020_5BINF_G02",
  password = "marsela1234",
  database = "DB_2020_5BINF_G02"
  datos = [host, user, password, database]
  conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
  cursor = conn.cursor()  # Crear un cursor
  cursor.execute("Select * from barrio")  # Ejecutar una consulta
  data = cursor.fetchall()
  return data


app.run(host='0.0.0.0', port=8000)
