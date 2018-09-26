loggedpy
========================================

.. code:: console

  $ python hello.py
  hello hello
  bye

  $ loggedpy hello.py
  INFO	2018-09-24 01:06:56,698	hello hello
  INFO	2018-09-24 01:06:56,698	bye

hello.py

.. code:: python

  def main():
      print("hello hello")
      print("bye")


  if __name__ == "__main__":
      main()

customization
----------------------------------------

.. code:: console

  $ loggedpy --flavor=./customized.py:Flavor hello.py
  INFO	2018-09-24 01:09:12,691	__main__	in	hello.py:2	main	hello hello
  INFO	2018-09-24 01:09:12,691	__main__	in	hello.py:3	main	bye

customized.py

.. code:: python

  import logging
  import loggedpy


  class Flavor(loggedpy.Flavor):
      format = "%(levelname)s\t%(asctime)s\t%(name)s\tin\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s"
      level = logging.DEBUG

support external command
----------------------------------------

.. code:: console

  $ loggedpy-cat hello.py
  def main():
      print("hello hello")
      print("bye")


  if __name__ == "__main__":
      main()

  $ loggedpy --flavor=./customized.py:Flavor loggedpy-cat hello.py
  INFO	2018-09-24 01:12:21,568	loggedpy-cat	in	_cat.py:8	main	def main():
  INFO	2018-09-24 01:12:21,568	loggedpy-cat	in	_cat.py:8	main	    print("hello hello")
  INFO	2018-09-24 01:12:21,568	loggedpy-cat	in	_cat.py:8	main	    print("bye")
  INFO	2018-09-24 01:12:21,568	loggedpy-cat	in	_cat.py:8	main	if __name__ == "__main__":
  INFO	2018-09-24 01:12:21,568	loggedpy-cat	in	_cat.py:8	main	    main()

support `-m`
----------------------------------------


.. code:: console

  $ loggedpy -m tokenize --flavor=./customized.py:Flavor hello.py
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	0,0-0,0:            ENCODING       'utf-8'        
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	1,0-1,3:            NAME           'def'          
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	1,4-1,8:            NAME           'main'         
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	1,8-1,9:            OP             '('            
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	1,9-1,10:           OP             ')'            
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	1,10-1,11:          OP             ':'            
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	1,11-1,12:          NEWLINE        '\n'           
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	2,0-2,4:            INDENT         '    '         
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	2,4-2,9:            NAME           'print'        
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	2,9-2,10:           OP             '('            
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	2,10-2,23:          STRING         '"hello hello"'
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	2,23-2,24:          OP             ')'            
  INFO	2018-09-24 01:10:39,418	tokenize	in	tokenize.py:708	main	2,24-2,25:          NEWLINE        '\n'           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	3,4-3,9:            NAME           'print'        
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	3,9-3,10:           OP             '('            
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	3,10-3,15:          STRING         '"bye"'        
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	3,15-3,16:          OP             ')'            
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	3,16-3,17:          NEWLINE        '\n'           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	4,0-4,1:            NL             '\n'           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	5,0-5,1:            NL             '\n'           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,0-6,0:            DEDENT         ''             
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,0-6,2:            NAME           'if'           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,3-6,11:           NAME           '__name__'     
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,12-6,14:          OP             '=='           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,15-6,25:          STRING         '"__main__"'   
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,25-6,26:          OP             ':'            
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	6,26-6,27:          NEWLINE        '\n'           
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	7,0-7,4:            INDENT         '    '         
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	7,4-7,8:            NAME           'main'         
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	7,8-7,9:            OP             '('            
  INFO	2018-09-24 01:10:39,419	tokenize	in	tokenize.py:708	main	7,9-7,10:           OP             ')'            
  INFO	2018-09-24 01:10:39,420	tokenize	in	tokenize.py:708	main	7,10-7,11:          NEWLINE        '\n'           
  INFO	2018-09-24 01:10:39,420	tokenize	in	tokenize.py:708	main	8,0-8,0:            DEDENT         ''             
  INFO	2018-09-24 01:10:39,420	tokenize	in	tokenize.py:708	main	8,0-8,0:            ENDMARKER      ''             
