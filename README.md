# Shut-the-box
Probability of winning a game of shut the box

I've seen this game on tiktok called shut the box and I've been curious for ages about the probability of winning a game. 
The rules can be found on: https://www.mastersofgames.com/rules/shut-box-rules.htm

This uses the Monte Carlo method to predict the probability of winning a game of shut the box if you did not use strategy. 

shut_the_box.py: 
This code specifically uses randomness, with no strategy involved. 
The results show that there is a roughly 2.2% chance of winning. 
This is very low, indicating that randomness is not an optimal strategy. 

shut_the_box_big_strat.py: 
This code wants to get rid of the larger numbers first, prioritising the box shutting resulting in as large a number as possible being shut. 
The results show that there is roughly an 8.6% chance of winning using this strategy, making it nearly 4 times more effective than randomness. 

shut_the_box_small_strat.py: 
This code prioritises getting rid of the smallest numbers possible first, holding the biggest numbers as late as possible. 
The results show there is roughly a 1.0% chance of winning with this strategy, making it have less than half the effectiveness of randomly choosing numbers. 

shut_the_box_hold_the.py: 
An extension of the big_strat that waits as long as possible to get rid of certain numbers. 
Holding the 1 is roughly 8.1% effective. Holding the 2 is roughly 8.4% effective. Holding the 3 is roughly 7.6% effective. 
Holding the 4 is roughly 7.2% effective. Holding the 5 is roughly 6.5% effective. Holding the 6 is roughly 6.4% effective. 
Holding the 7 is roughly 5.5% effective. Holding the 8 is roughly 5.1% effective. Holding the 9 is roughly 4.1% effective. 
If you were going to wait to put down a number for as long as possible, the suggestion would be 2. However, it is not as effective as just choosing the most effective largest number to put down. 

Ideally, in the future I would be uploading other versions of the strategy, eventually collating the code so one can test different strategies on the same base game. 
Will update when I have time/am motivated. 
Might also document my code at some point.


