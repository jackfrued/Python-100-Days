data = [7, 20, 3, 15, 11]

# result = []
# for i in data:
#     if i > 10:
#         result.append(i * 3)

result = [num * 3 for num in data if num > 10]
print(result)
