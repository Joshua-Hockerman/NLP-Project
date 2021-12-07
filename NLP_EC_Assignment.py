from textblob import TextBlob
from pathlib import Path
import matplotlib.pyplot as plt

new_blob = TextBlob(Path("panini_tweet_replies.txt").read_text())

sentence_sentiment = []

for line in new_blob.sentences:
    sentiment = line.sentiment.polarity
    sentence_sentiment.append(sentiment)

plt.hist(sentence_sentiment)

plt.xlabel("Comment Polarity")
plt.ylabel("Number of Replies")
plt.title("Histogram of Tweet Reply Sentiment")

plt.show()
