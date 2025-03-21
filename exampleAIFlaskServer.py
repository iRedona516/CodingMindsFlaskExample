from flask import Flask, jsonify
from flask_cors import CORS
import requests
from textblob import TextBlob
from bs4 import BeautifulSoup
from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

app = Flask(__name__)
CORS(app)

@app.route("/sentiment")
def get_sentiment_analysis():
  # Grab text from quotes web page
  data = requests.get("http://quotes.toscrape.com/tag/inspirational/")

  # Add contents
  data_scraping = BeautifulSoup(data.content, "html.parser")
  spans = data_scraping.select(".text")

  # Initialize empty list to store sentiment analysis results
  sentiment_analysis_results = []

  # Loop through the data and perform sentiment analysis
  for span in spans:
    quote = TextBlob(span.text)
    quoteScore = round(quote.sentiment.polarity, 2)

    sentiment_analysis_results.append({
      "quote": span.text,
      "sentiment_analysis": quoteScore,
    })

  # Return all sentiment analysis results
  return jsonify(sentiment_analysis_results)

@app.route("/user_sentiment/<quote>")
def get_user_sentiment(quote):
    user_sentiment_result = {}
    
    # Dictionary example
    # student: {"student_id": 8439043,
    #           "name": "Isiah Redona",
    #           "age": 25,
    #           "name": [NOT ALLOWED, KEYS MUST BE UNIQUE]}
    
    user_sentiment_result["quote"] = quote
    textblob_quote = TextBlob(quote)
    user_sentiment_result["score"] = round(textblob_quote.sentiment.polarity, 2)
    
    return jsonify(user_sentiment_result)

@app.route("/ice_cream_sales_calc/<temperature>")
def predict_icecream_sales(temperature):
    # Input data
    temperature = int(temperature)
    temperatures_2d = [
        [1, 62], 
        [1, 71], 
        [1, 65], 
        [1, 60], 
        [1, 58], 
        [1, 53], 
        [1, 49], 
        [1, 46], 
        [1, 50],
        [1, 42]
    ]
    
    # Output data
    ice_cream_sold = [80, 91, 78, 74, 72, 68, 61, 59, 63, 52]
    
    model = linear_model.LinearRegression()
    model.fit(temperatures_2d, ice_cream_sold)
    sales_prediction = model.predict([[1, temperature]])
    
    icecream_sales_prediction = {
      "user temperature": temperature,
      "predicted sales": sales_prediction[0]
    }
    
    return jsonify(icecream_sales_prediction)
  
@app.route("/wait_time_calc/<time>")
def calculate_wait_time(time):
  time = float(time)
  input_data = [
    [9],
    [10],
    [11],
    [12],
    [13],
    [14],
    [15],
    [16],
  ]

  output_data = [0,10,20,30,40,30,20,10]
  model = make_pipeline(PolynomialFeatures(2), Ridge())
  model.fit(input_data, output_data)
  
  wait_prediction = model.predict([[time]])
  wait_time = {
    "time" : time,
    "wait prediction" : wait_prediction[0]
  }
  
  return jsonify(wait_time)
  
app.run(host = '0.0.0.0')
