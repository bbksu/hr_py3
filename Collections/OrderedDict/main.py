from collections import OrderedDict

items = int(input())
order_dict = OrderedDict()
for i in range(items):
    items = input().split()        
    item_name, price = " ".join(items[:-1]), int(items[-1])   
    order_dict[item_name] = order_dict.setdefault(item_name, 0) + price

item_net = "\n".join(f"{x} {y}" for x, y in order_dict.items())
print(item_net)