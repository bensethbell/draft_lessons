#Part 1: Experimental Design

Include your answers in ``afternoon_answers.md``.

You are a data scientist at Etsy, a peer-to-peer e-commerce platform.
Your task is to determine if attending local meetups increases a seller's sales.

(**Estimated Time: 30 mins**)

1. What is the problem if we use past sellers' sales and meetup data?

2. What is the generic name for this problem?

3. Outline the steps to design an experiment that would allow us to
determine if local meetups _**causes**_ a seller to sell more?


#Part 2: A / B Testing

Include your answers in ``afternoon_answers.md``.

Include your code in ``ab_test.py``.

Designers at Etsy have created a **new landing page** in an attempt to
improve sign-up rate for local meetups.

The historic sign-up rate for the **old landing page** is 10%.
An improvement to only 10.1% would provide a lift of 1%.
If statistically significant, this would be considered a success.
The product manager will not consider implementing the new page if
the lift is not more or equal to 1%.

Your task is to determine if the new_landing page can provide a 1% or more
lift to sign-up rate.

<br>

1. Design an experiment **to collect data** in order to decide if the new page
   has 0.1% more sign-up rate than the old page? (**_3 bullet points_**)

   (**Estimated Time: 10 mins**)

    - Randomly divert 50% of incoming users to the new page. The rest 50%
      will be directed to the old page.
    - Record the page the user landed on and whether he/she signed up
    - Only allow each user to be recorded once in the whole experiment to
      to ensure the observations are independent

2. State your null hypothesis and alternative hypothesis?

   (**Estimated Time: 5 mins**)

    - <b>H<sub>0</sub></b>: conversion<sub>new</sub> - conversion<sub>old</sub> = 0.001
    - <b>H<sub>1</sub></b>: conversion<sub>new</sub> - conversion<sub>old</sub> &ne; 0.001

3. You ran a pilot experiment according to ``Qu 1.`` for ~40 minutes. The
   collected data is in ``sample.csv``. Import the data into a pandas
   dataframe. **Hint: Write a function to check consistency between ab and
   landing_page columns and duplicate rows. You will need to repeat the same
   procedures later** 

   (**Estimated Time: 30 mins**)

4. Based on the pilot, calculate the minimum sample size required to achieve
   80% power at 0.05 significance level, assuming equal sample size in both
   old page and new page groups. Read ``power_functions.py`` and use the
   ``calc_min_sample()`` function. Estimate how long the whole experiment
   would take if the experiment was to continue to run. 

   (**Estimated Time: 20 mins**)

5. State why running a pilot experiment allows us to more accurately
   determine the minimum sample size required for a certain power. 

   (**Estimated Time: 5 mins**)

   - Running a pilot informs us of a more accurate sign-up rate of the new
     page than guess-work. Subsequently, we are more informed about the sample
     size needed to show statistical signifance of the difference between
     the new and the old page

6. The full experiment was executed as planned to achieve 80% power at 0.5. The
   data is in ``whole.csv``. Import the data and clean it following the same
   steps as in ``Qu 3.``.
   You will find there are some more rows than the expected minimum sample
   size. That is to buffer for rows removed for duplicate users.

   (**Estimated Time: 10 mins**)

7. Calculate the p-value using a z-test.


7. Plot sample size and power. What happens if you change your effect size
two tail instead of one tail



## `country.csv`
* `user_id`: A unique identifier for each user.
* `country`: Country of user.
