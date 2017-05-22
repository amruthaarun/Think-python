def capitalize_nested(t):
	res=[]
	for i in t:
		res.append(capitalize_all(i))
	print res

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

t=[['a','b'],['b','c'],['c','d']]
capitalize_nested(t)
