from typing import List, Dict
from flask import render_template
from app import app
import csv
from pathlib import Path
from collections import namedtuple


Table = namedtuple('Table',
                   ['fieldnames', 'public_fields', 'description', 'models'])

data_dir = Path(__file__).parent / 'data'

with (data_dir / 'results.csv').open() as f:
    reader = csv.reader(f)
    fieldnames: List[str] = next(reader)
    public_names: Dict[str, str] = dict(zip(fieldnames, next(reader)))
    model_info = [dict(zip(fieldnames, info_line)) for info_line in reader]  # type: ignore


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Tasks Assessing Protein Embeddings - TAPE')


@app.route('/leaderboard')
def leaderboard():
    leaderboard_fields = ['date', 'model', 'secondary_structure', 'contact_prediction',
                          'remote_homology', 'fluorescence', 'stability']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Overall Results on TAPE Benchmark Tasks.",
                  model_info)
    return render_template('leaderboard.html', title='Leaderboard - TAPE', table=table)


@app.route('/leaderboard/secondary_structure')
def secondary_structure():
    leaderboard_fields = ['date', 'model', 'ss_cb513_3', 'ss_casp12_3', 'ss_ts115_3',
                          'ss_cb513_8', 'ss_casp12_8', 'ss_ts115_8']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Secondary structure results for the CB513, CASP12, and TS115 datasets. "
                  "Both 3-class and 8-class prediction results are reported",
                  model_info)
    return render_template('leaderboard.html', title='Secondary Structure - TAPE', table=table)


@app.route('/leaderboard/contact_prediction')
def contact_prediction():
    leaderboard_fields = [
        'date', 'model',
        'cp_short_range_auprc', 'cp_short_range_pl', 'cp_short_range_pl2', 'cp_short_range_pl5',
        'cp_medium_range_auprc', 'cp_medium_range_pl', 'cp_medium_range_pl2', 'cp_medium_range_pl5',  # noqa E501
        'cp_long_range_auprc', 'cp_long_range_pl', 'cp_long_range_pl2', 'cp_long_range_pl5']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Contact prediction results on the CASP 12 dataset. Results are reported for "
                  "short (6-11), medium (12-23), and long (24+) range contacts.",
                  model_info)
    return render_template('leaderboard.html', title='Contact Prediction - TAPE', table=table)


@app.route('/leaderboard/remote_homology')
def remote_homology():
    leaderboard_fields = [
        'date', 'model',
        'rh_fold_1', 'rh_fold_5', 'rh_superfamily_1',
        'rh_superfamily_5', 'rh_family_1', 'rh_family_5']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Remote homology prediction results. Results are reported for Fold-level, "
                  "Superfamily-level, and Family-level holdout sets. Each holdout set allows "
                  "for increasing levels of evolutionary similarity, which is reflected in "
                  "the higher performance on the Superfamily and Family-level sets.",
                  model_info)
    return render_template('leaderboard.html', title='Remote Homology - TAPE', table=table)


@app.route('/leaderboard/fluorescence')
def fluorescence():
    leaderboard_fields = [
        'date', 'model',
        'fl_mse_full', 'fl_rho_full', 'fl_mse_bright', 'fl_rho_bright',
        'fl_mse_dark', 'fl_rho_dark']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Fluoresence prediction results for proteins around the GFP protein. Results"
                  " are shown for full dataset, as well as for within the two modes "
                  "(Bright and Dark).",
                  model_info)
    return render_template('leaderboard.html', title='Fluorescence - TAPE', table=table)


@app.route('/leaderboard/stability')
def stability():
    leaderboard_fields = [
        'date', 'model',
        'st_rho', 'st_acc', 'st_aaa_rho', 'st_aaa_acc',
        'st_abba_rho', 'st_abba_acc', 'st_babb_rho', 'st_babb_acc',
        'st_bbabb_rho', 'st_bbabb_acc']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Stability prediction results for a variety of proteins. Results are shown"
                  " for the full dataset, as well as for subsets with specific folds.",
                  model_info)
    return render_template('leaderboard.html', title='Stability - TAPE', table=table)
