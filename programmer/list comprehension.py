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

def main():
 S = [x**2 for x in range(10)]
 V = [2**i for i in range(13)]
 M = [x for x in S if x % 2 == 0]
 print S;
 print V;
 print M

if __name__ == '__main__':
    main()
