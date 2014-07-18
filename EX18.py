# -*- coding:utf-8 -*-
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

def print_hello():
    print "def is nice"

#不确定参数个数的时候使用*args
def fun_var_args(farg, *args):  
    print "arg:", farg  
    for value in args:  
        print "another arg:", value 

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
print_hello()
fun_var_args("1","2","3","4")

