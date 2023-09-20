from flask import Flask, request, render_template, send_file
from pytaxon import Pytaxon

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/test')
def homepage1():
    return render_template('test.html')
    

@app.route('/normalize_taxonomies', methods=['POST'])
def normalize_taxonomies():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':  # implement tempfile module
        file_path = f'process/{uploaded_file.filename}'
        uploaded_file.save(file_path)

        pt = Pytaxon()
        pt.read_spreadshet(file_path)
        pt.read_taxon_columns('Genus1', 'Species1')  # TEST
        pt.connect_to_api()
        pt.data_incorrect_taxons()
        pt.create_taxonomies_pivot_spreadsheet()
        return send_file(
                pt._normalized_df_name,
                as_attachment=True,
                download_name=pt._normalized_df_name,
                mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
    else:
        return 'Nenhum arquivo enviado.'
    

@app.route('/normalize_lineage', methods=['POST'])
def normalize_lineage():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        # uploaded_file.save(uploaded_file.filename)
        return 'Arquivo enviado com sucessoo.'
    else:
        return 'Nenhum arquivo enviadoo.'


if __name__ == '__main__':
    app.run(debug=True)
