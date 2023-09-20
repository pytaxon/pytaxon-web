from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/a')
def homepage1():
    return render_template('index1.html')
    

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        # Salvar o arquivo em algum local no servidor ou processá-lo conforme necessário
        uploaded_file.save(uploaded_file.filename)
        return 'Arquivo enviado com sucesso.'
    else:
        return 'Nenhum arquivo enviado.'

if __name__ == '__main__':
    app.run(debug=True)
