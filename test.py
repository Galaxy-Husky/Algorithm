import re
print(re.fullmatch(r'[+-]?((\d+\.\d*)|(\d+)|(\.\d+))([eE][+-]?\d+)?', 'e9'))
print(re.search(r'[+-]?((\d+\.\d*)|(\d+)|(\.\d+))([eE][+-]?\d+)?', 'e9').group())