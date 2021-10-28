## JavaScript 기초

> 템플릿 코드를 통해 제시된 기능을 충족하는 todo app 을 완성하시오
>
> - [필수사항]
>   - TODO 아이템을 추가할 수 있다
>   - 아이템 클릭을 통해 아이템에 취소선을 추가하거나 제거할 수 있다
>   - x 버튼을 통해 아이템을 삭제할 수 있다
> - [선택사항]
>   - 빈 값의 데이터 입력 방지
>   - 빈 값 입력 시 브라우저 팝업 출력하기
>   - 데이터 작성 후 input value 초기화

```html
<script>
  const form = document.querySelector('form')

  function addTodo (event) {
    // 이벤트를 취소한다.
    event.preventDefault()

    // 입력 element를 찾고 해당 입력 element의 value 값을 저장한다.
    const input = document.querySelector('input')
    const content = input.value

    if (content.trim()) {
      // li element를 생성 후 input element의 value 값을 데이터로 저장한다
    
      const liTag = document.createElement('li')
      liTag.innerText = content

    // ul 태그의 자식 태그로 위에서 생성한 li element를 넣는다.
      const ulTag = document.querySelector('ul')
      ulTag.appendChild(liTag)

    // 삭제 버튼을 생성 후 li 태그의 자식 태그로 넣는다.
      const myButton = document.createElement('button')
      myButton.innerText = 'X'
      liTag.appendChild(myButton)

    // 삭제 버튼을 클릭하면 해당 li element를 삭제한다
      myButton.addEventListener('click', function (event) {
        event.target.parentElement.remove()
      })

    // li element를 클릭하면 취소선이 토글된다.
      liTag.addEventListener('click', function (event) {
        console.log(event)
        event.target.classList.toggle("done")
      })
    } else {
      alert('할 일을 입력해주세요.')
    }
    event.target.reset()
  }
    

  form.addEventListener('submit', addTodo)
</script>
```

