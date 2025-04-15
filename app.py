from flask import Flask, send_file

app = Flask(__name__)

@app.route('/C:/Users/Usuario/Downloads/')
def enviar_pdf():
    return send_file('20250414102815planilladecarga.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run()
