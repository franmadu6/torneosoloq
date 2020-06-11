import functools
from requests_html import HTMLSession
from bs4 import *
from tabulate import tabulate
from flask import Flask, redirect, render_template, request, session, url_for,abort
import osñ

app = Flask(__name__, template_folder="templates")

#---------pg de inicio
@app.route('/',methods=["GET"])
def inicio():
    return render_template("index.html",error= None)

#----------pg pickem
@app.route('/pickem',methods=["GET","POST"])
def oblibros():
    
    return render_template('pickem.html',error= None)

#-----------pg premios
@app.route('/premios',methods=["GET","POST"])
def obusuario():
        
    return render_template('premios.html',error= None)

#-----------pg reglas
@app.route('/reglas',methods=["GET","POST"])
def oblistasmr():
        
    return render_template('reglas.html',error= None)

#activar estas lineas para que vaya en heroku.
if __name__ == '__main__':
    port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)

#activar esta linea para que vaya en la termial.
#app.run(debug=True)
