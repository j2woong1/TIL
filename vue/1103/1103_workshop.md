## Vue 기초

> - Vue 및 lodash 라이브러리를 활용하여 점심메뉴와 로또 앱을 완성하시오
>   - Pick One 버튼을 클릭하면 미리 정의되어 있던 메뉴 리스트 중에서 랜덤한 아이템을 화면에 표시한다
>   - Get Lucky Numbers 버튼을 클릭하면 1 부터 45 까지의 숫자 중 랜덤한 숫자 6개를 선택하여 화면에 표시한다 .

```html
<body>
  <div id="app">
    <h2>점심메뉴</h2>
    <button @click="pickOne">Pick One</button>
    <p>{{ choice }}</p>
    <hr>

    <h2>로또</h2>
    <button @click="getLuckyNumbers">Get Lucky Numbers</button>
    <p v-if="luckyNumbers.length">{{ luckyNumbers }}</p>
  </div>
  <!-- Vue CDN & lodash 삽입 -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const app = new Vue ({
      el: '#app',
      data: {
        menus: ['국밥', '우동',  '낙지볶음', '보쌈'],
        choice: '',
        luckyNumbers: [],
      },
      methods: {
        pickOne: function () {
          const randomIndex = _.random(this.menus.length - 1)
          this.choice = this.menus[randomIndex]
        },
        getLuckyNumbers: function () {
          const numbers = _.range(1, 46)  
          this.luckyNumbers = _.sampleSize(numbers, 6)
        }
      }
    })
  </script>
</body>
```

