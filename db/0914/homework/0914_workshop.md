> Table Name : countries
>
> |   name    | data type |
> | :-------: | :-------: |
> | room_num  |   text    |
> | check_in  |   text    |
> | check_out |   text    |
> |   grade   |   text    |
> |   price   |  integer  |
>
> |  id  | room_num |  check_in  | check_out  |  grade   | price |
> | :--: | :------: | :--------: | :--------: | :------: | :---: |
> |  1   |   B203   | 2019-12-31 | 2020-01-03 |  suite   |  900  |
> |  2   |   1102   | 2020-01-04 | 2020-01-08 |  suite   |  850  |
> |  3   |   303    | 2020-01-01 | 2020-01-03 |  deluxe  |  500  |
> |  4   |   807    | 2020-01-04 | 2020-01-07 | superior |  300  |



# 1. SQL Query

> 위 countries 테이블을 바탕으로 아래 문제에 해당하는 SQL query 문을 작성하고 실행하시오.

1. countries 테이블을 생성하시오

   ```sqlite
   CREATE TABLE countries (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       room_num TEXT NOT NULL,
       check_in TEXT NOT NULL,
       check_out TEXT NOT NULL,
       grade TEXT NOT NULL,
       price INT NOT NULL
   );
   ```

2. 데이터를 입력하시오

   ```sqlite
   INSERT INTO countries (room_num, check_in, chech_out, grade,prce) 
   	VALUES ('B203','2019-12-31','2020-01-03', 'suite', 900) ,
   	('1102', '2020-01-04', '2020-01-08', 'suite', 850), 
   	('303', '2020-01-01', '2020-01-03', 'deluxe', 500), 
   	('807', '2020-01-04', '2020-01-07', 'superior', 300);
   
   INSERT INTO countries VALUES (1, 'B203', '2019-12-31', '2020-01-03', 'suite', 900);
   INSERT INTO countries VALUES (2, '1102', '2020-01-04', '2020-01-08', 'suite', 850);
   INSERT INTO countries VALUES (3, '303', '2020-01-01', '2020-01-03', 'deluxe', 500);
   INSERT INTO countries VALUES (4, '807', '2020-01-04', '2020-01-07', 'superior', 300);
   ```

3. 테이블의 이름을 hotels 로 변경하시오

   ```sqlite
   ALTER TABLE countries RENAME TO hotels;
   ```

4. 객실 가격을 내림차순으로 정렬하여 상위 2 개의 room_num 과 price 를 조회하시오

   ```sqlite
   SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2; 
   ```

5. grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오

   ```sqlite
   SELECT grade, COUNT(grade) FROM hotels GROUP BY grade ORDER BY COUNT(grade) DESC;
   ```

6. 객실의 위치가 지하 혹은 등급이 deluxe 인 객실의 모든 정보를 조회하시오

   ```sqlite
   SELECT * FROM hotels WHERE (room_num LIKE 'B%') OR (grade = 'deluxe');
   ```

7. 지상층 객실이면서 2020 년 1 월 4 일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오

   ```sqlite
   SELECT * FROM hotels WHERE (room_num NOT LIKE 'B%') AND (check_in = '2020-01-04') ORDER BY price ASC;
   ```



# 2. SQL ORM 비교하기

> 주어진 정보를 활용하여 작성된 SQL 문과 대응하는 ORM 문을 작성하고 실행하시오 .
>
> Table Name : users
>
> |    name    |  data type  |
> | :--------: | :---------: |
> |     id     | integer(pk) |
> | first_name |    text     |
> | last_name  |    text     |
> |    age     |   integer   |
> |  country   |    text     |
> |   phone    |    text     |
> |  balance   |   integer   |

1. user 테이블 전체 데이터를 조회하시오

   ```sqlite
   SELECT * FROM users_user;
   ```

   ```python
   users = User.objects.all()
   ```

2. id 가 19 인 사림의 age 를 조회하시오 .

   ```sqlite
   SELECT age FROM users_user WHERE id=19;
   ```

   ```python
   users = User.objects.filter(id=19).values('age')
   
   User.objects.get(pk=19).age
   ```

3. 모든 사람의 age 를 조회하시오 .

   ```sqlite
   SELECT age FROM users_user;
   ```

   ```python
   users = User.objects.all().values('age')
   ```

4. age 가 40 이하인 사림들의 id 와 balance 를 조회하시오 .

   ```sqlite
   SELECT id, balance FROM users_user WHERE age <= 40;
   ```

   ```python
   users = User.objects.filter(age__lte=40).values('pk', 'balance')
   for user in users:
       print(user.get('pk'))
       print(user.get('balance'))
       
   users = User.objects.filter(age__lte=40)
   for user in users:
       print(user.pk, user.balance)
   ```

5. last_name 이 ‘김’이고 balance 가 500 이상인 사람들의 first_name 을 조회하시오.

   ```sqlite
   SELECT first_name FROM users_user WHERE last_name='김' AND balance>=500;
   ```

   ```python
   users = User.objects.filter(last_name='김', balance__gte=500).values('first_name')
   
   from django.db.models import Q
   User.objects.filter(Q(last_name='김') | Q(balance__gte=500)).values('first_name')
   ```

6. first_name 이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance 를 조회하시오.

   ```sqlite
   SELECT balance FROM users_user WHERE first_name LIKE '%수' AND country='경기도';
   ```

   ```python
   users = User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
   ```

7. balance 가 2000 이상이거나 age 가 40 이하인 사람의 총 인원수를 구하시오 .

   ```sqlite
   SELECT COUNT(*) FROM users_user WHERE balance >= 2000 OR age <= 40;
   ```

   ```python
   from django.db.models import Q
   User.objects.filter(Q(age__lte=40) | Q(balance__gte=2000)).count()
   ```

8. phone 앞자리가 010’ 으로 시작하는 사람의 총원을 구하시오 .

   ```sqlite
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '010%';
   ```

   ```python
   User.objects.filter(phone__startswith='010').count()
   ```

9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오 .

   ```sqlite
   UPDATE users_user SET country='경기도' WHERE first_name='옥자' AND list_name='김';
   
   SELECT country FROM users_user WHERE first_name='옥자' AND list_name='김';
   ```

   ```python
   users = User.objects.filter(last_name='옥자', first_name='김')[0]
   user.country = '경기도'
   user.save()
       
   User.objects.filter(last_name='옥자', first_name='김').update(country='경기도');
   ```
   
10. 이름이 ‘백진호’인 사람을 삭제하시오 .

    ```sqlite
    DELETE FROM users_user WHERE first_name='진호' AND last_name='백';
    SELECT * FROM users_user WHERE first_name='진호' AND last_name='백';
    ```

    ```python
    User.objects.filter(last_name='진호', first_name='백').delete()
    ```

11. balance 를 기준으로 상위 4 명의 first_name, last_name, balance 를 조회하시오.

    ```sqlite
    SELECT first_name, last_name, balance FROM users_user ORDER BY balance DESC LIMIT 4;
    ```

    ```python
    User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]
    for user in users:
      print(user.get('first_name'))
      print(user.get('last_name'))
      print(user.get('balance'))
    ```

12. phone 에 '123’ 을 포함하고 age 가 30 미만인 정보를 조회하시오 .

    ```sqlite
    SELECT * FROM users_user WHERE phone LIKE '%123%' AND age < 30;
    ```

    ```python
    users = User.objects.filter(phone__contains='123', age__lt=30)
    ```

13. phone 이 010’ 으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오 .

    ```sqlite
    SELECT DISTINCT country FROM users_user WHERE phone LIKE '010%';
    ```

    ```python
    users = User.objects.filter(phone__startswith='010').values('country').distinct()
    ```

14. 모든 인원의 평균 age 를 구하시오 .

    ```sqlite
    SELECT AVG(age) FROM users_user;
    ```

    ```python
    from django.db.models import Avg
    User.objects.aggregate(Avg('age'))
    ```

15. 박씨의 평균 balance 를 구하시오 .

    ```sqlite
    SELECT AVG(balance) FROM users_user WHERE last_name='박';
    ```

    ```python
    User.objects.filter(last_name='박').aggregate(Avg('balance'))
    ```

16. 경상북도에 사는 사람 중 가장 많은 balance 의 액수를 구하시오 .

    ```sqlite
    SELECT MAX(balance) FROM users_user WHERE country = '경상북도';
    ```

    ```python
    User.objects.filter(country='경상북도').aggregate(Max('balance'))
    ```

17. 제주특별자치도에 사는 사람 중 balance 가 가장 많은 사람의 first_name 을 구하시오 .

    ```sqlite
    SELECT first_name FROM users_user WHERE country='제주특별자치도' ORDER BY balance DESC LIMIT 1;
    ```

    ```python
    user = User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[0]
    
    user = User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name').first()
    ```



