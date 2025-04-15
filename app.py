from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/lista1', methods=['GET', 'HEAD'])
def enviar_lista1():
    return send_file('lista_precio_1.pdf', mimetype='application/pdf')

@app.route('/lista2', methods=['GET', 'HEAD'])
def enviar_lista2():
    return send_file('lista_precio_2.pdf', mimetype='application/pdf')

@app.route('/lista3', methods=['GET', 'HEAD'])
def enviar_lista3():
    return send_file('lista_precio_3.pdf', mimetype='application/pdf')

@app.route('/lista4', methods=['GET', 'HEAD'])
def enviar_lista4():
    return send_file('lista_precio_4.pdf', mimetype='application/pdf')

@app.route('/lista5', methods=['GET', 'HEAD'])
def enviar_lista5():
    return send_file('lista_precio_5.pdf', mimetype='application/pdf')

@app.route('/lista6', methods=['GET', 'HEAD'])
def enviar_lista6():
    return send_file('lista_precio_6.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

