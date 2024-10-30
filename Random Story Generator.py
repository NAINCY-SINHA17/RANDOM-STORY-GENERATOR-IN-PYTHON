#RANDOM STORY GENERATOR PROGRAM...

import random

when = ['A few year ago','yesterday', 'last night','on 13 0ctober']
who = [ 'a  manager', 'a tarot card reader', 'a student', 'a pschologist']
name = ['Naincy', 'Sinu',  'Shivi', 'John']
residence = ['India', 'Germany', 'Canada','France','England']
went = ['seminar', 'university', 'forest','book shop', 'cafe']
happened = ['made a lot of friends', 'eats a pizza', 'buy a book named mysterious night' , 'found a ring' , 'solved a mistery']

print(random.choice(when)+ ',' + random.choice(who)+ ' named ' + random.choice(name)+
      ' that lived in ' + random.choice(residence)+ ' went to the ' + random.choice(went) +
      ' and ' + random.choice(happened))


