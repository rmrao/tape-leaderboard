from typing import List, Dict, Any
from flask import render_template
from app import app
from app.models import LeaderboardEntry, DisplayName


class LeaderboardTable:

    def __init__(self, name: str, title: str, fieldnames: List[str]):
        # Other metadata: pretrained, neural, institution, citation
        metadata_names = ['submission_date', 'name']
        self._name = name
        self._title = title
        self._fieldnames = metadata_names + fieldnames

    @property
    def name(self) -> str:
        return self._name

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return ''

    @property
    def fieldnames(self) -> List[str]:
        return self._fieldnames

    @property
    def headers(self) -> List[str]:
        return [DisplayName.get_by_key_name(key_name) for key_name in self._fieldnames]

    @property
    def entries(self) -> List[Dict[str, Any]]:
        entries = LeaderboardEntry.query.all()
        entry_info = [{field: getattr(entry, field) for field in self.fieldnames}
                      for entry in entries]
        return entry_info


overall_table = LeaderboardTable(
    'overall',
    'Leaderboard - TAPE',
    ['ss_cb513_3', 'cp_medium_long_pl5', 'rh_fold_1', 'fl_rho_full', 'st_rho'])

secondary_structure_table = LeaderboardTable(
    'secondary_structure', 'Secondary Structure - TAPE',
    ['ss_cb513_3', 'ss_casp12_3', 'ss_ts115_3', 'ss_cb513_8', 'ss_casp12_8', 'ss_ts115_8'])

contact_prediction_table = LeaderboardTable(
    'contact_prediction', 'Contact Prediction - TAPE',
    ['cp_short_range_auprc', 'cp_short_range_pl', 'cp_short_range_pl2', 'cp_short_range_pl5',
     'cp_medium_range_auprc', 'cp_medium_range_pl', 'cp_medium_range_pl2',
     'cp_medium_range_pl5', 'cp_long_range_auprc', 'cp_long_range_pl', 'cp_long_range_pl2',
     'cp_long_range_pl5'])

remote_homology_table = LeaderboardTable(
    'remote_homology', 'Remote Homology - TAPE',
    ['rh_fold_1', 'rh_fold_5', 'rh_superfamily_1', 'rh_superfamily_5', 'rh_family_1',
     'rh_family_5'])

fluorescence_table = LeaderboardTable(
    'fluorescence', 'Fluorescence - TAPE',
    ['fl_mse_full', 'fl_rho_full', 'fl_mse_bright', 'fl_rho_bright',
     'fl_mse_dark', 'fl_rho_dark'])

stability_table = LeaderboardTable(
    'stability', 'Stability - TAPE',
    ['st_rho', 'st_acc', 'st_aaa_rho', 'st_aaa_acc', 'st_abba_rho', 'st_abba_acc',
     'st_babb_rho', 'st_babb_acc', 'st_bbabb_rho', 'st_bbabb_acc'])


@app.route('/about')
def about():
    return render_template('about.html', title='Tasks Assessing Protein Embeddings - TAPE')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title=overall_table.title, table=overall_table)


@app.route('/secondary_structure')
def secondary_structure():
    return render_template(
        'index.html', title=secondary_structure_table.title, table=secondary_structure_table)


@app.route('/contact_prediction')
def contact_prediction():
    return render_template(
        'index.html', title=contact_prediction_table.title, table=contact_prediction_table)


@app.route('/remote_homology')
def remote_homology():
    return render_template(
        'index.html', title=remote_homology_table.title, table=remote_homology_table)


@app.route('/fluorescence')
def fluorescence():
    return render_template(
        'index.html', title=fluorescence_table.title, table=fluorescence_table)


@app.route('/stability')
def stability():
    return render_template('index.html', title=stability_table.title, table=stability_table)
