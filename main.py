from Knapsacker import Knapsacker as ks
from Select import Select as k_select
from getGCD import FinderGCD as gcd_finder
from CreateTable import CreateTable as table

knap = ks()
k_sel = k_select()
f_gcd = gcd_finder()
create_table = table()



# EDIT THIS AS YOUR USER INPUT

# limit weight
LIMIT = 70

# item no., value, weight
item_weights = {
    1 :40,
    2 :50,
    3 : 10,
    4 : 20,
    5 : 30,
}
item_values = {
    1 : 20,
    2 : 80,
    3 : 100,
    4 : 20,
    5 : 40,
}

# END USER INPUT

weights_array = [0]
values_array = [0]

for x,z in item_weights.items():
    weights_array.append(z)

for x,z in item_values.items():
    values_array.append(z)


array_gcd = f_gcd.find_gcd(weights_array)
weights = create_table.table(array_gcd, LIMIT)

# creates the columns for item number
items = []
for x in range(len(weights_array)):
    items.append(x)
print(items[1:])

print("WEIGHT OF ITEMS, VALUE BELOW:")
print(weights_array[1:])
print(values_array[1:])

k_tbl = [ [0]*len(items) for i in range(len(weights))]

k_tbl = knap.knapsack(k_tbl, values_array, weights, weights_array)
print("THE KNAPSACK TABLE")
for x in k_tbl:
    print(x)


# will start program
k_sel.k_selection(k_tbl)