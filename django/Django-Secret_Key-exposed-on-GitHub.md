# Django Secret Key exposed on GitHub

> Django 프로젝트를 바로 Git에 Push했을 때 메일로 날아오는 제목

내 SECRET_KEY가 외부에 노출될 수 있다는 의미.

SECRET_KEY는 말 그대로 **비밀**이기 때문에, 감춰야할 필요가 있다!!



이를 수행하기 위해, 

먼저 .gitignore, db.splite3, manage.py와 동일한 디렉토리에 

**secret.json**

파일을 생성한다.

또한 파일 내에는 다음과 같이,

setting.py에서 자신의 SECRET_KEY를 가져와서 복붙해준다.



> settings.py

```python
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '이 부분에 SECRET_KEY 내용이 적혀 있다.'
```

> secret.json

```json
{
    "SECRET_KEY": "이 부분에 SECRET_KEY 내용이 적혀 있다."
}
```



위의 기본 세팅이 완료되면, 

이제 settings.py에 내용을 덧붙인다.

settings.py의 기본 내용은 SECRET_KEY 부분을 제외하고 건들지 않으면서 다음과 같이 내용을 추가한다.



> settings.py

```python
import os, json  # 추가된 부분
from django.core.exceptions import ImproperlyConfigured  # 추가된 부분
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# secret_file에 만들어준 json파일의 경로를 넣어준다. (추가된 부분)
secret_file = os.path.join(BASE_DIR, 'secret.json')

# secret_file을 열어 secrets에 json파일의 내용을 넣어준다. (추가된 부분)
with open(secret_file) as f:
    secrets = json.loads(f.read())


# secrets에서 json파일의 내용 중 SECRET_KEY의 value를 가져오는 함수
# 발생할 수 있는 에러에 대한 예외 처리를 같이 진행해준다. (추가된 부분)
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable'
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY 변수에 우리가 숨겨놨던 SECRET_KEY를 가져온다!! (변경된 부분)
SECRET_KEY = get_secret("SECRET_KEY")
```



이제 SECRET_KEY를 숨겨놓고 가져와서 사용하는 과정에 대한 코드는 끝났다.

마지막으로,

원래의 목적이었던 SECRET_KEY를 Git에 올리지 않는 것은 간단하게 구현한다.



**.gitignore** 파일의 마지막에,

만들어 주었던 **secret.json**을 적어주는 것!!

.gitignore파일에 적혀있는 내용들은 Git에 Push되지 않기 때문에

적어주는 것 하나만으로 secret.json파일을 숨길 수 있다!!!



이 과정을 끝으로,

다음부터는 다시는 이런 메일을 접하지 않을 수 있다!!