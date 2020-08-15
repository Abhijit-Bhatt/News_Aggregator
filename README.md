# News_Aggregator
A News Aggregator

News Aggregator site using NewsAPI to pull News articles from external sources based off of keywords. NewsAPI sends us the relevant data in JSON format. Our application backend is currently implemented on a flask server. It parses the data sent to us from NewsAPI and renders each article onto a card and displays on a single page. We also currently have a basic UI designed in Flask that allows users to pass parameters to NewsAPI. Additionally, we allow users to filter by news source.

In the future, we'd like to move our frontend to Angular and have it communicate with our backend Flask server in a RESTful way. We'd also like to connect our flask server to a database that would mainly be used to save articles as well as preferences (i.e. automate what news sources NewsAPI pulls from on login based on user inputted parameters). This also means we will add some basic authentication.
