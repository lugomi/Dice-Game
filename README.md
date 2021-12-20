# Greed
Dice game 


Questions I came up with:
1) Would a user care to see actual die or is a number ok for this use case?

Assumptions I made:
1) I assumed that the user wouldn't care about previous scores, so no score is saved. Instead the score is given every time the user plays a round of Greed.

2) Another assumption that I made is that the user will operate the program as intended, so no error checks. What that means in this specific case is that the user will be prompted if they want to roll the die. 

a) If a user responds with "yes", then the game will execute. 
b) If they response with "no", then the game will not go on.

Different paths:
1) The first problem I had to focus on was determining how I wanted to implement die. At first I considered creating multiple dice, but then decided instead that the dice object could have a method that would allow a user to roll a specified amount of die. Doing this would allow further modularization in the event the user would like to use more/less than the standard 5 die for a roll.

2) Keeping track of numbers rolled and their occurences provided multiple me multiple options. At first I considered using a set, but then decided otherwise since it would not take duplicates into account. I instead decided to make a dynamic array/list that would allow me to keep track of every number rolled. 

3) When trying to calculate score the first thing I noticed was that all numbers can provide points when they appear at least three times in a roll, but only two of six possible numbers can provide points if they appear only once (1 and 5). At first I found myself making a very lengthy method that calculated score but had to reasses since there was a lot of reptition. I then was able to reapproach the problem and instead made a method for calculation that reduced repetition and focused more on checking for occurences of triple and single numbers. 

4) Originally my dice had the ability to calculate score but I found it better to make a separate score checker since it would be confusing and cause clutter to my dice object. Instead I created a sepearate calculator for scores and it helped reduce clutter and allowed there to be a direct focus on determining scores. 