## JavaScript 기초

> - 제시된 CREATE, READ 기능을 충족하는 todo app 을 완성하시오
>   [필수사항]
>   - form 태그를 사용한다
>   - form 에서 submit 이벤트가 발생되었을 때 input 에 작성된 값이 todo 로 추가된다
>   - todo 는 ul 태그의 li 태그로 추가된다
>   - todo 가 추가된 후 input value 의 값은 초기화 된다
>   - (선택) 빈 값인 데이터는 입력을 방지한다
>     - 빈 값이면 알림창을 띄워 값을 입력하도록 안내한다

```html
<form action="">
    <input type="text" id="todo">
    <input type="submit" id="submit">
</form>
<script>

    const submitElement = document.querySelector('#submit')

    submitElement.addEventListener('click', function(event){
      event.preventDefault()
      const todoElement = document.querySelector('#todo')
      const todo = todoElement.value

      if (todo.trim()) {
        // 문자열이 있다면
        const liElement = document.createElement('li')
        liElement.innerText = todo

        const ulElement = document.querySelector('ul')
        ulElement.appendChild(liElement)

        todoElement.value = ''      
      }
      else {
        alert('할일을 입력해주세요')
      }
    })
</script>
```

