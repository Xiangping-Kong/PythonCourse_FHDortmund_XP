
# Define a function to get the last element of a tuple
def get_last(tuple_item):
    return tuple_item[-1]

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Use get_last as the sorting key
sorted_list = sorted(sample_list, key=get_last)
#sample_list.sort(key=get_last)

print(sorted_list)

