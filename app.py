from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/a')
def homepage1():
    return render_template('index1.html')
    

@app.route('/normalize_taxonomies', methods=['POST'])
def normalize_taxonomies():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        # Salvar o arquivo em algum local no servidor ou processá-lo conforme necessário
        uploaded_file.save(uploaded_file.filename)
        return 'Arquivo enviado com sucesso.'
    else:
        return 'Nenhum arquivo enviado.'
    

@app.route('/normalize_lineage', methods=['POST'])
def normalize_lineage():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        # Salvar o arquivo em algum local no servidor ou processá-lo conforme necessário
        uploaded_file.save(uploaded_file.filename)
        return 'Arquivo enviado com sucessoo.'
    else:
        return 'Nenhum arquivo enviadoo.'


if __name__ == '__main__':
    app.run(debug=True)
