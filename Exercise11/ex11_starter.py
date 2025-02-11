# Shebang (#!) line to specify the Python interpreter (`/usr/bin/python`) for script execution on Unix/Linux systems.
#!/usr/bin/python

# Given String containing data about Belgium.
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# the length of the Belgium string is calculated and multiply the hyphen character by that Length.
print('-' * len(Belgium))

# used replace() to replace the commas with colon in the string.
colon_separated = Belgium.replace(',',':')
print(colon_separated)

# To Calculate the total population of belgium by adding the population of Belgium & the population of its capital city
# split()- Splitting the string into a list
# belgium_list will be a list containing individual elements from the original string.
Belgium_list = Belgium.split(',')
print(Belgium_list)

# Get the population of Belgium from index 1 and convert it to an integer.
population_Belgium = int(Belgium_list[1])
# Get the population of the capital city from index 3 and convert it to an integer.
population_capital_city = int(Belgium_list[3])

# add the population of Belgium and the population of the capital city to get the total population.
print(f"The total population of Belgium is: {population_Belgium + population_capital_city}") # prints the total population.

#print('-' * len(Belgium),"\n", Belgium.replace(',',':'),"\n", Belgium_list, "\n",population_Belgium + population_capital_city)



