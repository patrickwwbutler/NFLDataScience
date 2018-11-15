# NFLDataScience
Machine Learning Project to create fantasy football projections

This is a WIP personal project of mine with the ultimate goal of creating an effective fantasy football 
projections system to help decide which players to start on a given week.

My main objectives for this are to:
1. Learn to use various machine learning techniques
2. Compare effectiveness of different techniques and learn to identify which to use for future projects
3. Successfully project game scores with high accuracy
4. Project players' overall season rankings - preseason and midseason

Current work:
Learning to use numpy and pandas to manipulate data in a way that can be useful.
Working only with WRs and TEs, and planning to simply use the most recent game's stats as the only predictor 
as a proof of concept.

Progress:
A linear regression predictor based on various fantasy relevant statistics from the player's most recent game using only Wide Receivers and Tight Ends.
This method gives an average error of 0.01-0.05 (Each run is different due to randomized train/test splitting)
and the error's standard deviation is generally around 5.2-5.5.

The average is highly accurate with this model, but the standard deviation leaves something to be desired, 
where in fantasy football a swing of 5 points can be a difference maker.
