def my_url(**kwargs):
    url = 'https://api.go.kr?'
    print(kwargs)
    for name, value in kwargs.items():
        url += f'{name}={value}&'
    return url


print(my_url(sidoname='서울', key='asdf'))
