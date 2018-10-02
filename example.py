# Welcome to the iPython notebook tutorial!

# You can write some Python code here and run it with Shift-Enter.
# The result of your last line of code gets printed out,
# so no more need for `print` statements!

x = 5
y = 3
x + y

# iPython remembers the variables you've used before.
x * y

# You can make functions too!

def square(x):
    return x * x

square(12)

# You can go back and edit a previous line, too.
# Can you turn the previous function `square` into `cube`?

# Let's play around with a real dataset.

# It's a best practice to import all your required packages up here.

import csv

# This is a handy recipe for turning a CSV into a 
# list of dictionaries - which are like structs in C
# or objects in JavaScript, if you're familiar with those.

concentration_data = []

with open('concentration-enrollment.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['concentration'])
        # You can't just do `concentration_data = reader`
        # because the `reader` object disappears once the file
        # is read. Instead, you want to copy each row into
        # a different list.
        concentration_data.append(row)

# Let's see what we got
concentration_data

# We can now start crunching the numbers!

# Let's just see what the first piece of data looks like
# Each year corresponds with the number of concentrators in that concentration
# in that year.
aaas = concentration_data[0]

# Ew, it looks like the enrollment numbers are strings, not integers!
# That makes it harder to run calculations.
# Let's clean up this data.

def clean_concentration(raw):
    return dict([
        ('concentration', raw['concentration']),
        ('2010-11', int(raw['2010-11'])),
        ('2011-12', int(raw['2011-12'])),
        ('2012-13', int(raw['2012-13'])),
        ('2013-14', int(raw['2013-14'])),
        ('2014-15', int(raw['2014-15']))
    ])

clean_concentration(aaas)

# That's better! Let's clean all the concentrations, then

clean_concentration_data = [clean_concentration(c) for c in concentration_data]

clean_concentration_data[3]

# Let's see how many concentrators Computer Science added from 2010-2015.
# This is a trick to filter a list
computer_science = [c for c in clean_concentration_data if c['concentration'] == 'Computer Science'][0]
computer_science

#####
# Now it's your turn to start working with the data!
#####

# Calculate the growth in CS concentrators from 2010-11 to 2014-15. 
new_cs_concentrators = 0 # CHANGE ME
growth_percent = 0 # CHANGE ME

"CS added {} concentrators, for a growth rate of {} percent!".format(new_cs_concentrators, growth_percent)

# Hey, that was cool. Why don't we do that for every concentration?

def summary_for_concentration(concentration):
    # Replace this with code that returns something like the above
    # ("CS added...") for any given concentration
    pass


for c in clean_concentration_data:
    print summary_for_concentration(c)

# Things to do next:
# - Print the 5 largest concentrations.
# - Print the 5 fastest-growing concentrations.
# - Add the growth rate to each concentration's dict.
# - Write a new CSV that includes the growth rate for each concentration.

# If you're feeling ambitious:
# - Use matplotlib to make a graph.