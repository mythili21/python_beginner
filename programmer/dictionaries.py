#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      16ece015
#
# Created:     21/10/2017
# Copyright:   (c) 16ece015 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 mydict = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
 print "Cost of apple is " + str(mydict["apples"])
 mydict["apples"] = 800
 print "New Cost of apple is " + str(mydict["apples"])

if __name__ == '__main__':
    main()
