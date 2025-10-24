
set_01 = {10, 20, 30, 40, 50, 60}
set_02 = {10, 20, 30}
set_03 = {1, 2, 3, 4, 5, 6}
print(type(set_01))

# 交集
# 集合01与集合02的交集
new_set_01 = set_01.intersection(set_02)
print(new_set_01)
for iterm in new_set_01:
    print(iterm)

# 并集
new_set_02 = set_01.union(set_03)
print(new_set_02)
for iterm in new_set_02:
    print(iterm)

# 减集
new_set_03 = set_01.difference(set_02)
print(new_set_03)
for iterm in new_set_03:
    print(iterm)
