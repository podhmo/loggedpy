00:
	loggedpy 00*.py
01:
	loggedpy 01*.py
02:
	loggedpy loggedpy-cat customized.py
03:
	loggedpy -m tokenize customized.py
04:
	loggedpy --loggedpy-driver=./customized.py:Driver 00*.py
05:
	loggedpy --loggedpy-driver=./customized.py:Driver 01*.py
06:
	loggedpy --loggedpy-driver=./customized.py:Driver loggedpy-cat customized.py
07:
	loggedpy --loggedpy-driver=./customized.py:Driver -m tokenize customized.py

