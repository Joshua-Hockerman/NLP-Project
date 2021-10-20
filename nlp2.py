from textblob import TextBlob
import nltk


from pathlib import Path
import pandas as pd

# nltk.download("stopwords")
from nltk.corpus import stopwords

stops = stopwords.words("english")

# print(stops)

# blob = TextBlob("Today is a beautiful day.")

# print(blob.words)

# cleanlist = [word for word in blob.words if word not in stops]

# print(cleanlist)

new_blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

# print(new_blob.words.count("joy"))

# print(new_blob.word_counts["juliet"])

more_stops = ["thee", "thou", "thy"]

stops += more_stops

items = new_blob.word_counts.items()

clean_items = [item for item in items if item[0] not in stops]

# print(clean_items[:10])

from operator import itemgetter

sorted_items = sorted(clean_items, key=itemgetter(1), reverse=True)

print(sorted_items[:20])

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns=["Word", "Count"])

import matplotlib.pyplot as plt

df.plot.bar(x="Word", y="Count", legend=False, color=["y", "c", "m", "b", "g"])

plt.gcf().tight_layout()

plt.show()
