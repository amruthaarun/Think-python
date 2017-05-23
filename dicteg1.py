def dict_eg(f,s):
	fin=open(f)
	i=0
	word_dict=dict()
	for l in fin:
		for word in l.split():
			word_dict[word]=i
			i=i+1
	print word_dict
	if s in word_dict:
		return True
	return False
print dict_eg('word.txt','arun')

