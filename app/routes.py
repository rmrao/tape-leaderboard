from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Tasks Assessing Protein Embeddings - TAPE')


@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', title='Leaderboard - TAPE')
