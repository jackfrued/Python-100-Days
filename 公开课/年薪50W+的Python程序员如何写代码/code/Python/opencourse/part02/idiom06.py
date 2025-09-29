data = {'x': '5'}

# if 'x' in data and isinstance(data['x'], (str, int, float)) \
#         and data['x'].isdigit():
#     value = int(data['x'])
#     print(value)
# else:
#     value = None

try:
    value = int(data['x'])
    print(value)
except (KeyError, TypeError, ValueError):
    value = None
