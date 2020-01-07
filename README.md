# Simple Vector implementation in python 

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
a = Vector([0, 1, 2, 3])
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Operations:
- Addition with a scalar `a+1`
- Vector addition: `a + b`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache . 
```

## Travis build badge:

$ git clone --depth=50 --branch=master https://github.com/TomasZilinek/open-source-development-course-hw02-1.git TomasZilinek/open-source-development-course-hw02-1

Cloning into 'TomasZilinek/open-source-development-course-hw02-1'...

remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 37 (delta 8), reused 17 (delta 5), pack-reused 16
Receiving objects: 100% (37/37), 8.48 KiB | 4.24 MiB/s, done.
Resolving deltas: 100% (8/8), done.

$ cd TomasZilinek/open-source-development-course-hw02-1
$ git checkout -qf 8d38774612e9b66e4424877b024a0b9905e617f4
$ source ~/virtualenv/python3.6/bin/activate
$ python --version
Python 3.6.7

$ pip --version
pip 19.0.3 from /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/pip (python 3.6)

$ python --version
Python 3.6.7

$ pip install unittest2
$ cd ossdev/tests
$ python vct_test.py

Traceback (most recent call last):

  File "vct_test.py", line 7, in <module>

    from ossdev import Vector

ModuleNotFoundError: No module named 'ossdev'

The command "python vct_test.py" exited with 1.

Done. Your build exited with 1.


## Supported operations:
  - adding, subtracting, XOR, getting lengt ...
