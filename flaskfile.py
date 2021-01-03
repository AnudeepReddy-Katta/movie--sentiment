from flask import Flask, render_template, request
import pickle
import numpy as np
import sqlite3 as sql
import preprocess


model = pickle.load(open('pipline.pkl', 'rb'))

app = Flask('__name__')

@app.route('/')
def base():
    return render_template('layout.html')

@app.route('/home.html')
def home():
    return render_template('layout.html')

@app.route('/result',methods=['POST'])
def results():

    features = request.form.get('review')
    preprocessed=preprocess.review_cleaner(features)
    prediction = model.predict([preprocessed])
    if prediction == 1:
        sentiment = 'positive'
    elif prediction == 0:
        sentiment = 'negative'
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO movie_review (review,sentiment) VALUES (?,?)",
                        (features, sentiment))
            con.commit()
    except :
        con.rollback()
    finally :
        con.close()
    return render_template('/result.html', features=features,sentiment=sentiment)

@app.route('/data.html')
def show_data():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from movie_review")

    rows = cur.fetchall()  # returns list of dictionaries
    return render_template("data.html", rows=rows)


if __name__ == '__main__' :
    app.run()
