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

An extension could be to wait as long as possible to get rid of certain numbers. 
Ideally, in the future I would be uploading other versions of the strategy, eventually collating the code so one can test different strategies on the same base game. 
Will update when I have time/am motivated
Might also document my code at some point


