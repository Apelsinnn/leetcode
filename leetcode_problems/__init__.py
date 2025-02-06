import re


jewels = "aA"
stones = "aAAbbbb"
count_in_list = re.findall(rf'[{jewels}]', stones)
count_jewels = len(count_in_list)
print(count_in_list)
print(count_jewels)

