from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def enviar_pdf():
    return send_file('foda.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run()
