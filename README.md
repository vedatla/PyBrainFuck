PyBrainFuck
===========

An interpreter for brainfuck written in python.

Usage
=====
* If no command line argument is supplied, the program will run in the
  interactive mode.
  * Type "r" on an empty line, to reset the tape and set the program counter
    to zero.
  * Type ";" on an empty line, to get your code evaluated.
  * Type "q" on an empty line to quit the program.
* If the first argument is a "-", the program will read stdin, and evaluate
  it.
* Else: Every supplied command line argument will be interpreted in the order
  they were supplied.

License Info
============
Copyright (c) 2012, Vedat Levi Alev

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

