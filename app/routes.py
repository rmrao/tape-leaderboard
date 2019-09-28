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
    leaderboard_fields = ['date', 'model', 'ss_cb513_3', 'ss_casp12_3', 'ss_ts115_3', 'ss_cb513_8']
    table = Table(leaderboard_fields,
                  [public_names[fn] for fn in leaderboard_fields],
                  "Overall Results on TAPE Benchmark Tasks.",
                  model_info)
    return render_template('leaderboard.html', title='Leaderboard - TAPE', table=table)
