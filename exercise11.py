#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
Belgium_list=Belgium.split(",")
print("-"*len(Belgium), "\n", Belgium.replace(",", ":"), "\n", int(Belgium_list[1])+int(Belgium_list[3]), "\n")