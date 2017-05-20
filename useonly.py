def use_only(word,letter):
	index=0
	for char in letter:
			index=word.find(char)
			if index==-1:
				return False
	return True
word=raw_input("enter word\n")
print use_only(word,'acefhlo')
