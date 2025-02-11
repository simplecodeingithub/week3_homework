
#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# 1 approach
print('the length of string is',len(Belgium))
#  2 approach
print('-' *len(Belgium))

Belgium_list = Belgium.split(',')
# created a list from the variable Belgium to extract singular elements, replaced "," as a separator
Belgium_list[1]= int(Belgium_list[1])
# change the element of the string from a string into a interger
Belgium_list[3]= int(Belgium_list[3])
# once the elements are both integers we  perform an operation (addition) to get the final result
# in one line
print('\n', Belgium.replace(Belgium, '-'* 81),'\n','the total population of Belgium and its capital is', Belgium_list[1]+ Belgium_list[3])
# added a string to make the output more readable


