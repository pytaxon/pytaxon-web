import os
from flask import Flask, request, render_template, send_file, session
from pytaxon import Pytaxon

app = Flask(__name__)
app.secret_key = 'Iza minha futura noiva'
app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/test')
def homepage1():
    return render_template('test.html')


@app.route('/test2')
def homepage2():
    return render_template('test2.html')
    

@app.route('/check_taxonomies', methods=['POST'])
def check_taxonomies():
    uploaded_file = request.files['file']

    caminho_temporario = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
    uploaded_file.save(caminho_temporario)

    session['caminho_temporario'] = caminho_temporario

    if uploaded_file.filename != '':  # implement tempfile module
        return render_template('check_taxonomies.html')
    else:
        return 'Nenhum arquivo enviado.'
    

@app.route('/pivot_taxonomies', methods=['POST'])
def pivot_taxonomies():
    genus = request.form['Genus']
    species = request.form['Species']
    caminho_temporario = session.get('caminho_temporario')

    if genus and species:  # implement tempfile module
        pt = Pytaxon()
        pt.read_spreadshet(caminho_temporario)
        pt.read_taxon_columns(genus, species)
        pt.connect_to_api()
        pt.data_incorrect_taxons()
        pt.create_taxonomies_pivot_spreadsheet()
        return send_file(
                'UPLOAD_FOLDER/' + pt._checked_df_name,  # REFACTOR
                as_attachment = True,
                download_name = pt._checked_df_name,
                mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
    else:
        return 'Nenhum arquivo enviado.'
    

@app.route('/update_original_spreadsheet')
def update_original_spreadsheet():
    return render_template('update_original_spreadsheet.html')
    

@app.route('/check_lineage', methods=['POST'])
def check_lineage():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        # uploaded_file.save(uploaded_file.filename)
        return 'Arquivo enviado com sucessoo.'
    else:
        return 'Nenhum arquivo enviadoo.'


if __name__ == '__main__':
    app.run(debug=True)
