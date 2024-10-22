Dataset : price of house Theran
coulmn :Area Room Parking Warehouse Elevator Address Price Price(USD)

summary:

I made graphs bassed on the price of the house
bassed on the number of rooms and having and 
don't having Parking Warehouse Elevator and
I plotted the highest and lowest price of each 
address and I plotted the average price of the data 

Data Cleaning:

We have someting in Area (Dtype is object) 
well, i reolaced them with None
Then i deleted None (Address/Area)
The Area dtype is float and i turned into init

Statistic:

1- I find the Address mode(the most repetition of the Address)
I calculated the highest(maximum) lowest house price(minimum) 
bassed on the number of room

2-I have categorized them according to having and not having
Parking\Warehouse\Elevator(def value)

3- I found the highest snd lowest price of each address and
put them in a tuple (zip) so that i sorted them by highest price
then I found the minimum price at all 

4- I found the average data and removed the outliers
so i repeated this until there were no outliers

visualize:

1- I cose a chart from matplotlib example(hat graph)

I plotted the highest price and 
the lowest price of each house
bassed on the number of rooms in
Tehran provimce and in the most 
repeated address Punak 

2- I showed those who have in green and
those who don't have in red and you can 
understand how much it affects the price 
with different areas in Tehran and Punak  

3- I plotted line of (highest and lowest) price 
and I showed the maximum and minimum point

4- I plotted the line of average price in tehran 
and scatter normal data and outliers 
until the data becomes normal 