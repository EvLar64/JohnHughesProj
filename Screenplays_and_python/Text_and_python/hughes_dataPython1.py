from collections import Counter
from nltk import pos_tag
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
import xml.etree.ElementTree as ET
import re

# JOHN HUGHES PROJECT PYTHON #1 - Data

# importing "stop word" set to be used in finding "unique" script words
stop_words = set(stopwords.words('english'))

# taking in each text file
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

print("SCREENPLAY DATA FROM EACH OF THE THREE MOVIES")
print()

# Sixteen Candles Average Scene/Dialogue Lengths, Character Frequencies

def get_all_text(elem):
    return ''.join(elem.itertext())
# takes in xml directly
tree = ET.parse('sixteen_V2.xml')
root = tree.getroot()
s_scenes = root.findall('.//scene')
s_scene_word_counts = [
    len(get_all_text(scene).split())
    for scene in s_scenes
]
s_dialog = root.findall('.//d')
s_dialog_word_counts = [
    len(get_all_text(d).split())
    for d in s_dialog
]
average_word_count = sum(s_scene_word_counts) / len(s_scene_word_counts) if s_scene_word_counts else 0
print(f"Average word count of scenes in Sixteen Candles - {average_word_count:.2f} words")
average_dialog_word_count = sum(s_dialog_word_counts) / len(s_dialog_word_counts) if s_dialog_word_counts else 0
print(f"Average length of dialogue - {average_dialog_word_count:.2f} words")
chars = root.findall('.//char')
who_list = [char.get('who') for char in chars if char.get('who')]
who_counts = Counter(who_list)
print("Frequencies of character mentions in the script - ")
for who, count in who_counts.items():
    print(f"{who}: {count} times")
print()

# BC Average Scene/Dialogue Lengths

tree = ET.parse('breakfast_V1.xml')
root = tree.getroot()
b_scenes = root.findall('.//scene')
b_scene_word_counts = [
    len(get_all_text(scene).split())
    for scene in b_scenes
]
b_dialog = root.findall('.//d')
b_dialog_word_counts = [
    len(get_all_text(d).split())
    for d in b_dialog
]
average_word_count = sum(b_scene_word_counts) / len(b_scene_word_counts) if b_scene_word_counts else 0
print(f"Average word count of scenes in Breakfast Club - {average_word_count:.2f} words")
average_dialog_word_count = sum(b_dialog_word_counts) / len(b_dialog_word_counts) if b_dialog_word_counts else 0
print(f"Average length of dialogue - {average_dialog_word_count:.2f} words")
chars = root.findall('.//char')
who_list = [char.get('who') for char in chars if char.get('who')]
who_counts = Counter(who_list)
print("Frequencies of character mentions in the script - ")
for who, count in who_counts.items():
    print(f"{who}: {count} times")
print()

# FB Average Scene/Dialogue Length

tree = ET.parse('ferris_V2.xml')
root = tree.getroot()
f_scenes = root.findall('.//scene')
f_scene_word_counts = [
    len(get_all_text(scene).split())
    for scene in f_scenes
]
f_dialog = root.findall('.//d')
f_dialog_word_counts = [
    len(get_all_text(d).split())
    for d in f_dialog
]
average_word_count = sum(f_scene_word_counts) / len(f_scene_word_counts) if f_scene_word_counts else 0
print(f"Average word count of scenes in Ferris Bueller - {average_word_count:.2f} words")
average_dialog_word_count = sum(f_dialog_word_counts) / len(f_dialog_word_counts) if f_dialog_word_counts else 0
print(f"Average length of dialogue - {average_dialog_word_count:.2f} words")
chars = root.findall('.//char')
who_list = [char.get('who') for char in chars if char.get('who')]
who_counts = Counter(who_list)
print("Frequencies of character mentions in the script - ")
for who, count in who_counts.items():
    print(f"{who}: {count} times")
print()

# Frequencies of Different Types of Locations in Each Movie

# uses regex to fix punctuation errors and tagging words as "'S", etc.
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

# shot descriptions and frequencies, using parse on the xml file for the third time

print("Shot Descriptions (and frequencies) within each script:")
print()

print("Ferris Bueller -")
tree = ET.parse('ferris_V2.xml')
root = tree.getroot()
shots = root.findall('.//shot')
shot_list = [shot.text.strip() for shot in shots if shot.text and shot.text.strip()]
shot_counts = Counter(shot_list)
for shot, count in shot_counts.items():
    print(f"{shot}: {count} times")

print()
print("Sixteen Candles -")
tree = ET.parse('sixteen_V2.xml')
root = tree.getroot()
shots = root.findall('.//shot')
shot_list = [shot.text.strip() for shot in shots if shot.text and shot.text.strip()]
shot_counts = Counter(shot_list)
for shot, count in shot_counts.items():
    if shot != "POINT OF VIEW - THE" :
        print(f"{shot}: {count} times")

print()
print("Breakfast Club -")
print( "n/a ")

# Word Data:

# makes text objects from "cleaned-up" versions of words
text_ferris2 = Text(ferris2)
text_sixteen2 = Text(sixteen2)
text_breakfast2 = Text(breakfast2)

print()
print("WORD DATA FROM EACH OF THE THREE MOVIES")

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

# set of common character names and script words that we DON'T want included in this analysis
character_and_scriptWords = ["Ferris", "FERRIS", "ROONEY", "DONG","Dong","Rooney",
                             "JEANIE", "Jeanie", "CAMERON", "Cameron", "SLOANE",
                             "Sloane", "CLAIRE", "Claire", "BRENDA", "Brenda", "JIM",
                             "Jim", "Voice", "BRIAN","Brian","VERNON","Vernon","CARL","Carl",
                             "BENDER","Bender","Allison","ALLISON", "ANDREW", "Andrew",
                             "SAM", "Sam","GEEK", "CAROLINE", "Caroline", "JAKE","Jake",
                             "CONTINUED","CUT","EXT","INT", "CU", "DAY", "NIGHT","VOICE",
                             "Ginny","GINNY", "ROOM", "RANDY", "Randy"]
# lower cases words
filtered_cap_ferris2 = {word.lower() for word in ferris2}
filtered_cap_sixteen2 = {word.lower() for word in sixteen2}
filtered_cap_breakfast2 = {word.lower() for word in breakfast2}

# then takes out any numbers
filtered_num_ferris2 = [word for word in filtered_cap_ferris2 if not word.isdigit()]
filtered_num_sixteen2 = [word for word in filtered_cap_sixteen2 if not word.isdigit()]
filtered_num_breakfast2 = [word for word in filtered_cap_breakfast2 if not word.isdigit()]

# then takes out any stop words
filtered_stop_ferris2 = [word for word in filtered_num_ferris2 if word not in stop_words]
filtered_stop_sixteen2 = [word for word in filtered_num_sixteen2 if word not in stop_words]
filtered_stop_breakfast2 = [word for word in filtered_num_breakfast2 if word not in stop_words]

# then finally takes out any of the previous character/script words
filtered_script_ferris2 = [word for word in filtered_stop_ferris2 if word not in character_and_scriptWords]
filtered_script_sixteen2 = [word for word in filtered_stop_sixteen2 if word not in character_and_scriptWords]
filtered_script_breakfast2 = [word for word in filtered_stop_breakfast2 if word not in character_and_scriptWords]

# counts the words
ferris_unique = Counter(filtered_script_ferris2)
sixteen_unique = Counter(filtered_script_sixteen2)
breakfast_unique = Counter(filtered_script_breakfast2)

# prints the 20 "most common" unique words from the scripts,
# but since many of them are one off uses, it's more of a word-bag
# randomizer for each script
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