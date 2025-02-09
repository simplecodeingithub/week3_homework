
#!/usr/bin/python
from xml.sax.handler import property_interning_dict

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# 1 example
print('the length of string is',len(Belgium))
#  2 example
print('-' *len(Belgium))

Belgium_list = Belgium.split(',')
Belgium_list[1]= int(Belgium_list[1])
Belgium_list[3]= int(Belgium_list[3])
print(Belgium.replace(Belgium, '-'* 81),'\n',('the total population of Belgium + its capital is', Belgium_list[1]+ Belgium_list[3]))

