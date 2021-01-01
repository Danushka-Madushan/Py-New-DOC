import sys

try:
	Y = sys.argv[2 or 3 or 4 or 5 or 6 or 7 or 8 or 9]
	if Y:
		print("\n$ Usage : New.py {FileName.Extension}")
		sys.exit()

except Exception:
	try:
		X = sys.argv[1]
		if X:
			NEW_DOC = open(X, 'w')
			NEW_DOC.close()
			print(f"\n$ Created Document : [ {X} ]")
			sys.exit()

	except Exception:
		print("\n$ Usage : New.py {FileName.Extension}")
		sys.exit()
