#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# splitting the string to make it a list
Belgium_list=Belgium.split(",")
# printing - for the length of belgium string, followed by new line, followed by the string with , replaced by :, newline
# followed by the sum of Belgium and Brussels population made into integers
print("-"*len(Belgium), "\n", Belgium.replace(",", ":"), "\n", int(Belgium_list[1])+int(Belgium_list[3]), "\n")