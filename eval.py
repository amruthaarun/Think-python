def eval_loop():
	s=raw_input("enter string to evaluate\n")
	while s!='done':
		print eval(s)
		s=raw_input("enter string to evaluate\n")
	return s

print eval_loop()
