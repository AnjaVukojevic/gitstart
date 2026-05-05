import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def dostavaHrane():
    # poziv baze i preuzimanje podataka
    naslovSpiska = "Restorani"
    #spisakRestorana = ["Bavka", "Dits", "ABC", "Nedodjija"]
    # prosledjivanje podataka sablonu
    con = sqlite3.connect("dostavaHrane.db")
    cur = con.cursor()
    cur.execute("SELECT id, naziv FROM restoran")
    spisakRestorana = cur.fetchall()
    return render_template("index.html", 
                           naslov=naslovSpiska, 
                           spisak=spisakRestorana)

@app.route("/restoran")
def restoran():
    # poziv baze i preuzimanje podataka
    naslovRestorana = "Bavka"
    spisakJela = ["Pasta", "Pljeskavica", "Club sendvic", "Pica"]
    # prosledjivanje podataka sablonu
    return render_template("restoran.html", 
                           naslov=naslovRestorana, 
                           spisak=spisakJela)

@app.route("/primer-string")
def string():
    return "Neki ne preterano dugacak tekst"

@app.route("/primer-broj")
def broj():
    return 265

@app.route("/primer-niz")
def niz():
    nekiNiz = [1, 2, 3, 4, 5]
    return nekiNiz

@app.route("/primer-json")
def primerJson():
    data = {
        "message": "This is a JSON response",
        "status": "success"
    }
    return data

@app.route("/primer-html")
def primerHTML():
    data = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <h1>Zdravo programeri</h1>
</body>
</html>"""
    return data

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
   app.run()
   
