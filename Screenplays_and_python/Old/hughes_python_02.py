# Additional John Hughes Project Python (to be consolidated later) - EL

import os
from nltk import pos_tag
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import PlaintextCorpusReader

cwd = os.getcwd()
filepath = 'hughesColl/breakfast.txt'
f = open(filepath, 'r', encoding='utf8').read()

os.listdir(cwd)
coll = os.path.join(cwd, 'hughesColl')
os.listdir(coll)

for file in os.listdir(coll):
   if file.endswith(".txt"):
        filepath = f"{coll}/{file}"
        print(filepath)
print()
corpus_root = 'hughesColl'
corpus = PlaintextCorpusReader(corpus_root, '.*')
corpus.fileids()

# adjective counter and adjective list variables created
# (which will get added upon as the scripts are passed through)
adjective_count = 0
adjectives = []

for file in corpus.fileids():
    hughesContent = corpus.raw(file)
    words = word_tokenize(hughesContent)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        # adjective codes sourced from the internet
        if tag in ['JJ', 'JJR', 'JJS']:
            adjective_count += 1
            adjectives.append(word)

adjective_freq = FreqDist(adjectives)
print(f"Total number of adjectives in the corpus (all three scripts): {adjective_count} ")
print()
print("The 50 most common adjectives used in the three screenplays are:")
hughes_common_adj = adjective_freq.most_common(50)
print(hughes_common_adj)
print()

# does a similar thing to the adjectives above, but this time it also sorts them and creates
# a unique set with them
verb_count = 0
verbs = []
for file in corpus.fileids():
    hughesContent = corpus.raw(file)
    hughesWords = word_tokenize(hughesContent)
    tagged_words = pos_tag(hughesWords)
    for word, tag in tagged_words:
        if tag in ['VB'] :
            # special circumstance because capital words (even non-verbs) were
            # also being included
            if word.islower() :
                verb_count += 1
                verbs.append(word)

print("The total verb count across all three screenplays:")
print(verb_count)
print("The set of unique verbs present throughout all of the three project screenplays:")
print(sorted(set(verbs)))

print("Most frequent bigrams:")
print()
# needs a little editing to account for punctuation and those types of things
for file in corpus.fileids():
    hughesContent = corpus.raw(file)
    words = word_tokenize(hughesContent)
    bigramFinder = BigramCollocationFinder.from_words(words)
    bigrams = bigramFinder.nbest(BigramAssocMeasures.likelihood_ratio, 10)
    for bigram in bigrams:
        print(bigram)

filepath1 = 'hughesColl/sixteen.txt'
sixteen = open(filepath1, 'r', encoding='utf8').read()
filepath2 = 'hughesColl/ferris.txt'
ferris = open(filepath2, 'r', encoding='utf8').read()
filepath3 = 'hughesColl/breakfast.txt'
breakfast = open(filepath3, 'r', encoding='utf8').read()

sixteenwords = word_tokenize(sixteen)
ferriswords = word_tokenize(ferris)
breakfastwords = word_tokenize(breakfast)

# making a speech counter and graph showing frequencies of
# different parts of speech (in Ferris Bueller)
f_pos_counts = Counter()
ferris_tagged = pos_tag(ferriswords)
for word, tag in ferris_tagged:
    if tag.startswith('NN'):
        f_pos_counts['Noun'] += 1
    elif tag.startswith('VB'):
        f_pos_counts['Verb'] += 1
    elif tag.startswith('JJ'):
        f_pos_counts['Adjective'] += 1

plt.figure()
plt.bar(f_pos_counts.keys(), f_pos_counts.values(), color=['blue', 'red', 'yellow'])
plt.title('Frequency of Nouns, Verbs, and Adjectives within Ferris Bueller')
plt.ylabel('Count')

# same thing for Breakfast Club
b_pos_counts = Counter()
breakfast_tagged = pos_tag(breakfastwords)
for word, tag in breakfast_tagged:
    if tag.startswith('NN'):
        b_pos_counts['Noun'] += 1
    elif tag.startswith('VB'):
        b_pos_counts['Verb'] += 1
    elif tag.startswith('JJ'):
        b_pos_counts['Adjective'] += 1

plt.figure()
plt.bar(b_pos_counts.keys(), b_pos_counts.values(), color=['green', 'orange', 'purple'])
plt.title('Frequency of Nouns, Verbs, and Adjectives within Breakfast Club')
plt.ylabel('Count')

# same thing for Sixteen Candles
s_pos_counts = Counter()
sixteen_tagged = pos_tag(sixteenwords)
for word, tag in sixteen_tagged:
    if tag.startswith('NN'):
        s_pos_counts['Noun'] += 1
    elif tag.startswith('VB'):
        s_pos_counts['Verb'] += 1
    elif tag.startswith('JJ'):
        s_pos_counts['Adjective'] += 1

plt.figure()
plt.bar(s_pos_counts.keys(), s_pos_counts.values(), color=['grey', 'teal', 'black'])
plt.title('Frequency of Nouns, Verbs, and Adjectives within Sixteen Candles')
plt.ylabel('Count')
plt.show()