# 1. Semantic Tag

- header, section, footer + aside, nav, article



# 2. Input Tag

```html
<form action="#">
	<label for="username">USERNAME: </label>
    <input type="text" id="username" placeholder="아이디를 입력해주세요.">
    <br>
    <label for="password">PWD: </label>
    <input type="password" id="password">
    
    <input type="submit" value="로그인"
</form>
```



# 3. 크기 단위

- rem



# 4. 선택자

```html
<!-- 자손 결합자 : 모든 상속관계에 적용-->
div p {
	color: crimson;
}

<!-- 자식 결합자 : 바로 하단관계에 있는 상속 관계에만 적용--> 
div > p {
	color: crimson;
}
```

