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
    - <b>H<sub>1</sub></b>: conversion<sub>new</sub> - conversion<sub>old</sub> > 0.001

3. You ran a pilot experiment according to ``Qu 1.`` for ~1 day. The
   collected data is in ``experiment.csv``. Import the data into a pandas
   dataframe.

   **Hint: Write a function to check consistency between ab and
   landing_page columns and duplicate rows.**

   (**Estimated Time: 20 mins**)

   ``See answer in ab_test.py``

4. State a rationale for using a one-tailed z-test of a two-tailed z-test.
   Calculate a p-value for a 0.1% lift from using the new page compare to the
   old page. Fill in ``z_test()`` in ``ab_test.py`` to execute the z-test.

   Based on the p-value alone, explain your decision to adopt the
   new page or not.

   - One tailed z-test is used because we will only adopt the new page if the
     lift is larger than 0.1% with statistical significance. Otherwise, we keep
     the old page. We don't need the lift to be signigicant lower than 0.1% to
     abandon the new page and keep the old
   - p-value: 0.244060255972. Based on the p-value alone, the lift is not
     significantly larger than 0.1%. The null is not rejected, and the new
     page is not adopted

5. Based on the pilot, calculate the minimum sample size required to achieve
   80% power at 0.05 significance level, assuming equal sample size in both
   old page and new page groups. Read the doc string in ``power_functions.py``.

   Use ``calc_min_sample()`` function to calculate the minimum sample required
   to get 80% power at 0.05 significance level. Subsequently, calculate the
   approximate time needed to run the experiment based on the number of user
   in the pilot.

   Use ``calc_power()`` to calculate the power of the pilot. Interpret what the
   power means. Is the power enough to draw any conclusions?

   (**Estimated Time: 20 mins**)

   ```
   For 80% power at 0.05 significance level:
    - Minimum requred sample size: 1201311
    - Approx. required time: 8.2 days
    - Current power: 0.252200577093
    - Interpretation: There is only 16.3% chance of detecting any statisitcally
      significant difference from 0.1% between the old and new pages.
    - The pilot sample size is underpowered and we can't interpret the
      insignificant p-value from the z-test previously

   See the code in ab_test.py
   ```

5. State why running a pilot experiment allows us to more accurately
   determine the minimum sample size required for a certain power.

   (**Estimated Time: 5 mins**)

   - Running a pilot informs us of a more accurate sign-up rate of the new
     page than guess-work. Subsequently, we are more informed about the sample
     size needed to show statistical signifance of the difference between
     the new and the old page
