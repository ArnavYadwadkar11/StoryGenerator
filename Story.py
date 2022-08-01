import random 
when = ["Yesterday", "Tomorrow", "A few years ago", "Today", "On 31st December!"]
who = ["A boy", "A man", "A rabbit", "A monkey", "A Elephant"]
name = ["Arnav", "Dhruv", "Kiran", "Aryan", "Sameer"]
residence = ["India", "Paris", "Dubai", "China", "Australia"]
went = ["the park", "his friends house", "his office", "the electronics shop", "the amusement park"]
happened = ["Had a wonderful party!", "Buyed a new Computer", "Saw some amazing things", "To see the fireworks", "Did a lot of work"]
print(random.choice(when) + ', ' + random.choice(who) + " " + random.choice(name)+ ' that lived in ' + random.choice(residence) + " Went to the " + random.choice(went) + " and " + random.choice(happened))
