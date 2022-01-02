# Fire Emblem: Three Houses Gardening Tool


This program assumes that you can plant up to 5 seeds and that you have unlocked all the cultivate methods. I may in the future have another prompt for professor level and all that stuff, but as of right now, that has not happened.

You must type in what you want to grow exactly. This includes capitalization, hyphens, apostrophes, and spaces (and correct spelling of course). Input sanitization is next on my to-do list

There is still one unknown regarding how combining seeds affects the odds. This program assumes that if you plant x of seed1 and y of seed2, then the chance of selecting seed1's growth chart is x/(x+y). Apart from that one assumption, the expected values (EVs) generated should be accurate.

The program will by default output the 50 highest producing seed combinations. At the end, you will be prompted if you would like to see the remaining combinations.

Stat boosters are calculated differently. I wasn't able to find an exact way to calculate their probability so I used a general score system which should be directly proportional to the scores given.

The newest release tells you how much you should cultivate a given combination. Level 0 would be not cultivating at all and Level 6 is "Spread Unicorn Blessings."


This program produces all viable seed combinations using AT MOST 2 different types of seeds. Honestly, full support for up to 5 different seeds would likely make the program run far too slowly.


This program uses only the standard python library and the math library.
