import pandas as pd
import requests
from collections import defaultdict
from pprint import pprint
import os

class Pytaxon:
    def __init__(self):
        self._path_to_original_spreadsheet:str = None
        self._name_original_spreadsheet:str = None
        self._original_df:pd.DataFrame = None
        self._genus_column:str = None
        self._species_column:str = None
        self._taxons_list:list = None
        self._json_post:dict = None
        self._matched_names:dict = None
        self._incorrect_taxon_data:defaultdict = defaultdict(list)
        self._checked_df_name:dict = None
        self._df_to_correct:pd.DataFrame = None
        self._corrected_df = None
        self._lineage_dict = dict
        self._incorrect_lineage_data:defaultdict = defaultdict(list)

    def read_spreadshet(self, spreadsheet:str) -> None:
        self._path_to_original_spreadsheet = spreadsheet.replace('"', '')
        self._name_original_spreadsheet, extension = os.path.splitext(os.path.basename(self._path_to_original_spreadsheet))

        try:
            self._original_df = pd.read_excel(self._path_to_original_spreadsheet).reset_index()
            print('Success reading the spreadsheet, now entering columns names...')
        except Exception as e:
            print('Error reading the spreadsheet: ', e)  

    # Analyze TAXONOMIES (genus and species)
    def read_taxon_columns(self, genus, species) -> None:
        self._genus_column = genus
        self._species_column = species

        try: 
            self._taxons_list = list((self._original_df[self._genus_column] + ' ' + self._original_df[self._species_column]).values)
            print('Success loading spreadsheet with given columns names, now connecting to API...')
        except Exception as e:
            print('Error loading spreadsheet with given columns names', e)

    def connect_to_api(self) -> None:
        self._json_post = {'names': self._taxons_list,
                           'do_approximate_matching': True,
                           'context_name': 'All life'}

        try:
            self.r = requests.post('https://api.opentreeoflife.org/v3/tnrs/match_names', json=self._json_post)
            print('Success accessing the OpenTreeOfLife API, now checking taxons...')
        except Exception as error:
            print('Error accessing the OpenTreeOfLife API: ', error)

        # pprint(self.r.json())

    def data_incorrect_taxons(self) -> None:
        self._matched_names = self.r.json()['matched_names']

        for i, taxon in enumerate(self._matched_names):
            try:
                first_match_score = self.r.json()['results'][i]['matches'][0]['score']
            except:
                self._incorrect_taxon_data['Error Line'].append(self._matched_names.index(taxon, i))
                self._incorrect_taxon_data['Wrong Taxon'].append(taxon)
                self._incorrect_taxon_data['Options'].append('No Correspondence')
                self._incorrect_taxon_data['Match Score'].append(0)
                self._incorrect_taxon_data['Alternatives'].append(None)
                self._incorrect_taxon_data['Taxon Sources'].append(None)
                continue

            if first_match_score < 1.:
                matches = self.r.json()['results'][i]['matches']
                match_names  = [match['matched_name'] for match in matches]

                self._incorrect_taxon_data['Error Line'].append(self._matched_names.index(taxon, i))
                self._incorrect_taxon_data['Wrong Taxon'].append(taxon)
                self._incorrect_taxon_data['Options'].append((list(range(1, len(match_names)+1))))
                self._incorrect_taxon_data['Matches Scores'].append([round(match['score'], 3) for match in matches])
                self._incorrect_taxon_data['Alternatives'].append(match_names)
                self._incorrect_taxon_data['Taxon Sources'].append([match['taxon']['tax_sources'] for match in matches])
                continue

        # pprint(self._matched_names)

    def create_taxonomies_pivot_spreadsheet(self) -> None:
        def sum2(num):
            return num + 2
        
        Alternatives1 = []
        Alternatives2 = []
        for i in range(len(self._incorrect_taxon_data['Alternatives'])):
            result = f"Species Name: {self._incorrect_taxon_data['Alternatives'][i][0]} | Score: {self._incorrect_taxon_data['Matches Scores'][i][0]} | Sources: {self._incorrect_taxon_data['Taxon Sources'][i][0]}"
            result2 = f"Species Name: {self._incorrect_taxon_data['Alternatives'][i][1]} | Score: {self._incorrect_taxon_data['Matches Scores'][i][1]} | Sources: {self._incorrect_taxon_data['Taxon Sources'][i][1]}"
            
            Alternatives1.append(result)
            Alternatives2.append(result2)

        self._df_to_correct = pd.DataFrame(data={  # Refazer
            'Error Line': list(map(sum2, self._incorrect_taxon_data['Error Line'])),
            'Wrong Taxon': self._incorrect_taxon_data['Wrong Taxon'],
            'Options': self._incorrect_taxon_data['Options'],
            'Alternative1': Alternatives1,  # REDO
            'Alternative2': Alternatives2  # REDO
            })

        # print(self._df_to_correct)
        try:
            self._checked_df_name = f'TO_CORRECT_{self._name_original_spreadsheet}.xlsx'
            self._df_to_correct.to_excel('UPLOAD_FOLDER/' + self._checked_df_name)
        except Exception as e:
            print('Error creating corrected spreadsheet: ', e)

    def update_original_spreadsheet(self):
        corrections = self._df_to_correct['Alternative1'].str.split(expand=True)  # Ajeitar

        self._corrected_df = self._original_df

        self._corrected_df.loc[self._incorrect_taxon_data['Error Line'], self._genus_column] = corrections[1].values
        self._corrected_df.loc[self._incorrect_taxon_data['Error Line'], self._species_column] = corrections[2].values

        try:
            self._corrected_df.to_excel(f'{self._path_to_original_spreadsheet[:-4]}_corrigido.xlsx')
        except Exception as e:
            print('Error to update original spreadsheet: ', e)
