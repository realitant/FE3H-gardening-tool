# Fire Emblem: Three Houses Gardening Tool


This program assumes that you can plant up to 5 seeds and that you have unlocked all the cultivate methods. I may in the future have another prompt for professor level and all that stuff, but as of right now, that has not happened.

You must type in what you want to grow exactly. This includes capitalization, hyphens, apostrophes, and spaces (and correct spelling of course). Input sanitization is next on my to-do list

Each seed combination has a star rating. More stars mean a higher likelihood to get the item. However, some of the exact probabilities are still unknown to me, so there may be times where a close star rating actually favors the combination with fewer stars. I would try to avoid any combination with fewer than 2 stars unless there were absolutely no other options to get that item (except for stat boosters)

Stat boosters are calculated differently. For this reason, there are only two star ratings. One star is better than none.

The newest release tells you how much you should cultivate a given combination. Level 0 would be not cultivating at all and Level 6 is "Spread Unicorn Blessings."


This program produces all viable seed combinations using AT MOST 2 different types of seeds. Honestly, full support for up to 5 different seeds would likely make the program run far too slowly.


This program uses only the standard python library and the math library.
