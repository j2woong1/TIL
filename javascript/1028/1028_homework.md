## JavaScript 기초

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오

> - let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다
> - "값이 없음" 을 표현하는 값으로 null 과 undefined 두 종류가 있으며 둘 다 typeof 연산자에서 undefined 가 반환된다
> - for ... in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 활용하는 경우에 주로 활용한다
> - 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false 를 반환한다
> - JavaScript 에서 함수는 변수에 할당 , 인자로 전달할 수 있으나 함수의 결괏값으로 반환할 수는 없다

- F : var : 변수 재선언 허용, hoisting (선언 이전 참조)
- F : typeoff null -> object
- T
- F
- F



#### 2. 다음의 Array Helper Method 의 동작을 간략히 서술하시오

> map, filter, find, every, some, reduce

- map : 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환, 배열을 다른 모습으로 바꿀 때
- filter : 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- find : 콜백 함수의 반환 값이 참이면 해당 요소를 반환, 찾는 값이 배열에 없으면 undefined 반환
- every : 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환, 모든 요소가 통과하지 못하면 거짓, 빈 배열이면 참 반환
- some : 배열의 모든 요소가 주어진 판별 함수를 통과 하면 참을 반환, 모든 요소가 통과하지 못하거나 빈 배열이면 거짓 반환
- reduce : 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 후 콜백 함수의 반환 값들을 하나의 값에 누적 후 반환



#### 3. 아래의 숫자 배열에 map 함수를 사용하여 모든 아이템에 3 제곱을 한 새로운 배열을 만드는 코드를 작성하시오

> ```javascript
> const nums = [1, 2, 3, 4]
> ```

```javascript
const nums = [1, 2, 3, 4]
const result = nums.map(num => {
    return num**3
})
console.log(result)
```

