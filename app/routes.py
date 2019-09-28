from flask import render_template
from app import app
import csv
from pathlib import Path

data_dir = Path(__file__).parent / 'data'

with (data_dir / 'results.csv').open() as f:
    reader = csv.reader(f)
    fieldnames = next(reader)
    public_names = next(reader)
    model_info = [dict(zip(fieldnames, info_line)) for info_line in reader]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Tasks Assessing Protein Embeddings - TAPE')


@app.route('/leaderboard')
def leaderboard():
    leaderboard_fields = ['model', 'date', 'secondary_structure', 'contact_prediction',
                          'remote_homology', 'fluorescence', 'stability']
    return render_template('leaderboard.html', title='Leaderboard - TAPE')
