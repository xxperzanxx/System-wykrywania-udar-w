keys = list(map(lambda x: x.replace('\n', ''), open("model/diab.txt", "r").readlines()))
values = list(map(lambda x:int(x.replace('\n', '')), open("model/diab_fact.txt", "r").readlines()))

print(dict(zip(keys, values)))