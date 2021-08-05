# 1. Flex Box

## Justify-Content : 가로 정렬

- `flex-start`: 요소 -> 컨테이너의 왼쪽 정렬
- `flex-end`: 요소 -> 컨테이너의 오른쪽 정렬
- `center`: 요소 -> 컨테이너의 가운데 정렬
- `space-between`: 요소 사이 동일한 간격
- `space-around`: 요소 주위 동일한 간격

![image-20210805093034282](0805_practice.assets/image-20210805093034282.png)

```css
justify-content: flex-end;
```

![image-20210805093209484](0805_practice.assets/image-20210805093209484.png)

```css
justify-content: center;
```

![image-20210805093329225](0805_practice.assets/image-20210805093329225.png)

```css
justify-content: space-around;
```

![image-20210805093416355](0805_practice.assets/image-20210805093416355.png)

```css
justify-content: space-between;
```

## Align-Items : 세로 정렬

- `flex-start`: 요소 -> 컨테이너의 꼭대기 정렬
- `flex-end`: 요소 -> 컨테이너의 바닥 정렬
- `center`: 요소 -> 컨테이너의 세로선 상의 가운데 정렬
- `baseline`: 요소 -> 컨테이너의 시작 위치 정렬
- `stretch`: 요소 -> 컨테이너에 맞도록 늘림

![image-20210805093457629](0805_practice.assets/image-20210805093457629.png)

```css
align-items: flex-end;
```

![image-20210805093540199](0805_practice.assets/image-20210805093540199.png)

```css
justify-content: center;
align-items: center;
```

![image-20210805093632385](0805_practice.assets/image-20210805093632385.png)

```css
justify-content: space-around;
align-items: flex-end;
```

## Flex-Direction : 정렬 방향

- `row`: 요소 -> 텍스트의 방향과 동일하게 정렬
- `row-reverse`: 요소 -> 텍스트의 반대 방향으로 정렬
- `column`: 요소 -> 위에서 아래로 정렬
- `column-reverse`: 요소 -> 아래에서 위로 정렬

![image-20210805093707249](0805_practice.assets/image-20210805093707249.png)

```css
flex-direction: row-reverse;
```

![image-20210805093755502](0805_practice.assets/image-20210805093755502.png)

```css
flex-direction: column;
```

![image-20210805094243197](0805_practice.assets/image-20210805094243197.png)

```css
flex-direction: row-reverse;
justify-content: flex-end;
```

![image-20210805094414139](0805_practice.assets/image-20210805094414139.png)

```css
flex-direction: column;
justify-content: flex-end;
```

![image-20210805094510236](0805_practice.assets/image-20210805094510236.png)

```css
flex-direction: column-reverse;
justify-content: space-between;
```

![image-20210805094619447](0805_practice.assets/image-20210805094619447.png)

```css
flex-direction: row-reverse;
justify-content: center;
align-items: flex-end;
```

## Order : 요소 순서

![image-20210805094702581](0805_practice.assets/image-20210805094702581.png)

```css
.yellow {
	order: 1;
}
```

![image-20210805094812877](0805_practice.assets/image-20210805094812877.png)

```css
.red {
	order: -1;
}
```

## Align-Self

- 개별 요소에 적용
-  `align-items`가 사용하는 값들을 인자

![image-20210805094906665](0805_practice.assets/image-20210805094906665.png)

```css
.yellow {
	align-self: flex-end;
}
```

![image-20210805094957186](0805_practice.assets/image-20210805094957186.png)

```css
.yellow {
    align-self: flex-end;
    order: 1;
}
```

## Flex-Wrap : 한 or 여러 줄

- `nowrap`: 모든 요소 -> 한 줄에 정렬
- `wrap`: 요소 -> 여러 줄에 정렬
- `wrap-reverse`: 요소 -> 여러 줄 반대로 정렬

![image-20210805095046191](0805_practice.assets/image-20210805095046191.png)

```css
flex-wrap: wrap;
```

![image-20210805095138421](0805_practice.assets/image-20210805095138421.png)

```css
flex-direction: column;
flex-wrap: wrap;
```

## Flex-Flow : Flex Direction + Flex Wrap

![image-20210805095221064](0805_practice.assets/image-20210805095221064.png)

```css
flex-flow: column wrap;
```

## Align-Content : 세로 여분 공간 -> 컨테이너 사이 공간 조절

- `flex-start`: 여러 줄 -> 컨테이너의 꼭대기 정렬
- `flex-end`: 여러 줄 -> 컨테이너의 바닥에 정렬
- `center`: 여러 줄 -> 세로선 상의 가운데에 정렬
- `space-between`: 여러 줄 사이 동일한 간격
- `space-around`: 여러 줄 주위 동일한 간격
- `stretch`: 여러 줄 -> 컨테이너에 맞도록 늘림



**Align-Content : 여러 줄 사이 간격**

**Align-Items: 요소 정렬**

![image-20210805095304280](0805_practice.assets/image-20210805095304280.png)

```css
flex-wrap: wrap;
align-content: flex-start;
```

![image-20210805095356867](0805_practice.assets/image-20210805095356867.png)

```css
flex-wrap: wrap;
align-content: flex-end;
```

![image-20210805095454534](0805_practice.assets/image-20210805095454534.png)

```css
flex-wrap: wrap;
flex-direction: column-reverse;
align-content: center;
```

![image-20210805095630236](0805_practice.assets/image-20210805095630236.png)

```css
flex-flow: column-reverse wrap-reverse;
justify-content: center;
align-content: space-between;
```



# 2. Responsive Web

![image-20210805174104758](0805_practice.assets/image-20210805174104758.png)

- nav : 최상단 고정

```html
<nav class="navbar navbar-light bg-light w-100 sticky-top fw-bold">
    <div class="container-fluid">
      <a class="navbar-brand">SAMSUNG</a>
      <div class="d-flex">
        <a href="#" class="text-decoration-none text-black me-5">Contact</a>
        <a href="#" class="text-decoration-none text-black me-5">Cart</a>
        <a href="#" class="text-decoration-none text-black me-5">Login</a>
      </div>
    </div>
  </nav>
```

- 768 미만 : 1개 / 768 이상 992 미만 : 2개 / 992 이상 : 4개

```html
<article>
      <h4 class="text-center fw-bold my-5">Our New Products</h4>
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4 text-center">
        <div class="col">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="">
            <div class="card-body">
              <h5 class="card-title">Buds</h5>
              <p class="card-text">179,000</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="">
            <div class="card-body">
              <h5 class="card-title">Buds</h5>
              <p class="card-text">179,000</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="">
            <div class="card-body">
              <h5 class="card-title">Buds</h5>
              <p class="card-text">179,000</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="">
            <div class="card-body">
              <h5 class="card-title">Buds</h5>
              <p class="card-text">179,000</p>
            </div>
          </div>
        </div>
      </div>
    </article>
```

- SNS 연결

```html
<footer class="d-flex justify-content-center my-5">
      <a href="https://www.instagram.com/" class="mx-2">
        <img src="images/instagram.png" alt="" class="icon-size">
      </a>
      <a href="https://www.facebook.com/" class="mx-2">
        <img src="images/facebook.png" alt="" class="icon-size">
      </a>
      <a href="https://www.twitter.com/" class="mx-2">
        <img src="images/twitter.png" alt="" class="icon-size">
      </a>
</footer>
```

