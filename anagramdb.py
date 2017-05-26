from anagram_sets import *
import shelve
import sys
def store_anagram(d):
	shelf=shelve.open('anagram.db','c')
	for w in d:
		shelf[w]=d[w]
	#print shelf
	shelf.close()
def read_anagram(word):
	shelf=open('anagram.db','rw')
	w=list(word)
	w.sort()
	w1=''.join(w)
	print w1
	try:
		return shelf[w1]
		shelf.close()
	except KeyError:
		print "word not in shelf"	


	




d = all_anagrams('words.txt')
store_anagram(d)
word=raw_input("enter word to return\n")
print read_anagram(word)
