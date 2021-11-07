## Vue 기초

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오

> - 동일한 요소에 v for 와 v if 두 디렉티브가 함께 작성된 경우, 매 반복 시에 v if 의 조건문으로 요소의 렌더링 여부를 결정한다
> - v-bind 디렉티브는 `@`, v-on 디렉티브는`:` shortcut(약어)을 제공한다
> - v model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 v model 속성값의 제어를 통해 값을 바꿀 수 있다

- T
- F : v-bind : `:`, v-on : `@`
- F : 양방향



### 2. computed 와 watch 의 개념과 그 차이에 대해서 간단히 서술하시오

- computed : 함수의 형태로 정의, 함수가 아닌 함수의 반환 값이 바인딩, 종속된 대상이 변경될 때만 함수를 실행

- watch : 특정 데이터의 변화 상황에 맞춰 다른 data등이 바뀌어야 할 때, 데이터에 변화가 일어났을 때 실행

  



### 3. 다음은 홀수 데이터만 렌더링하는 Vue Application 의 예시이다. 빈칸 (a), (b), (c) 에 들어갈 코드를 작성하시오

> ```html
> <div id="app">
>     <div (a)="(num, (b)) in (c)" :key="(b)">
>     	<p>{{ num }}</p>
>     </div>
> </div>
>     
> <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
>     <script>
>     const app = new Vue ({
>         el: "#app",
>         data: {
>         nums: [1, 2, 3, 4, 5, 6],
>         },
>         computed: {
>             oddNumbers: function () {
>                 return this.nums.filter((num) => {
>                     return num % 2 == 1
>                 })
>             }
>         }
>     })
> </script>
> ```

```html
<div id="app">
    <div v-for="(num, idx) in oddNumbers" :key="idx">
    	<p>{{ num }}</p>
    </div>
</div>
    
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    const app = new Vue ({
        el: "#app",
        data: {
        nums: [1, 2, 3, 4, 5, 6],
        },
        computed: {
            oddNumbers: function () {
                return this.nums.filter((num) => {
                    return num % 2 == 1
                })
            }
        }
    })
</script>
```

