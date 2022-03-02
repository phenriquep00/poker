import re

regex = re.compile(r"\[[^\\]]*]")

string = 'pair [5, 71, 8, 102, 12]'

final = re.search("\\[[^]]*]", string)
print(final.group())
