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


