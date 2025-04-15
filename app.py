from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def enviar_pdf():
    return send_file('foda.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render le pasa un puerto
    app.run(host='0.0.0.0', port=port)

