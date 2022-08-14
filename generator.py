nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

def gen(lst: list) -> list:
    return (item for sub in lst for item in sub)

for item in gen(nested_list):
    print(item)
