#!/usr/bin/env python

"""
a simple (and not neccesarily efficient) brainfuck interpreter
If called with no additional command line arguments, goes in the interactive
mode.
If the first argument is a "-", program reads stdin and evaluates it.
Else, program reads all arguments and evaluates them.
"""

import sys

##
# primitive ::= { . | , | < | > | + | - }
# program   ::= primitive | "[" program "]"
##

# simulate the tape with a dict
tape = [0]*(3*10**4 + 1)

# the data pointer
ptr   = 0

# the simple brainfuck commands

def lt():
    """ performs a < """
    global ptr
    if ptr == 0:
        raise ValueError, "Segmentation fault!"
    ptr -= 1

def gt():
    """" performs a > """
    global ptr
    if ptr == 3*10**4:
        raise ValueError, "Segmentation fault!"
    ptr += 1

def plus():
    """ performs a + """
    global ptr
    tape[ptr] = (tape[ptr] + 1) % 256

def minus():
    """ perfoms a - """
    global ptr
    tape[ptr] = (tape[ptr] - 1) % 256

def dot():
    """ performs a . """
    global ptr
    sys.stdout.write(chr(tape[ptr]))

def comma():
    """ performs a , """
    global ptr
    c = ord(sys.stdin.read(1))
    if c != 26:
        tape[ptr] = c

# primitives which can directly be handled
handle_directly = { "." : dot, "," : comma, "<" : lt, ">" : gt, "+" : plus, "-" : minus}


def parse(code):
    # stack to contain the indices of the opening brackets
    opening = []
    # dict which maps the indices of the opening brackets to the closing
    # brackets
    loop    = {}
    for i,c in enumerate(code):
        if c == "[":
            opening.append(i)
        elif c == "]":
            try:
                begin = opening.pop()
                loop[begin] = i
            except IndexError:
                raise ValueError, "Supplied string isn't balanced, too many ]s!"
    # if the stack isn't empty, the string cannot be balanced
    if opening != []:
        raise ValueError, "Supplied string isn't balanced, too many [s"
    else:
        return loop

#def eval_bf(code):
#    global ptr
#    loop = parse(code)
#    def eval_part(start, end):
#        not_done = False
#        for pc in range(start, end):
#            c = code[pc]
#            if c in handle_directly:
#                apply(handle_directly[c])
#            elif c == "[":
#                not_done = True
#                break
#        if not_done:
#            loop_end = loop[pc]
#            while tape[ptr]:
#                eval_part(pc+1,loop_end)
#            eval_part(loop_end, end)
#    eval_part(0, len(code))


def eval_bf(code):
    global ptr
    # get the scopes of the "[", "]"s
    loop  = parse(code)
    # initialize a variable for the program counter
    pc    = 0
    # a stack to store the pc for loops
    stack = []
    while pc < len(code):
        instruction = code[pc]
        # handle the primitives directly
        if instruction in handle_directly:
            apply(handle_directly[instruction])
        elif instruction == "[":
            # if loop condition is fullfiled
            # enter loop block
            if tape[ptr] > 0:
                stack.append(pc)
            else: # else go to the end of the block
                pc = loop[pc]
        elif instruction == "]":
            # jump back where you came from!
            pc = stack.pop() - 1
        pc += 1


def reset():
    global ptr, tape
    ptr = 0
    tape = [0] * (3*10**4 + 1)

def interactive():
    print """Welcome to the Brainfuck Interpreter.
    Magical commands: (if the last command wasn't a ',')
    \tType ";" on an empty line to get your program evaluated.
    \tType "r" on an empty line to reset the tape
    \tType "q" on an empty line to quit"""
    code = ""
    last = ""
    while True:
        line = str(raw_input("> "))
        if last != ",":
            if line == "r":
                reset()
                continue
            elif line == ";":
                try:
                    sys.stdout.write("\n")
                    eval_bf(code)
                    sys.stdout.write("\n")
                    continue
                except Exception, message:
                    print message
                    print "Something went wrong, let's take it from the top!"
                    reset()
                code = ""
            elif line == "q":
                return
        code += line


if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive()
    elif sys.argv[1] == "-":
        code = sys.stdin.read()
        eval_bf(code)
    else:
        for fd in sys.argv[1:]:
            with open(fd, "r") as f:
                code = f.read()
            eval_bf(code)
