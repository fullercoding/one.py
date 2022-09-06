import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#you can give a function an alias with "as"

from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra bacon')

#giving the module an alias

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'lemons', 'extra cheese')

#importing all functions in a modules

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'oranges', 'extra swiss cheese')