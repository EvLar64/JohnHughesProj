import matplotlib.pyplot as plt
from nltk.text import Text
from nltk import pos_tag
from nltk import word_tokenize
import numpy as np
import re

# JOHN HUGHES PROJECT PYTHON #2 - Visualizations

# takes in each txt file
with open("ferris.txt",'r') as file:
    ferris=file.read()
with open("sixteen.txt",'r') as file:
    sixteen=file.read()
with open("breakfast.txt",'r') as file:
    breakfast=file.read()

# tokenizes and creates a text object with each script
ferris1 = word_tokenize(ferris)
text_ferris1 = Text(ferris1)
sixteen1 = word_tokenize(sixteen)
text_sixteen1 = Text(sixteen1)
breakfast1 = word_tokenize(breakfast)
text_breakfast1 = Text(breakfast1)

# filters out punctuation errors in word sets
ferris2 = re.findall(r"\b\w+(?:'\w+)?\b", ferris)
breakfast2 = re.findall(r"\b\w+(?:'\w+)?\b", breakfast)
sixteen2 = re.findall(r"\b\w+(?:'\w+)?\b", sixteen)
text_ferris2 = Text(ferris2)
text_breakfast2 = Text(breakfast2)
text_sixteen2 = Text(sixteen2)

# tags words for parts of speech (pos_tag library)
tagged_ferris = pos_tag(ferris2)
tagged_breakfast = pos_tag(breakfast2)
tagged_sixteen = pos_tag(sixteen2)

# tags verbs (VB)
ferrisverbs = [word for word, tag in tagged_ferris if tag.startswith('VB')]
sixteenverbs = [word for word, tag in tagged_sixteen if tag.startswith('VB')]
breakfastverbs = [word for word, tag in tagged_breakfast if tag.startswith('VB')]

# tags adjectives (JJ)
ferrisadj = [word for word, tag in tagged_ferris if tag.startswith('JJ')]
sixteenadj = [word for word, tag in tagged_sixteen if tag.startswith('JJ')]
breakfastadj = [word for word, tag in tagged_breakfast if tag.startswith('JJ')]

# tags prepositions (IN)
ferrisprep = [word for word, tag in tagged_ferris if tag.startswith('IN')]
sixteenprep = [word for word, tag in tagged_sixteen if tag.startswith('IN')]
breakfastprep = [word for word, tag in tagged_breakfast if tag.startswith('IN')]

# Lexical Dispersion for words pertaining to emotion in the three movies
emotion_words = [
    'love', 'hate', 'anger', 'joy', 'fear', 'sadness', 'happiness',
    'hope', 'desire', 'regret', 'frustration', 'guilt', 'relief',
    'loneliness', 'excitement', 'confusion', 'ashamed', 'pride',
    'envy', 'guilt', 'disappointment', 'embarrassment', 'jealousy',
    'grief', 'euphoria', 'sympathy', 'serenity', 'anxiety', 'contentment'
]

# counting INT/EXT locations in each movie
ferrisEXT = 'EXT.'
ferrisINT = 'INT.'
ferris_int_count = ferris.count(ferrisINT)
ferris_ext_count = ferris.count(ferrisEXT)
breakfastEXT = 'EXT.'
breakfastINT = 'INT.'
breakfast_int_count = breakfast.count(breakfastINT)
breakfast_ext_count = breakfast.count(breakfastEXT)
sixteenEXT = 'EXT.'
sixteenINT = 'INT.'
sixteen_int_count = sixteen.count(sixteenINT)
sixteen_ext_count = sixteen.count(sixteenEXT)

# created color sets
colors1 = ['#FF6EC7', '#00FFFF']
colors2 = ['#FF00FF', '#98FF98']
colors3 = ['#FFFF66', '#9B30FF']
colors4 = ['#006C5B','#FF6B00']

# pie charts comparing INT/EXT locations in each movie
plt.figure(1)
plt.title('Interior vs. Exterior Locations in Ferris Bueller',  fontweight='bold')
y = np.array([ferris_int_count, ferris_ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels, colors=colors1, wedgeprops={'edgecolor': 'orange', 'linewidth': 1.5})

plt.figure(2)
plt.title('Interior vs. Exterior Locations in Breakfast Club', fontweight='bold')
y = np.array([breakfast_int_count, breakfast_ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels, colors=colors2, wedgeprops={'edgecolor': 'red', 'linewidth': 1.5})

plt.figure(3)
plt.title('Interior vs. Exterior Locations in Sixteen Candles', fontweight='bold')
y = np.array([sixteen_int_count, sixteen_ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels, colors=colors3, wedgeprops={'edgecolor': 'green', 'linewidth': 1.5})

# bar graph of character mentions in Breakfast Club specifically
breakfast_characters = ['Allison', 'Andrew', 'Vernon', 'Bender', 'Brian', 'Claire']
name_counts = {name: breakfast1.count(name) for name in breakfast_characters}
plt.figure(4)
plt.bar(name_counts.keys(), name_counts.values(), color=colors2, edgecolor='black', linewidth=2)
plt.xlabel('Characters')
plt.ylabel('Screenplay Mentions')
plt.title('Frequency of Main Character Mentions in Breakfast Club', fontweight='bold')

# using regex, found :
# lines of dialogue by Ferris
ferrisLines = 298
# Ferris lines spoken to the camera
ferris_fourthWallLines = 39

# bar graph of Ferris parts of speech
movies = ['Verbs', 'Adjectives', 'Prepositions']
frequencies1 = [len(ferrisverbs), len(ferrisadj), len(ferrisprep)]
plt.figure(5)
plt.bar(movies, frequencies1, color='#FF8C42', edgecolor='black', linewidth=2)
plt.xlabel('Part of Speech')
plt.ylabel('Frequencies')
plt.title('Part of Speech Use in Ferris Bueller', fontweight='bold')

# bar graph of Breakfast Club parts of speech
frequencies2 = [len(breakfastverbs), len(breakfastadj), len(breakfastprep)]
plt.figure(6)
plt.bar(movies, frequencies2, color='#D46A6A', edgecolor='black', linewidth=2)
plt.xlabel('Part of Speech')
plt.ylabel('Frequencies')
plt.title('Part of Speech Use in Breakfast Club', fontweight='bold')

# bar graph of Sixteen Candles parts of speech
frequencies3 = [len(sixteenverbs), len(sixteenadj), len(sixteenprep)]
plt.figure(7)
plt.bar(movies, frequencies3, color='#F5DEB3', edgecolor='black', linewidth=2)
plt.xlabel('Part of Speech')
plt.ylabel('Frequencies')
plt.title('Part of Speech Use in Sixteen Candles', fontweight='bold')

# dialogue counts in breakfast club
brian_d = 121
andrew_d = 140
claire_d = 154
allison_d = 71
bender_d = 213
vernon_d = 87
carl_d = 21
misc_d = 8
# breakfast dialogue total = 815
breakfast_totald = (brian_d + andrew_d + claire_d + allison_d + bender_d + vernon_d + carl_d + misc_d)

# Breakfast Club dialogue pie chart
plt.figure(8)
plt.title('Breakfast Club: Dialogue Breakdown',  fontweight='bold')
y = np.array([brian_d, andrew_d, claire_d, allison_d, bender_d, vernon_d, carl_d, misc_d])
charlabels = ["Brian", "Andrew", "Claire", "Allison", "Bender", "Vernon", "Carl", "Misc."]
d_labels = ["121 Lines", "140 Lines", "154 Lines", "71 Lines", "213 Lines", "87 Lines", "21 Lines", "8 Lines"]
plt.pie(y, labels = d_labels, colors=colors1+colors2+colors3+colors4, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
plt.legend(charlabels, title="Characters", bbox_to_anchor=(1.2, 0.6))

# Lexical Dispersion plots for words pertaining to emotion
text_ferris2.dispersion_plot(emotion_words)
plt.figure(9)
plt.title('Lexical Dispersion of 80s Slang Words in Ferris Bueller', fontweight='bold')

text_breakfast2.dispersion_plot(emotion_words)
plt.figure(10)
plt.title('Lexical Dispersion of 80s Slang Words in Breakfast Club', fontweight='bold')

text_sixteen2.dispersion_plot(emotion_words)
plt.figure(11)
plt.title('Lexical Dispersion of 80s Slang Words in Sixteen Candles', fontweight='bold')

plt.show()