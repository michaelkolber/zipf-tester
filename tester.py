# This Python file uses the following encoding: utf-8

import re

verses = []
verses_by_word = []

with open('output_no_extra.txt') as output_file:
    output = output_file.read()
    verses = re.split(r'\n', output)
    for verse in verses:
        verses_by_word.append(re.split(r' |־', verse))
    
    longest_verse = [0,0]
    current_verse = 0
    for verse in verses:
        if len(verse) > len(verses[longest_verse[0]]):
            longest_verse[1] = longest_verse[0]
            longest_verse[0] = current_verse
        elif len(verse) == len(verses[longest_verse[0]]):
            longest_verse[1] = current_verse
        current_verse += 1
        
    longest_verse_by_word = [0,0]
    current_verse_by_word = 0
    for verse in verses_by_word:
        if len(verse) > len(verses_by_word[longest_verse_by_word[0]]):
            longest_verse_by_word[1] = longest_verse_by_word[0]
            longest_verse_by_word[0] = current_verse_by_word
        elif len(verse) == len(verses_by_word[longest_verse_by_word[0]]):
            longest_verse_by_word[1] = current_verse_by_word
        current_verse_by_word += 1
        
print "Longest line: " + str(longest_verse[0]) + ". Second-longest line: " + str(longest_verse[1])
print "Longest line by words: " + str(longest_verse_by_word[0]) + ". Second-longest line by words: " + str(longest_verse_by_word[1])
print len(verses_by_word[16])
print verses_by_word[16]