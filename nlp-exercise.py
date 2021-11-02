from textblob import TextBlob
import nltk


from pathlib import Path
from wordcloud import WordCloud
import imageio


# nltk.download("stopwords")
from nltk.corpus import stopwords

from operator import itemgetter

stops = stopwords.words("english")

new_blob = TextBlob(Path("book of John text.txt").read_text())

more_stops = [
    "thy",
    "ye",
    "thee",
    "hath",
    "verily",
    "say",
    "thou",
    "art",
    "shall",
    "unto",
    "said",
    "therefore",
    "saith",
    "man",
    "one",
    "things",
    "come",
    "world",
    "answered",
    "came",
    "may",
    "disciples",
    "son",
    "also",
    "went",
    "sent",
    "cometh",
    "life",
    "lord",
    "go",
    "even",
    "witness",
    "yet",
    "given",
    "see",
    "word",
    "heard",
    "spake",
    "made",
    "hast",
    "many",
    "truth",
    "believed",
    "saying",
    "day",
    "knew",
    "light",
    "name",
    "us",
    "hour",
    "give",
    "water",
    "works",
    "feast",
    "take",
    "love",
    "might",
    "seen",
    "saw",
    "called",
    "forth",
    "would",
    "another",
    "bear",
    "true",
]

stops += more_stops

items = new_blob.word_counts.items()

clean_items = [word for word in items if word[0] not in stops]


sorted_items = sorted(clean_items, key=itemgetter(1), reverse=True)

text = sorted_items[:15]


print(text[1][0])

text_only = ""

"""
Testing for making a wordcloud based on how often the words appear, will continue to 
work on it later.  Current loop satisfies assignment requirements.

for i in range(len(text)):

    new_word = text[i][0]

    n = 0

    while n < int(text[i][1]):
        text_only = text_only + new_word + " "

        n += 1
"""

for i in range(len(text)):
    text_only = text_only + text[i][0] + " "


mask_image = imageio.imread("mask_oval.png")

wordcloud = WordCloud(colormap="Blues", mask=mask_image, background_color="grey")

wordcloud = wordcloud.generate(text_only)

wordcloud = wordcloud.to_file("Book_of_John_Word_Cloud.png")

print("Done")
