#WAF to printn the elements of a list in a single line.
cities = ["gale", "texas", "wiper", "rider", "wider"]
spells = ["absoluteZ", "thunderclapimp", "gust", "dicathen"]

# def print_l(list):
#     print(list)
#     return list
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(spells)
print()