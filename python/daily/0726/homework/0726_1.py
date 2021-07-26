def get_dict_avg(dic):
    num = sum(dic.values())
    return num / len(dic)


print(get_dict_avg({
    'python': 80,
    'algorithm': 90,
    'django': 89,
    'web': 83
}))
