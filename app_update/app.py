from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/parque_tayrona')
def parque():
    return render_template('parque_tayrona.html')

@app.route('/santa_marta')
def san():
    return render_template('santa_marta.html')

@app.route('/minca')
def minca():
    return render_template('minca.html')

@app.route('/ciudad_perdida')
def ciu():
    return render_template('ciudad_perdida.html')

@app.route('/palomino')
def palo():
    return render_template('palomino.html')

@app.route('/tours')
def tour():
    return render_template('tours.html')

@app.route('/playa_blanca')
def playa():
    return render_template('Playa_Blanca.html')

@app.route('/cabo_sanjuan')
def cabo():
    return render_template('cabo_sanjuan.html')

@app.route('/pozo_azul')
def pozo():
    return render_template('pozo_azul.html')

@app.route('/untitled')
def resultado():
    return render_template('untitled.html')

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

@app.route('/compra', methods=['POST', 'GET'])
def compra():
    if request.method == 'POST':
        valor = request.form['valor']
        print(valor)
        return render_template('pagos.html')

if __name__ == "__main__":
    app.run(debug=True)