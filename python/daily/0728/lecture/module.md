# Module

## 1. Module, Package

### 1. Module

- 특정 기능 파이썬 단위(.py)로 작성

### 2. Package

- 특정 기능 관련 여러 모듈 집합
- 패키지 안 -> 다른 서브 패키지

### 3. 파이썬 패키지 관리자 (pip) 명령어

#### 1. 설치

```python
pip install ~
```

#### 2. 삭제

```python
pip uninstall ~
```

#### 3. 목록, 특정 패키지 정보

```python
pip list
pip show ~
```

#### 4. freeze

- pip install에서 활용되는 형식으로 출력
- 해당 목록 requirements.txt로 관리

```python
pip freeze
```

#### 5. 관리

```python
pip freeze > requirements.txt
pip install -r requirements.txt
```



## 2. 가상환경

- 외부 패키지, 모듈 사용

### 1. venv

- 고유한 파이썬 패키지 집합

```python
python -m venv <폴더명> : 설치
source venv/Scripts/activate : 활성화
```



## 3. 활용

### 1. 모듈 만들기 - check

```python
# 짝수 (even), 홀수 (odd) 판별

def odd(n):
	return bool(n % 2)
	
def even(n):
	return not bool(n % 2)
	
import check
dir(check)
check.odd(3) # True
check.even(3) # False

from check import odd
odd(5) # True
even(4) # NameError

from check import *
odd(5) # True
even(4) # True
```

### 2. 패키지

- 여러 모듈/하위 패키지로 구조화
  - package.module
- __init__.py : 패키지 인식

