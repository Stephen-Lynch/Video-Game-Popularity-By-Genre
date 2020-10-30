# Video-Game-Popularity-By-Genre
Capstone 1 Project for Galvanize. Shows which video game genres have climbed in popularity as time has gone on.

## Overview

![image](images/revenue.jpg)

The video game market has recently become the most lucrative form of entertainment, with an estimated 159.3 billion dollars 
of revenue coming in by the end of this year. This information came as a surprise to me since video games were sort of a shunned activity 
when I was growing up, always being linked to things such as gun violence and The Devil. Since that's apparently done a 180 in terms of how popular they've become, and how mainstream they 
currently are, I wanted find out where you should start looking if you were to make a brand new game tomorrow and answer a few questions 
that came to mind, such as:
    -What genre of game should you make if you're looking to make the most sales?
    -Does any particular genre sell better in certain parts of the world?
    -If you were to take an exclusivity deal, which platform should you choose?

## The Data

df.head() image

I pulled my data from a google dataset which conversly pulled it's information from the website [vgchartz](https://www.vgchartz.com), which tracked the physical global sales for over 16,598 video game releases starting in the year 1978 to the year 2017. It also contains sales per region as well as the platform on which it was sold on.

![image](images/bar_over_time.png)

I wanted to give a little bit of background on this data and state the data begins to dip starting in the year 2013. While this looks alarming at first, keep in mind this data only tracked physical sales and
it's cause is likely due to the massive rise in digital sales for both PC and Console gaming. Considering gaming has been bringing in the most revenue for a few years now, it's no doubt that global sales
are certainly still on the rise if we were to include digital sales. So with this in mind I will be focusing on the marketshare of these games and not necessarily the total amount of global sales.

## Most popular video game genres
![Genre_Over_Time](images/gen_over_time.png)

As you can see, many genres have risen and fallen over the years. Platformers were considered the bees knees in the early 1990s, however as time has gone on they've struggled to perform as well as the behemoths that are Action games and Shooters.
While both of these genres have there ups and downs, they both benefit from being rather flexible with both what the gameplay has to offer, as well as what you're looking to write in terms of your story. They also tend to be more accessible than a game within a 
more niche genre such as sports or role-playing, where the both the gameplay and story narrative (If you have one) need to be focused on either the sport itself, or allow you to role-play the exact character you want to be. If you're looking to maximize your sales for your first game, I would highly suggest creating either an action game or a shooter.


## Percentage of sales for each country
![image](images/genre.png)

You'll also want to know where should you market your game. North America seems to always outsell every other part of the world with the EU coming in close second for most genres. This is likely due to how massive North America is, but it's still something to keep in mind. There are two exceptions to this however, Racing games are more popular in EU countries while role-playing games do exceptionally well in Japan outselling the EU and competeing with North America. One thing to keep in mind, even though games such as simulation, strategy, and fighting games don't sell the most boxes, they do hit niche markets that the big genres like shooters and action games don't necessarily hit.

## What platform should you sell your game on?
![image](images/platforms.png)

The final thing to note is deciding which platform your game should have an exclusivity deal with if you choose to do so. As you can see video games on PS4 outsell both of the other consoles combined, so if you're looking to be exclusive to one console you should consider Sony first. The Xbox One has an incredibly interesting story to tell as well. If you plan on only selling your game in North America, then PS4 and Xbox One video game sales are relatively similar. However, in EU, Japan, and other parts of the world, Xbox One underpeforms significantly compared to it's counterpart. So if you land a deal with XBox you're relatively safe to spend the majority of your marketing in North America. This finally brings us to the Wii U which is far below it's other two competitors, I would suggest stearing clear for an exclusivity deal for the WiiU , that is unless they're willing to make up for the nearly half the difference in sales you would make with Xbox one or nearly 4 times the sales you would make with Ps4. The same can be said with Xbox one compared to PS4 with nearly double the sales.

## Conclusion
You have a lot of options when deciding both what game you're making and where you're trying to market it. Clearly Action and Shooter games come out on top in the war against genres, and PS4 dominates the console field. If you're looking at exactly where you should be marketing your game, the safe bet is to spend the majority of your marketing budget in North America, followed by Europe, then Japan, and finally the rest of the world. This is all of course under the assumption you make a decent game within these genres themselves.