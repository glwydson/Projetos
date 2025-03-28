from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contador():
    resultado = None
    if request.method == 'POST':
        data_inicial = request.form['data_inicial']
        data_final = request.form['data_final']

        # Converte as datas de string para objeto datetime
        formato = "%Y-%m-%d"
        try:
            data_inicial = datetime.strptime(data_inicial, formato)
            data_final = datetime.strptime(data_final, formato)

            # Calcula a diferença de dias
            resultado = (data_final - data_inicial).days
        except ValueError:
            resultado = "Datas inválidas! Por favor, insira no formato AAAA-MM-DD."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
