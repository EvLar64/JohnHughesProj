from collections import Counter
from nltk import pos_tag
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words('english'))

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

# Sixteen Candles Average Scene Length
# BC Average Scene Length
# FB Average Scene Length
# SC Average Dialogue Length
# BC Average Dialogue Length
# FB Average Dialogue Length

# Frequencies of Different Types of Locations in Each Movie

ferris2 = re.findall(r"\b\w+(?:'\w+)?\b", ferris)
breakfast2 = re.findall(r"\b\w+(?:'\w+)?\b", breakfast)
sixteen2 = re.findall(r"\b\w+(?:'\w+)?\b", sixteen)

ferrisEXT = 'EXT.'
ferrisINT = 'INT.'
int_count = ferris.count(ferrisINT)
ext_count = ferris.count(ferrisEXT)
print("Frequencies of different locations in each movie:")
print()
print(f"There are {int_count} '{ferrisINT}' locations in Ferris Bueller.")
print(f"There are {ext_count} '{ferrisEXT}' locations in Ferris Bueller.")
print(f"Total = {int_count + ext_count}")
print()

breakfastEXT = 'EXT.'
breakfastINT = 'INT.'
int_count = breakfast.count(breakfastINT)
ext_count = breakfast.count(breakfastEXT)
print(f"There are {int_count} '{breakfastINT}' locations in Breakfast Club.")
print(f"There are {ext_count} '{breakfastEXT}' locations in Breakfast Club.")
print(f"Total = {int_count + ext_count}")
print()

sixteenEXT = 'EXT.'
sixteenINT = 'INT.'
int_count = sixteen.count(sixteenINT)
ext_count = sixteen.count(sixteenEXT)
print(f"There are {int_count} '{sixteenINT}' locations in Sixteen Candles.")
print(f"There are {ext_count} '{sixteenEXT}' locations in Sixteen Candles.")
print(f"Total = {int_count + ext_count}")
print()

# Word Data:
text_ferris2 = Text(ferris2)
text_sixteen2 = Text(sixteen2)
text_breakfast2 = Text(breakfast2)

# Concordance examples of different words for each movie
print()
print("Concordance of the word 'school' within the script for Ferris Bueller:")
text_ferris2.concordance("school", lines=10)
print()
print("Concordance of the word 'birthday' within the script for Sixteen Candles:")
text_sixteen2.concordance("birthday", lines=10)
print()
print("Concordance of the word 'essay' within the script for Breakfast Club:")
text_breakfast2.concordance("essay", lines=10)
print()

# Lexical Richness of all three scripts
print("Lexical Richness = Unique Words / Total Words")
print("Richness of Ferris Bueller:")
print(f"{(len(set(ferris2)) / len(ferris2)):.4f}")
print("Richness of Sixteen Candles:")
print(f"{(len(set(sixteen2)) / len(sixteen2)):.4f}")
print("Richness of Breakfast Club:")
print(f"{(len(set(breakfast2)) / len(breakfast2)):.4f}")

# 20 instances of "unique" words in each script, with script words, stop words, and digits removed
character_and_scriptWords = ["Ferris", "FERRIS", "ROONEY", "DONG","Dong","Rooney",
                             "JEANIE", "Jeanie", "CAMERON", "Cameron", "SLOANE",
                             "Sloane", "CLAIRE", "Claire", "BRENDA", "Brenda", "JIM",
                             "Jim", "Voice", "BRIAN","Brian","VERNON","Vernon","CARL","Carl",
                             "BENDER","Bender","Allison","ALLISON", "ANDREW", "Andrew",
                             "SAM", "Sam","GEEK", "CAROLINE", "Caroline", "JAKE","Jake",
                             "CONTINUED","CUT","EXT","INT", "CU", "DAY", "NIGHT","VOICE",
                             "Ginny","GINNY", "ROOM", "RANDY", "Randy"]
filtered_cap_ferris2 = {word.lower() for word in ferris2}
filtered_cap_sixteen2 = {word.lower() for word in sixteen2}
filtered_cap_breakfast2 = {word.lower() for word in breakfast2}

filtered_num_ferris2 = [word for word in filtered_cap_ferris2 if not word.isdigit()]
filtered_num_sixteen2 = [word for word in filtered_cap_sixteen2 if not word.isdigit()]
filtered_num_breakfast2 = [word for word in filtered_cap_breakfast2 if not word.isdigit()]

filtered_stop_ferris2 = [word for word in filtered_num_ferris2 if word not in stop_words]
filtered_stop_sixteen2 = [word for word in filtered_num_sixteen2 if word not in stop_words]
filtered_stop_breakfast2 = [word for word in filtered_num_breakfast2 if word not in stop_words]

filtered_script_ferris2 = [word for word in filtered_stop_ferris2 if word not in character_and_scriptWords]
filtered_script_sixteen2 = [word for word in filtered_stop_sixteen2 if word not in character_and_scriptWords]
filtered_script_breakfast2 = [word for word in filtered_stop_breakfast2 if word not in character_and_scriptWords]

ferris_unique = Counter(filtered_script_ferris2)
sixteen_unique = Counter(filtered_script_sixteen2)
breakfast_unique = Counter(filtered_script_breakfast2)

ferris_top20 = ferris_unique.most_common(20)
sixteen_top20 = sixteen_unique.most_common(20)
breakfast_top20 = breakfast_unique.most_common(20)

print()
print("20 instances of 'unique' words within each script (after removing script words, 'stop' words, and numbers):")
print("Ferris Bueller -")
print(sorted(ferris_top20))
print()
print("Sixteen Candles -")
print(sorted(sixteen_top20))
print()
print("Breakfast Club -")
print(sorted(breakfast_top20))
print()

# Part of Speech Data
print("Part of Speech Data for Each Screenplay:")
print("Verbs")
print("10 most common verbs in Ferris Bueller -")
tagged_ferris = pos_tag(ferris2)
ferrisverbs = [word for word, tag in tagged_ferris if tag.startswith('VB')]
ferris_verbs = FreqDist(ferrisverbs)
ferris_common_verbs = ferris_verbs.most_common(10)
print(ferris_common_verbs)
print("Total number of unique verbs -")
print(len(set(ferrisverbs)))
print("10 most common verbs in Sixteen Candles -")
tagged_sixteen = pos_tag(sixteen2)
sixteenverbs = [word for word, tag in tagged_sixteen if tag.startswith('VB')]
sixteen_verbs = FreqDist(sixteenverbs)
sixteen_common_verbs = sixteen_verbs.most_common(10)
print(sixteen_common_verbs)
print("Total number of unique verbs -")
print(len(set(sixteenverbs)))
print("10 most common verbs in Breakfast Club -")
tagged_breakfast = pos_tag(breakfast2)
breakfastverbs = [word for word, tag in tagged_breakfast if tag.startswith('VB')]
breakfast_verbs = FreqDist(breakfastverbs)
breakfast_common_verbs = breakfast_verbs.most_common(10)
print(breakfast_common_verbs)
print("Total number of unique verbs -")
print(len(set(breakfastverbs)))
print()

print("Adjectives")
print("10 most common adjectives in Ferris Bueller -")
ferrisadj = [word for word, tag in tagged_ferris if tag.startswith('JJ')]
ferris_adj = FreqDist(ferrisadj)
ferris_common_adj = ferris_adj.most_common(10)
print(ferris_common_adj)
print("Total number of unique adjectives -")
print(len(set(ferrisadj)))
print("10 most common adjectives in Sixteen Candles -")
sixteenadj = [word for word, tag in tagged_sixteen if tag.startswith('JJ')]
sixteen_adj = FreqDist(sixteenadj)
sixteen_common_adj = sixteen_adj.most_common(10)
print(sixteen_common_adj)
print("Total number of unique adjectives -")
print(len(set(sixteenadj)))
print("10 most common adjectives in Breakfast Club -")
breakfastadj = [word for word, tag in tagged_breakfast if tag.startswith('JJ')]
filtered_breakfast_adj = [item for item in breakfastadj if item != 'Brian']
breakfast_adj = FreqDist(filtered_breakfast_adj)
breakfast_common_adj = breakfast_adj.most_common(10)
print(breakfast_common_adj)
print("Total number of unique adjectives -")
print(len(set(breakfastadj)))
print()

print("Prepositions")
print("10 most common prepositions in Ferris Bueller -")
ferrisprep = [word for word, tag in tagged_ferris if tag.startswith('IN')]
ferris_prep = FreqDist(ferrisprep)
ferris_common_prep = ferris_prep.most_common(10)
print(ferris_common_prep)
print("Total number of unique prepositions -")
print(len(set(ferrisprep)))
print("10 most common prepositions in Sixteen Candles -")
sixteenprep = [word for word, tag in tagged_sixteen if tag.startswith('IN')]
sixteen_prep = FreqDist(sixteenprep)
sixteen_common_prep = sixteen_prep.most_common(10)
print(sixteen_common_prep)
print("Total number of unique prepositions -")
print(len(set(sixteenprep)))
print("10 most common prepositions in Breakfast Club -")
breakfastprep = [word for word, tag in tagged_breakfast if tag.startswith('IN')]
breakfast_prep = FreqDist(breakfastprep)
breakfast_common_prep = breakfast_prep.most_common(10)
print(breakfast_common_prep)
print("Total number of unique prepositions -")
print(len(set(breakfastprep)))