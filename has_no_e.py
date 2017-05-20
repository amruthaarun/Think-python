def has_no_e(word):
	v=word.find('e')
	if v>=0:
		return False
	else:
		return True
print has_no_e('ammu')
