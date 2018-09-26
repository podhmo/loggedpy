## 00

```console
$ loggedpy 00*.py
INFO	2018-09-24 00:58:59,494	hello
```

## 01

```console
$ loggedpy 01*.py
INFO	2018-09-24 00:59:19,711	hello
INFO	2018-09-24 00:59:19,711	hello
INFO	2018-09-24 00:59:19,711	hello
```

## 02

```console
$ loggedpy loggedpy-cat customized.py
INFO	2018-09-24 00:59:33,000	import logging
INFO	2018-09-24 00:59:33,000	import loggedpy
INFO	2018-09-24 00:59:33,000	class Flavor(loggedpy.Flavor):
INFO	2018-09-24 00:59:33,000	    format = "%(levelname)s\t%(asctime)s\t%(name)s\tin\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s"
INFO	2018-09-24 00:59:33,000	    level = logging.DEBUG
```

## 03

```console
$ loggedpy -m tokenize customized.py
INFO	2018-09-24 01:00:10,578	0,0-0,0:            ENCODING       'utf-8'        
INFO	2018-09-24 01:00:10,578	1,0-1,6:            NAME           'import'       
INFO	2018-09-24 01:00:10,578	1,7-1,14:           NAME           'logging'      
INFO	2018-09-24 01:00:10,578	1,14-1,15:          NEWLINE        '\n'           
INFO	2018-09-24 01:00:10,578	2,0-2,6:            NAME           'import'       
INFO	2018-09-24 01:00:10,578	2,7-2,15:           NAME           'loggedpy'     
INFO	2018-09-24 01:00:10,578	2,15-2,16:          NEWLINE        '\n'           
INFO	2018-09-24 01:00:10,578	3,0-3,1:            NL             '\n'           
INFO	2018-09-24 01:00:10,578	4,0-4,1:            NL             '\n'           
INFO	2018-09-24 01:00:10,578	5,0-5,5:            NAME           'class'        
INFO	2018-09-24 01:00:10,578	5,6-5,12:           NAME           'Flavor'       
INFO	2018-09-24 01:00:10,578	5,12-5,13:          OP             '('            
INFO	2018-09-24 01:00:10,578	5,13-5,21:          NAME           'loggedpy'     
INFO	2018-09-24 01:00:10,578	5,21-5,22:          OP             '.'            
INFO	2018-09-24 01:00:10,579	5,22-5,28:          NAME           'Flavor'       
INFO	2018-09-24 01:00:10,579	5,28-5,29:          OP             ')'            
INFO	2018-09-24 01:00:10,579	5,29-5,30:          OP             ':'            
INFO	2018-09-24 01:00:10,579	5,30-5,31:          NEWLINE        '\n'           
INFO	2018-09-24 01:00:10,579	6,0-6,4:            INDENT         '    '         
INFO	2018-09-24 01:00:10,579	6,4-6,10:           NAME           'format'       
INFO	2018-09-24 01:00:10,579	6,11-6,12:          OP             '='            
INFO	2018-09-24 01:00:10,579	6,13-6,107:         STRING         '"%(levelname)s\\t%(asctime)s\\t%(name)s\\tin\\t%(filename)s:%(lineno)s\\t%(funcName)s\\t%(message)s"'
INFO	2018-09-24 01:00:10,579	6,107-6,108:        NEWLINE        '\n'           
INFO	2018-09-24 01:00:10,579	7,4-7,9:            NAME           'level'        
INFO	2018-09-24 01:00:10,579	7,10-7,11:          OP             '='            
INFO	2018-09-24 01:00:10,579	7,12-7,19:          NAME           'logging'      
INFO	2018-09-24 01:00:10,579	7,19-7,20:          OP             '.'            
INFO	2018-09-24 01:00:10,579	7,20-7,25:          NAME           'DEBUG'        
INFO	2018-09-24 01:00:10,579	7,25-7,26:          NEWLINE        '\n'           
INFO	2018-09-24 01:00:10,579	8,0-8,0:            DEDENT         ''             
INFO	2018-09-24 01:00:10,579	8,0-8,0:            ENDMARKER      ''             
```

## 04

```console
$ loggedpy --flavor=./customized.py:Flavor 00*.py
INFO	2018-09-24 01:00:27,195	__main__	in	00hello.py:1	<module>	hello
```

## 05

```console
$ loggedpy --flavor=./customized.py:Flavor 01*.py
INFO	2018-09-24 01:00:36,634	__main__	in	01hello.py:2	hello	hello
INFO	2018-09-24 01:00:36,634	__main__	in	01hello.py:2	hello	hello
INFO	2018-09-24 01:00:36,634	__main__	in	01hello.py:2	hello	hello
```

## 06

```console
$ loggedpy --flavor=./customized.py:Flavor loggedpy-cat customized.py
INFO	2018-09-24 01:00:47,985	loggedpy-cat	in	_cat.py:8	main	import logging
INFO	2018-09-24 01:00:47,985	loggedpy-cat	in	_cat.py:8	main	import loggedpy
INFO	2018-09-24 01:00:47,985	loggedpy-cat	in	_cat.py:8	main	class Flavor(loggedpy.Flavor):
INFO	2018-09-24 01:00:47,985	loggedpy-cat	in	_cat.py:8	main	    format = "%(levelname)s\t%(asctime)s\t%(name)s\tin\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s"
INFO	2018-09-24 01:00:47,985	loggedpy-cat	in	_cat.py:8	main	    level = logging.DEBUG
```

## 07

```console
$ loggedpy --flavor=./customized.py:Flavor -m tokenize customized.py
INFO	2018-09-24 01:01:02,738	tokenize	in	tokenize.py:708	main	0,0-0,0:            ENCODING       'utf-8'        
INFO	2018-09-24 01:01:02,738	tokenize	in	tokenize.py:708	main	1,0-1,6:            NAME           'import'       
INFO	2018-09-24 01:01:02,738	tokenize	in	tokenize.py:708	main	1,7-1,14:           NAME           'logging'      
INFO	2018-09-24 01:01:02,738	tokenize	in	tokenize.py:708	main	1,14-1,15:          NEWLINE        '\n'           
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	2,0-2,6:            NAME           'import'       
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	2,7-2,15:           NAME           'loggedpy'     
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	2,15-2,16:          NEWLINE        '\n'           
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	3,0-3,1:            NL             '\n'           
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	4,0-4,1:            NL             '\n'           
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	5,0-5,5:            NAME           'class'        
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	5,6-5,12:           NAME           'Flavor'       
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	5,12-5,13:          OP             '('            
INFO	2018-09-24 01:01:02,739	tokenize	in	tokenize.py:708	main	5,13-5,21:          NAME           'loggedpy'     
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	5,21-5,22:          OP             '.'            
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	5,22-5,28:          NAME           'Flavor'       
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	5,28-5,29:          OP             ')'            
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	5,29-5,30:          OP             ':'            
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	5,30-5,31:          NEWLINE        '\n'           
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	6,0-6,4:            INDENT         '    '         
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	6,4-6,10:           NAME           'format'       
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	6,11-6,12:          OP             '='            
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	6,13-6,107:         STRING         '"%(levelname)s\\t%(asctime)s\\t%(name)s\\tin\\t%(filename)s:%(lineno)s\\t%(funcName)s\\t%(message)s"'
INFO	2018-09-24 01:01:02,740	tokenize	in	tokenize.py:708	main	6,107-6,108:        NEWLINE        '\n'           
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	7,4-7,9:            NAME           'level'        
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	7,10-7,11:          OP             '='            
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	7,12-7,19:          NAME           'logging'      
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	7,19-7,20:          OP             '.'            
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	7,20-7,25:          NAME           'DEBUG'        
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	7,25-7,26:          NEWLINE        '\n'           
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	8,0-8,0:            DEDENT         ''             
INFO	2018-09-24 01:01:02,741	tokenize	in	tokenize.py:708	main	8,0-8,0:            ENDMARKER      ''             
```
