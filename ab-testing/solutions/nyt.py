
# coding: utf-8

# In[185]:

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
from itertools import combinations
get_ipython().magic(u'matplotlib inline')


# In[209]:

# significance adjusted for multiple testing
alpha = 0.05 / 23


# In[71]:

data = pd.read_csv('data/nyt1.csv')


# In[72]:

data.info()


# In[99]:

data = data[data['Impressions'] != 0]
data['CTR'] = data['Clicks'] / data['Impressions'].astype(float)


# In[110]:

def plot_hist(df, title, color):
    df.hist(figsize=(12, 5), grid=False, normed=True, color=color, alpha=.2)
    # suptitle to place a title in the center of the figure
    # x,y to adjust where the title is placed
    plt.suptitle(title, size=18, weight='bold', y=1.05)


# In[111]:

plot_hist(data, 'Overall', 'b')


# In[112]:

signin_data = data[data['Signed_In'] == 1]
notsignin_data = data[data['Signed_In'] == 0]
plot_hist(signin_data, 'Signed In', 'g')
plot_hist(notsignin_data, 'Not Signed In', 'r')


# In[214]:

def t_test(gp1_df, gp2_df, gp1_name, gp2_name, filename):
    fig = plt.figure()
    gp1_mean = gp1_df['CTR'].mean()
    gp2_mean = gp2_df['CTR'].mean()

    print '%s Mean CTR: %s' % (gp1_name, gp1_mean)
    print '%s Mean CTR: %s' % (gp2_name, gp2_mean)
    print 'diff in mean:' , abs(gp2_mean - gp1_mean)
    p_val = scs.ttest_ind(gp1_df['CTR'], gp2_df['CTR'], equal_var=False)[1]
    print 'p value is:', p_val

    gp1_df['CTR'].hist(normed=True, label=gp1_name, color='g', alpha=0.3)
    gp2_df['CTR'].hist(normed=True, label=gp2_name, color='r', alpha=0.3)
    plt.axvline(gp1_mean, color='r', alpha=0.6, lw=2)
    plt.axvline(gp2_mean, color='g', alpha=0.6, lw=2)

    plt.ylabel('Probability Density')
    plt.xlabel('CTR')
    plt.legend()
    plt.grid('off')
    plt.savefig(filename)


# In[215]:

t_test(signin_data, notsignin_data, 'Signed In', 'Not Signed In', 'signin_ttest.png')


# In[216]:

male = signin_data[signin_data['Gender'] == 1]
female = signin_data[signin_data['Gender'] == 0]
t_test(male, female, 'M', 'F', 'female_ttest.png')


# In[203]:

signin_data['age_groups'] = pd.cut(signin_data['Age'], [7, 18, 24, 34, 44, 54, 64, 1000])


# In[217]:

signin_data['age_groups'].value_counts().sort_index().plot(kind='bar', grid=False)
plt.xlabel('Age Group')
plt.ylabel('Number of users')
plt.savefig('age_gp_freq.png')


# In[207]:

results = pd.DataFrame()
combos = combinations(pd.unique(signin_data['age_groups']), 2)
for age1, age2 in combos:
    ctr1 = signin_data[signin_data['age_groups'] == age1]['CTR']
    ctr2 = signin_data[signin_data['age_groups'] == age2]['CTR']
    p_val = scs.ttest_ind(ctr1, ctr2, equal_var=False)[1]
    ctr1_mean = ctr1.mean()
    ctr2_mean = ctr2.mean()
    diff = abs(ctr1_mean - ctr2_mean)
    results = results.append(dict(one=age1, two=age2,
                                  mean1=ctr1_mean, mean2=ctr2_mean,
                                  diff=diff, p=p_val), ignore_index=True)
results = results[['one', 'two', 'mean1', 'mean2', 'diff', 'p']]


# In[223]:

results[results['p'] < alpha].sort('diff', ascending=False)


# In[222]:

results[results['p'] > alpha].sort('diff', ascending=True)

