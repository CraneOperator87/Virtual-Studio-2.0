from flask import Flask, render_template, request, 
import json

from json import load

paameldte = []
favoritter = []

app = Flask(__name__)

fil = open("land.json", encoding="utf-8")
land_json = load(fil)
fil.close




@app.get("/")
def rute_index():
    return render_template("index.html", land=land_json)

'''@app.route("/onske", methods=["GET", "POST"])
def onskeliste():
    if request.method == "POST":
        navn = request.form.get("navn")
        favoritter.append(navn)
        return redirect("onske")'''



@app.get("/land/<nokkel>")
def rute_land(nokkel):
    valgt_land = land_json[nokkel]
    return render_template("valg_land.html", land=valgt_land)

@app.get("/reisevelger")
def rute_valg():
    return render_template("reisevelger.html", land=land_json)

@app.get("/takk")
def rute_takk():
    navn = request.args.get("navn")
    aktivitet = request.args.get("aktivitet")
    land = request.args.get("land")

    ny_paameldt = {
        "navn":navn,
        "aktivitet":aktivitet,
        "land":land
    }
    paameldte.append(ny_paameldt) 
    print(paameldte) 
    return render_template("takk.html", navn=navn, aktivitet=aktivitet, paameldte=paameldte)




@app.get("/book")
def rute_book():
    return render_template("book.html", land=land_json)



users = {}  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = password
            #return 'Bruker har blitt registrert.'
            return render_template('brukerregistrert.html')

        if users[username] == password:
            #return 'Du har blitt logget inn!'
            return render_template('loggetinn.html')
        else:
            #return 'Feil passord til denne brukeren. Prøv igjen.'
            return render_template('feilpassord.html')

    return render_template('login.html')


@app.route("/anmeldelser", methods=["POST", "GET"])
def rute_anmeldelser():
    if request.method == "POST":
        navn = request.form["navn"]
        melding = request.form["melding"]
        anmeldelser.append({
            "navn": navn,
            "melding": melding
        })
        skriv_anmeldelser()


    return render_template('anmeldelser.html', anmeldelser=anmeldelser)

fil_anmeldelser = open("anmeldelse.json")
anmeldelser = json.load(fil_anmeldelser)
fil_anmeldelser.close()


def skriv_anmeldelser():
    fil_anmeldelser = open("anmeldelse.json", "w")
    json.dump(anmeldelser, fil_anmeldelser)
    fil_anmeldelser.close()

@app.route("/reisevelger/<type>")
def rute_sortering(type):
    sortert = {}
    for id, enkeltland in land_json.items():
        if enkeltland["type"] == type:
            sortert[id] = enkeltland
    return render_template("reisevelger.html", land=sortert)



 


app.run(debug=True)