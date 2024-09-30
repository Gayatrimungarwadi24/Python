import re

txt="Hi I'm Gayatri Mungarwadi and I'm 21"
pattern="\d+"
result=re.findall(pattern,txt)
print(result)
