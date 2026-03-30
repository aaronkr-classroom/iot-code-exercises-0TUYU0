#3_set.py
# 두 집합 정의
set1 = {1, 2, 3, 'a', "Hello"}
set2 = {"Hello", 3, 4, 5, 'b'}

# 합집합
union_set = set1 | set2 # || = or(C), or = or(py)

# 교집합
intersection_set = set1 & set2 #&& = and(C)

# 차집합
difference_set = set1 - set2

# 대칭 차집합
symmetric_difference_set = set1 ^ set2 #union_set - intersection_set

print('union', union_set)
print(f"intersection: {intersection_set}")
print(f"difference: {difference_set}")
print(f"symmetric difference: {symmetric_difference_set}")