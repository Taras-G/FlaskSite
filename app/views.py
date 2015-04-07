from flask import render_template, request
from app import app, models, db

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

@app.route('/breakout', methods=['GET'])
def breakout():
    return render_template('breakout.html')

@app.route('/scores', methods=['GET'])
def scores():
    entries = models.Score.query.all()
    return render_template('scores.html', 
                            entries=entries)


@app.route('/submit', methods=['POST'])
def submit():
    score = models.Score(initials=request.form['initials'], score=request.form['score'])
    db.session.add(score)
    db.session.commit()
    entries = models.Score.query.all()
    return render_template('scores.html', 
                            entries=entries)