import pandas as pd
from z_test import z_test
from power_functions import ProportionPower

########################
###### Question 3 ######
########################
# Read in the csv into a pandas dataframe
data = pd.read_csv('data/experiment.csv')

# Discover the old/new landing page label does not always match
# the control/treatment label
print 'ab column counts:'
print data['ab'].value_counts()
print 'landing_page column counts:'
print data['landing_page'].value_counts()

# Find out the rows where the landing page / control-treatment
# labels are mismatched
def find_mismatch(ab_cell, landing_page_cell):
    if ab_cell == 'treatment' and landing_page_cell == 'new_page':
        return 0
    elif ab_cell == 'control' and landing_page_cell == 'old_page':
        return 0
    else:
        return 1

# Function that will be applied to the 2 columns
func = lambda row: find_mismatch(row['ab'], row['landing_page'])

# Define a mismatch column where 0 is ok, and 1 is mismatched
print 'Dropping treatment / control and landing page mismatch...'
# axis=1 means iterate the rows in the dataframe
data['mismatch'] = data.apply(func, axis=1)

# Get the percent mismatched
mismatched = data[data['mismatch'] == 1]
percent = (len(mismatched) / (len(data['mismatch']) * 1.) * 100)
print 'Percentage mismatched:', percent

# Dropping rows that are mismatched
data = data[data['mismatch'] == 0]

########################
###### Question 4 ######
########################

# Get the parameters needed for z_test()

old = data[data['landing_page'] == 'old_page']
new = data[data['landing_page'] == 'new_page']
old_nrow = old.shape[0] * 1.
new_nrow = new.shape[0] * 1.
old_convert = old[old['converted'] == 1].shape[0]
new_convert = new[new['converted'] == 1].shape[0]
old_conversion = old_convert / old_nrow
new_conversion = new_convert / new_nrow

# These are the arguments that z_test() takes:
# old_conversion, new_conversion, old_nrow, new_nrow,
# effect_size=0., two_tailed=True, alpha=.05
# The running z_test() will print out the results
z_test(old_conversion, new_conversion,
       old_nrow, new_nrow,
       effect_size=0.001, two_tailed=False, alpha=.05)


########################
###### Question 5 ######
########################

# Parameters for ProportionPower()
# p_samc, p_samt, effect_size, alpha=.05, power=None,
# total=None, two_tailed=True
nrow = old_nrow + new_nrow
p_power = ProportionPower(old_conversion, new_conversion,
                          effect_size=.001, alpha=.05, power=.8,
                          total=nrow, two_tailed=False)

# Calculate minimum sample size
print 'Minimum Sample: ', p_power.calc_min_sample()

# Calculate power of the pilot
print 'Power of the pilot:', p_power.calc_power()

