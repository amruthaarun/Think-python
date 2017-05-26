import os
def walks(dirn):
	for root, dirs, files in os.walk(dirn):
		    for name in files:
			    print (os.path.join(root,name))
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print path
        else:
            walk(path)
walks('/tmp')
walk('/tmp')
