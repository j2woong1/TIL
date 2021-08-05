# Grid System & Responsive Web

## 1. CSS flex-direction

- `row` : 수평(좌우) 메인 축
- `row-reverse` : `row` 수평 반전
- `column` : 수직(상하) 메인 축
- `column-reverse` : `column`  수평 반전



## 2. Bootstrap flex-direction

| CSS              | bootstrap class       |
| ---------------- | --------------------- |
| `row`            | `flex-row`            |
| `row-reverse`    | `flex-row-reverse`    |
| `column`         | `flex-column`         |
| `column-reverse` | `flex-column-reverse` |



## 3. Align-items

- `flex-start`: 요소 -> 컨테이너의 꼭대기 정렬
- `flex-end`: 요소 -> 컨테이너의 바닥 정렬
- `center`: 요소 -> 컨테이너의 세로선 상의 가운데 정렬
- `baseline`: 요소 -> 컨테이너의 시작 위치 정렬
- `stretch`: 요소 -> 컨테이너에 맞도록 늘림



## 4. flex-flow

`flex-direction` + `flex-wrap`



## 5. Bootstrap Grid System

```html
<div class="container">
	<div class="row">
		<div class="col-md-1"><div>
	<div>
<div>
```



## 6. Breakpoint prefix

- (c) : `공백`, `sm`, `md`, `lg`

| Extra small | Small   | Medium  | Large   | X-Large  | XX-Large |
| ----------- | ------- | ------- | ------- | -------- | -------- |
| < 576px     | ≥ 576px | ≥ 768px | ≥ 992px | ≥ 1200px | ≥ 1400px |
| `-`         | `sm`    | `md`    | `lg`    | `xl`     | `xxl`    |

- (d) : 1~12