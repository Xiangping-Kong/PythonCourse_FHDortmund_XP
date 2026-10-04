from typing import TypedDict, List


# 定义字典结构，给mypy识别类型
class Car(TypedDict):
    make: str
    model: int | str
    color: str


# Original list of dictionaries
cars: List[Car] = [
    {"make": "Google", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

print("Original list of dictionaries :")
print(cars)

# sort by model (convert to integer), reverse=True → 降序，匹配题目输出
sorted_cars = sorted(cars, key=lambda x: int(x["model"]), reverse=True)

print("\nSorting the List of dictionaries :")
print(sorted_cars)
