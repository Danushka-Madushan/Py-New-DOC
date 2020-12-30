import sys

try:
	X= sys.argv[1]
except Exception:
	print("\n$ Usage : Python New {FileName.Extension}")
	sys.exit()
NEW_DOC = open(X, 'w')
NEW_DOC.close()
print(f"\n$ Created Document : [ {X} ]")
sys.exit()
