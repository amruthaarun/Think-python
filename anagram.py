def is_anagram(s1,s2):
	t1=list(s1)
	t2=list(s2)
	t1.sort()
	t2.sort()
	if t1==t2:
		return True
	else:
		return False
s1=raw_input("enter s1\n")
s2=raw_input("enter s2\n")
print is_anagram(s1,s2)
	
