from collections import Counter
def count_of_most_occurring(numbers):
    return Counter(numbers).most_common(1)[0][1]
numbers = [1, 2, 2, 2, 3]
print(count_of_most_occurring(numbers))
def count_occurring(numbers):
    return Counter(numbers).most_common(1)[0][1]
numbers = [1, 5, 5, 6, 4]
print(count_occurring(numbers))
