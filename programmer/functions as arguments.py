#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16ece015
#
# Created:     21/10/2017
# Copyright:   (c) 16ece015 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list = ['GUVI', 'learning', 'is', 'awesome', 'always']
def foo(x):
     print x * 3


def my_map_simple(fun, list):
     for item in list:
         fun(item)


my_map_simple(foo, list)
