## Django REST Framework

### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

> - URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.
> - HTTP Method는 GET과 POST 두 종류 뿐이다.
> - ‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.

- T : Uniform Resource Identifier
- F : GET, POST, PUT, DELETE
- F : create 별도 명시 X, `/` 포함 x



### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

> - 200
> - 400
> - 401
> - 403
> - 404
> - 500

- 200 - OK, 요청 성공 
- 400 - Bad Request, 잘못된 문법으로 인해 서버가 요청을 이해할 수 없음
- 401 - Unauthorized 비인증된 요청
- 403 - Forbidden 클라이언트가 콘텐츠에 접근할 권리가 없다
- 404 - Not Found 사용자가 요청한 자원을 찾을 수 없음, 잘못된 url 접근
- 500 -  Internal Server Error 서버가 처리방법을 모르는 상황, 처리할 함수나 기능을 아직 서버가 구현해 놓지 않았을 때



### 3. 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

> ```python
> class Student(models.Model):
>     name = models.TextField()
>     age = models.CharField(max_length=20)
>     address = models.TextField()
> ```

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.serializer):
    class Meta:
        model = Student
        fields = '__all__'
```



### 4. Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

- 직렬화 : 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정