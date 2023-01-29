from flask import Flask,render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_score(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    if(score["compound"] >0 and score["compound"] <=1 ):
        return "positive"
    elif(score["compound"] <0 and score["compound"] >=-1 ):
        return "negative"
    elif(score["compound"]==0):
        return "neutral"



app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("mainpage.html")

if __name__ == "__main__":
    app.run(debug=True)