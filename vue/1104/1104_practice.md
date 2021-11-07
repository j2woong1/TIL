## Vue

> - Vue 와 axios 를 활용하여 API 서버로 요청을 보내 응답 받은 이미지를 화면에 표시하는 앱을 완성하시오
>   - 사용 API: https://api.thecatapi.com/v1/images/search
>   - Vue life cycle을 활용하여 Vue 인스턴스가 초기화 될 때 API 서버로 요청을 보내 이미지를 불러온다
>   - Vue life cycle을 활용하여 이미지 리소스가 업데이트 될 때마다 console 창에 이미지 리소스를 출력한다
>   - "Get Cat” 버튼을 누르면 새로운 이미지를 불러와 대체한다

```html
<div id="app">
	<h1>Cat Image</h1>
    <div v-if="imgSrc">
      <img :src="imgSrc" alt="cat image"> 
   	</div>
    <button @click="getCat">Get Cat</button> 
</div>
  
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
    const app = new Vue({
      el: '#app',
      data: {
        imgSrc: null, 
      },
      methods: {
        getCat: function () {
          const API_URL = "https://api.thecatapi.com/v1/images/search" 
          axios.get(API_URL)
            .then((response) => { 
              this.imgSrc = response.data[0].url
            })
        },
      },
      created: function () { 
        this.getCat()
      },
      updated: function () { 
        console.log(this.imgSrc)
      },
    })
</script>
```

![image-20211104160320511](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211104160320511.png)