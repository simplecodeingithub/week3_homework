
#!/usr/bin/python
from xml.sax.handler import property_interning_dict

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'


print('the lenght of string is',len(Belgium))
print(Belgium.replace(Belgium, '-'* 81))

Belgium_list = Belgium.split(',')
Belgium_list[1]= int(Belgium_list[1])
Belgium_list[3]= int(Belgium_list[3])
print('the total population of Belgium + its capital is', Belgium_list[1]+ Belgium_list[3])

