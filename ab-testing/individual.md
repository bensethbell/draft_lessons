##Part 1: Hypothesis testing recap
Include the answers in ``morning_answers.md``

1. State which test should be used for the following scenarios.
   a.
   b.
   c.
   d.

2. What is a p-value?

3. What is Type I and Type II error?

   What is the Type I error if the p-value is 0.002

4.


##Part 2: Analyzing Click Through Rate
We will use hypothesis testing to analyze **Click Through Rate (CTR)** on New York Times website.
CTR is defined as the number of clicks the user make per impression that is made upon the user.
We are going to determine if there is statistically significant difference between the mean CTR of
the following groups:
```
1. Signed in users v.s. Not signed in users
2. Male v.s. Female
3. 6 age groups
```

1. Load ``data/nyt1.csv`` in a pandas dataframe.

   Use ``data.info()`` to make sure the datatypes are valid and there are no null values.
   This data has been cleaned for you, but generally it is good practice to check for those.

2. We will compare the **Click Through Rate (CTR)** of the users later in the sprint. Make a new column
   ``CTR`` using the ``Impressions`` and the ``Clicks`` columns. Remember to remove the rows with ``0``
   impressions.

3. Plot the distribution of each column in the dataframe. Do that using ``data.hist()``.
   Check out the argments you can use with the function
   (here)[http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html].
   Set the ``figsize=(12,5)`` to make sure the graph is decipherable.

4. Make 2 dataframes separating the rows where the users are signed in and are not signed.
   Plot the distributions of the columns in each of the dataframes. By visually inspecting
   the two sets of distributions, what are the differences between users who are signed in and not
   signed in?

5. Use a Welch t-test to determine if the mean CTR between the signed-in users
   and the non-signed-in users is statistically different.

   The Welch t-test assume the two populations the samples are drawn have
   different variances.

   ```python
   scipy.stats.ttest_ind(a, b, equal_var=False)
   ```
6.

- Plot distributions of all columns
- Plot the columns for signed in and not signed in
- Realize there is no gender / age for people who are not signed in
- Get rid of the people who are not signed in
- Compute CTR column
- Compare mean CTR for male and female (male = 0, female=1)
- Compare mean CTR for different age groups
- Compare mean CTR for Signed in or not sign it
- Multiple testing, if not adjusted, what percent do we expect to be false discovery

- Is any one group significantly different from the rest
