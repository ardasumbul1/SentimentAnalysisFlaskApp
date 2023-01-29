from flask import Flask,render_template
from flask import request
from flask import jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from forms import getText


app = Flask(__name__)

@app.route("/")
def form():
    return render_template('mainpage.html')

@app.route("/",methods=['POST'])
def get_score():
    text = request.form['text']
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    if(score["compound"] >0 and score["compound"] <=1 ):
        result = "positive"
    elif(score["compound"] <0 and score["compound"] >=-1 ):
        result = "negative"
    elif(score["compound"]==0):
        result = "neutral"
    return render_template("mainpage.html",variable=result)

if __name__ == "__main__":
    app.run(debug=True)