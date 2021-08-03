# 1. Semantic Tag

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="header">
    <h1>header</h1>
  </header>
  <nav class="nav">
    <h2>nav</h2>
  </nav>
  <div class="clearfix">
    <section class="section">
      <h2>section</h2>
      <article class="article1">
        <h3>article1</h3>
      </article>
      <article class="article2">
        <h3>article2</h3>
      </article>
    </section>
    <aside class="aside">
      <h2>aside</h2>
    </aside>
  </div>  
  <footer class="footer">
    <h2>footer</h2>
  </footer>
</body>
</html>

```

## CSS

```css
/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */

.article1, .article2 {
  background-color: white;
}

.header, .nav, .footer, .section, .aside {
  background-color: lightgray;
}

/* 2. header, nav, footer 태그의 margin을 4px로 만들어주세요. */

/* 3. header, nav, footer 태그의 padding을 4px로 만들어주세요. */

.header, .nav, .footer {
  margin: 4px;
  padding: 4px;
}

/* 4. h1 태그를 수평 중앙 정렬 시켜주세요. */

.header {
  text-align: center;
}

/* 5. section 태그는 width 490px height 300px, 
   aside 태그는 width 280px height 300px로 만들어주세요.*/

.section {
    width: 490px;
    height: 300px;
}
  
.aside {
    width: 280px;
    height: 300px;
}

/* 6. 모든 semantic 태그의 border 두께를 1px, 실선, 검은색으로 만들어주세요. */

/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */

.header, .nav, .footer, .section, .aside, .article1, .article2 {
  border: 1px;
  border-style: solid;
  border-color: black;
  border-radius: 4px;
}
```

