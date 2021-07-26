# 1. 평균 점수 구하기

```python
# key : 과목명, value : 점수

def get_dict_avg(dic):
    num = sum(dic.values())
    return num / len(dic)


print(get_dict_avg({
    'python': 80,
    'algorithm': 90,
    'django': 89,
    'web': 83
}))
```



# 2. 혈액형 분류

```python
# list -> key : 혈액형 종류, value : 사람 수

def count_blood(blood_lst):
    blood_dict = {}

    for blood in blood_lst:
        if blood_dict.get(blood):
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1
    return blood_dict


print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB'
]))
```