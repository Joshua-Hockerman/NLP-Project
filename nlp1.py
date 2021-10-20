from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)

# print(blob.sentences)

# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)

# print(blob.sentiment)

# print(round(blob.sentiment.polarity), 3)
# print(round(blob.sentiment.subjectivity, 3))

# sentences = blob.sentences

# for sentence in sentences:
#     print(sentence)
#     print(round(sentence.sentiment.polarity, 3))


from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

# for sentence in blob.sentences:
#     print(sentence.sentiment)

# spanish = blob.translate(to="es")

# print(spanish)

# print(spanish.translate(to="en"))


from textblob import Word

# index = Word("index")

# print(index.pluralize())

# cacti = Word("cacti")

# print(cacti.singularize())

# word list

# animals = TextBlob(
#     "dog cat fish otter dodo tiger turkey fly shark turtle hippo penguin"
# ).words

# print(animals.pluralize())

# Spellcheck and correction

# word = Word("theyr")

# print(word.spellcheck())

# print(word.correct())

# word1 = Word("studies")
# ord2 = Word("varieties")

# print(word1.stem())
# print(word2.stem())

# print(word1.lemmatize())
# print(word2.lemmatize())


happy = Word("happy")

# print(happy.definitions)

# print(happy.synsets)

for s in happy.synsets:
    for lemma in s.lemmas():
        print(lemma.name())

synonym = happy.synsets[1].lemmas()[0].name()

print(synonym)


antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()

print(antonym)
