#to run this: "pip install feedparser" "pip install yahoo-finance"

from yahoo_finance import Share
import feedparser

def getCurrentPrice(Sym):    
	ticker = Share(Sym)
	return ticker.get_price()

def getPercentChange(Sym):
	ticker = Share(Sym)
	return ticker.get_percent_change()

def getNewsTitle(feed):
	return feed['feed']['title']

def getNews(feed, n):
	return feed['entries'][n]['title']

def main():
	ticker_name = raw_input("Enter a Stock Symbol: ")
	feed = feedparser.parse('http://finance.yahoo.com/rss/headline?s=%s' %ticker_name)
	print "The current price of", ticker_name, "is $", getCurrentPrice(ticker_name) , ". This is a", getPercentChange(ticker_name) , "change."
	print "The top headlines for", ticker_name, "from", getNewsTitle(feed), "are: \n\n", getNews(feed, 0), "\n\n", getNews(feed, 1), "\n\n", getNews(feed, 2)

main()