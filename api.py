from flask import Flask, render_template
import basecon as bdd
mongo1=bdd.conexion()
app = Flask(__name__)
@app.route('/')
def home():
    lista = []
    for r in mongo1.list_collection_names():
        a = mongo1[r]
        for c in a.find({}):
            elec = {
                "_id ": c['_id'],
                "name": c['name'],
                "marca": c['name'],
                "price": c['price']
            }
            lista.append(elec)
    return render_template('inicio.html', datos=lista)
if __name__ == '__main__':
    app.run(debug=True, port=4000)