import nltk
import matplotlib.pyplot as plt
from nltk import pos_tag
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.text import Text
import numpy as np

# JOHN HUGHES PROJECT WORD DATA W/ PYTHON - EL

# Takes in each screenplay text file
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

# frequency distributions made for each script
fdist_ferris = FreqDist(text_ferris1)
fdist_sixteen = FreqDist(text_sixteen1)
fdist_breakfast = FreqDist(text_breakfast1)

# concordance for a different word within each of the scripts
print()
print("Concordance of the word 'school' within the script for Ferris Bueller:")
text_ferris1.concordance("school")
print()
print("Concordance of the word 'birthday' within the script for Sixteen Candles:")
text_sixteen1.concordance("birthday")
print()
print("Concordance of the word 'detention' within the script for Breakfast Club:")
text_breakfast1.concordance("detention")
print()

# displays the 10 most common verbs in all three
print("10 most common verbs in Ferris Bueller:")
tagged_ferris = pos_tag(ferris1)
ferrisverbs = [word for word, tag in tagged_ferris if tag.startswith('VB')]
ferris_verbs = FreqDist(ferrisverbs)
ferris_common_verbs = ferris_verbs.most_common(10)
print(ferris_common_verbs)
print()

print("10 most common verbs in Sixteen Candles:")
tagged_sixteen = pos_tag(sixteen1)
sixteenverbs = [word for word, tag in tagged_sixteen if tag.startswith('VB')]
sixteen_verbs = FreqDist(sixteenverbs)
sixteen_common_verbs = sixteen_verbs.most_common(10)
print(sixteen_common_verbs)
print()

print("10 most common verbs in Breakfast Club:")
tagged_breakfast = pos_tag(breakfast1)
breakfastverbs = [word for word, tag in tagged_breakfast if tag.startswith('VB')]
breakfast_verbs = FreqDist(breakfastverbs)
breakfast_common_verbs = breakfast_verbs.most_common(10)
print(breakfast_common_verbs)
print()

# lexical richness as defined
# also rounding each number to three significant digits using f strings
print("Lexical Richness = Unique Words / Total Words")
print("Richness of Ferris Bueller:")
print(f"{(len(set(ferris1)) / len(ferris1)):.3f}")
print("Richness of Sixteen Candles:")
print(f"{(len(set(sixteen1)) / len(sixteen1)):.3f}")
print("Richness of Breakfast Club:")
print(f"{(len(set(breakfast1)) / len(breakfast1)):.3f}")

# makes specific words to find EXT. and INT. location frequency specifically,
# then counts them in Ferris Bueller
ferrisEXT = 'EXT.'
ferrisINT = 'INT.'
int_count = ferris.count(ferrisINT)
ext_count = ferris.count(ferrisEXT)

# prints the data before creating and outputting a pie chart
# comparing the frequencies of each type of location in the movie
print()
print(f"There are {int_count} '{ferrisINT}' locations in Ferris Bueller.")
print(f"There are {ext_count} '{ferrisEXT}' locations in Ferris Bueller.")
print()
plt.figure(1)
plt.title('Interior vs. Exterior Locations in Ferris Bueller')
y = np.array([int_count, ext_count])
loclabels = ["Interior Locations", "Exterior Locations"]
plt.pie(y, labels = loclabels)

# makes a set of strings as names from breakfast club (the most common ones)
# counts the mentions of each name in the screenplay and also plots this data
# on a bar graph
breakfast_characters = ['Allison', 'Andrew', 'Vernon', 'Bender', 'Brian', 'Claire']
name_counts = {name: breakfast1.count(name) for name in breakfast_characters}
plt.figure(2)
plt.bar(name_counts.keys(), name_counts.values())
plt.xlabel('Characters')
plt.ylabel('Screenplay Mentions')
plt.title('Frequency of Main Character Mentions in Breakfast Club')
plt.show()