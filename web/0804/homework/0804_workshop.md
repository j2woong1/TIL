# Bootstrap Component

- flexbox

```css
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
```



## 1. Nav

```css
<!-- 1. Nav -->
  <nav class="fixed-top bg-dark d-flex justify-content-between">
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>
    <ul class="d-flex align-items-center mb-0 me-3 list-unstyled">
      <li><a href="#" class="mx-3 text-decoration-none text-white">Home</a></li>
      <li><a href="#" class="mx-3 text-decoration-none text-white">Community</a></li>
      <li><a href="#" class="mx-3 text-decoration-none text-white">Login</a></li>
    </ul>
  </nav>
```

- fixed-top : 최상단 고정
- bg-dark : 배경색
- d-flex : flex
- justify-content-between : 양 끝 배치
- mx-3 : left, right에 1rem 만큼 margin
- text-decoration-none : 밑줄 제거



## 2. Header

```css
<!-- 2. Header -->
  <header class="d-flex flex-column justify-content-center align-items-center">
      <div class="display-1 text-white fw-bold">Cinema</div>
      <div class="display-1 text-white fw-bold">Community</div>
      <a href="#" class="btn btn-primary btn-lg mt-4">Let's Go</a>
  </header>
```

- flex-column justify-content-center align-items-center : 수직, 수평 중앙
- text-white fw-bold: 폰트 흰색, 굵게
- btn-primary btn-lg : 버튼 파란색, 크기 크게



## 3. Section

```css
<!-- 3. Section -->
  <section>
    <h2 class="text-center my-5">Used Skills</h2>
    <article class="d-flex justify-content-center">
      <div class="mx-5 text-center">
        <img src="images/web.png" alt="Web Image">
        <p>Web</p>
      </div>
      <div class="mx-5 text-center">
        <img src="images/html5.png" alt="HTML5 Image">
        <p>HTML5</p>
      </div>
      <div class="mx-5 text-center">
        <img src="images/css3.png" alt="CSS3 Image">
        <p>CSS3</p>
      </div>
    </article>
  </section>
```

- text-center my-5 : 수평 중앙
- justify-content-center : 간격 동일



## 4. Footer

```css
<!-- 4. Footer -->
  <footer class="fixed-bottom bg-primary d-flex justify-content-center align-items-center text-white">
    <p class="mb-0">HTML & CSS project. Created by JJW</p>
  </footer>
```

- fixed-bottom : 최하단 고정
- bg-primary : 파란색
- justify-content-center align-items-center : 수직, 수평 중앙