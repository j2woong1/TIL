## Vue 기초

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

> - SPA는 Single Pattern Application의 약자이다.
> - SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 이후부터는 페이지 갱신에 필요한 데이터만 전달받는다.
> - Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트되는 것을 의미한다.

- F : Single Page Application
- T
- T



### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.

Model, View, View Model

- Model : JavaScript의 Object 자료 구조 -> 화면에 표현되는 내용, 데이터
- View : 사용자가 보는 화면
- View Model : View에서 표시할 데이터가 추상화 처리, Model과 상호작용하여 데이터를 주고 받음
  - View에서 View Model의 특정 데이터를 참조하여 화면에 표시하도록 정의하고, View Model의 데이터가 바뀌면 그대로 화면에 반영함



### 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

> ```html
> <div id="app">
>   {{ (a) }}
> </div>
> 
> <script>
> 	const app = (b)({
>     el: (c),
>     data: {
>     message: 'Hello World',
> 	  }
>   })
> </script>
> ```

```html
<div id="app">
  {{ message }}
</div>

<script>
	const app = new Vue({
    el: '#app',
    data: {
    message: 'Hello World',
	  }
  })
</script>
```

