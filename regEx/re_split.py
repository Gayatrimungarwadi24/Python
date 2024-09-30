import re

string="Twelve: 12 Eighty nine: 89. "
pattern="\d+"
result=re.findall(pattern, string)
print(result)