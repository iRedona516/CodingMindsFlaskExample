async function getSentiment() {
    // Grab element with id result
    var result = document.getElementById("result")
    
    try{
      // Send a get request to flask server
        var response = await fetch("http://127.0.0.1:5000/sentiment")
      var data = await response.json()
      
      // Display sentiment analysis results
      var sentimentResults = '';
      data.forEach(function(item) {
        sentimentResults += '<p><strong>Quote:</strong> ' + item.quote + '</p>';
        sentimentResults += '<p><strong>Sentiment Analysis:</strong> ' + item.sentiment_analysis + '</p>';
        sentimentResults += '<hr>';
      });
      result.innerHTML = sentimentResults;
      
    } catch(err){
      // Catch any error
      console.log("err", err)
    }
  }


async function rateWalmart() {
    // Grab element with id result
    var scores = document.getElementById("scores")

    var userReview = document.getElementById("userreview").value
    // alert(userReview.value)

    try{
      // Send a get request to flask server
        var response = await fetch("http://127.0.0.1:5000/walmart/" + userReview)
        var data = await response.json()
      
      // Display sentiment analysis results
      var sentimentResults = '';
      data.forEach(function(item) { 
        sentimentResults += '<p><strong>Review:</strong> ' + item.quote + '</p>';
        if (item.score == 0) {
          var sentiment = "Negative Review"
        }
        else {
          var sentiment = "Positive Review"
        }
        sentimentResults += '<p><strong>Sentiment Analysis:</strong> ' + sentiment + '</p>';
        sentimentResults += '<hr>';
      });
      scores.innerHTML = sentimentResults;
      
    } catch(err){
      // Catch any error
      console.log("err", err)
    }
  }

  async function disneylinetime() {
    // Grab element with id result
    var time = document.getElementById("time")

    var disneytime = document.getElementById("disneytime").value
    // alert(disneytime.value)

    try{
      // Send a get request to flask server
        var response = await fetch("http://127.0.0.1:5000/disney/" + disneytime)
        var data = await response.json()
      
      // Display sentiment analysis results
      var timeResults = '';
      data.forEach(function(item) { 
        timeResults += '<p><strong>Time Entered in Line:</strong> ' + item.time_entered + '</p>';
        timeResults += '<p><strong>Predicted Wait Time:</strong> ' + item.time_predicted_in_line + '</p>';
        timeResults += '<hr>';
      });
      time.innerHTML = timeResults;
      
    } catch(err){
      // Catch any error
      console.log("err", err)
    }
  }
  
