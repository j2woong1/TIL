# Responsive Web

## 01_nav_footer

### 1. navbar

```html
<nav class="navbar navbar-expand-md sticky-top bg-dark navbar-light bg-light">
    <div class="d-flex justify-content-between align-items-center container-fluid">

      <a class="navbar-brand" href="02_home.html">
        <img src="images\logo.png" alt="logo" style="width: 100px;">
      </a>  

      <button class="navbar-toggler btn-light" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="navbar-collapse justify-content-end collapse" id="navbarSupportedContent">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active mx-2 text-white fw-bold" aria-current="page" href="02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link mx-2 text-secondary fw-bold" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link mx-2 text-secondary fw-bold" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
          </li>
        </ul>
      </div> 

    </div>
  </nav>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <div class="modal-body">
          <form>

            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Username</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
              <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>

            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>

            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
        
      </div>
    </div>    
  </div>
  
<footer class="fixed-bottom bg-dark d-flex justify-content-center align-items-center">
    <p class="text-white mb-0">HTML & CSS project. Created by JJW</p>
</footer>
```

- 상단 고정 : sticky-top
- 이미지 

```html
<a class="navbar-brand" href="02_home.html">
	<img src="images\logo.png" alt="logo" style="width: 100px;">
</a>  
```

- 네비게이션 리스트 오른쪽 정렬

```html
<div class="justify-content-end collapse navbar-collapse" id="navbarSupportedContent">
```

- 클릭 가능한 링크

```html
<a class="nav-link active mx-2 text-white fw-bold" aria-current="page" href="02_home.html">Home</a> <!-- active : Home 강조 -->
```

- 768px 미만 : 햄버거 버튼, 클릭 시 세부 항목

```html
<button class="navbar-toggler btn-light" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
</button>
```

- form 내부 비밀번호 표시 X

```html
<div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
</div>
```



### 2. Footer

```html
 <footer class="d-flex fixed-bottom justify-content-center align-items-center bg-dark">
    <p class="text-white mb-0">HTML & CSS project. Created by JJW</p>
  </footer>
```

- 하단 고정 : fixed-bottom

- 수평 정렬 (왼, 오른쪽 여백 same) : justify-content-center align-items-center



## 02_home

```html
<header>
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">

      <ol class="carousel-indicators">
        <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"></li>
        <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"></li>
        <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"></li>
      </ol>

      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="1000">
          <img src="images\header1.jpg" class="d-block w-100" alt="1">
        </div>

        <div class="carousel-item" data-bs-interval="1000">
          <img src="images\header2.jpg" class="d-block w-100" alt="2">
        </div>

        <div class="carousel-item" data-bs-interval="1000">
          <img src="images\header3.jpg" class="d-block w-100" alt="3">
        </div>
      </div>

      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </a>

      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>

    </div>
    
  </header>

  <h1 class="text-center fw-bold display-1 my-5">Boxoffice</h1>

  <section class="container my-5">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">

      <article>
        <div class="card" style="width: 18rem; height: 33rem;">
          <img src="images\movie1.jpg" class="card-img-top" alt="mv1" style="width: 18rem; height: 25rem;">
          <div class="card-body">
            <p class="card-text fw-bold">Movie Title</p>
            <p class="card-text">This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </article>

      <article>
        <div class="card" style="width: 18rem; height: 33rem;">
          <img src="images\movie2.jpg" class="card-img-top" alt="mv2" style="width: 18rem; height: 25rem;">
          <div class="card-body">
            <p class="card-text fw-bold">Movie Title</p>
            <p class="card-text">This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </article>

      <article>
        <div class="card" style="width: 18rem; height: 33rem;">
          <img src="images\movie3.jpg" class="card-img-top" alt="mv3" style="width: 18rem; height: 25rem;">
          <div class="card-body">
            <p class="card-text fw-bold">Movie Title</p>
            <p class="card-text">This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </article>

      <article>
        <div class="card" style="width: 18rem; height: 33rem;">
          <img src="images\movie4.jpg" class="card-img-top" alt="mv4" style="width: 18rem; height: 25rem;">
          <div class="card-body">
            <p class="card-text fw-bold">Movie Title</p>
            <p class="card-text">This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </article>

      <article>
        <div class="card" style="width: 18rem; height: 33rem;">
          <img src="images\movie5.jpg" class="card-img-top" alt="mv5" style="width: 18rem; height: 25rem;">
          <div class="card-body">
            <p class="card-text fw-bold">Movie Title</p>
            <p class="card-text">This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </article>

      <article>
        <div class="card" style="width: 18rem; height: 33rem;">
          <img src="images\movie6.jpg" class="card-img-top" alt="mv6" style="width: 18rem; height: 25rem;">
          <div class="card-body">
            <p class="card-text fw-bold">Movie Title</p>
            <p class="card-text">This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </article>
      
    </div>
  </section>
```

### Header

- 자동으로 전환

```html
<div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="1000">
          <img src="images\header1.jpg" class="d-block w-100" alt="1">
        </div>

        <div class="carousel-item" data-bs-interval="1000">
          <img src="images\header2.jpg" class="d-block w-100" alt="2">
        </div>

        <div class="carousel-item" data-bs-interval="1000">
          <img src="images\header3.jpg" class="d-block w-100" alt="3">
        </div>
</div>
```

### Section

- 576 미만 : article 1개씩, 이상 : 2개 이상

```html
<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
```



## 03_community

```html
<div class="main">
    <h1 class="text-center fw-bold display-1 my-5">Community</h1>
    <div class="row">
      <!-- Sidebar -->
      <aside class="col-12 col-lg-2">
        <ul class="list-group">

          <li class="list-group-item text-primary">
            <a href="#" class="text-decoration-none">Boxoffice</a>
          </li>

          <li class="list-group-item text-primary">
            <a href="#" class="text-decoration-none">Movies</a>
          </li>

          <li class="list-group-item text-primary">
            <a href="#" class="text-decoration-none">Genres</a>
          </li>

          <li class="list-group-item text-primary">
            <a href="#" class="text-decoration-none">Actors</a>
          </li>

        </ul>
      </aside>

      <!-- Board -->
      <section class="col-12 col-lg-10">
        <div class="d-none d-lg-table w-100">
          <table class="table table-striped table-hover col-none col-lg-10">

            <thead class="table-dark">
              <tr>
                <th scope="col">글 제목</th>
                <th scope="col">영화 제목</th>
                <th scope="col">사용자 id</th>
                <th scope="col">작성시간</th>
              </tr>
            </thead>

            <tbody>
              <tr>
                <th scope="row">Movie Title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minutes ago</td>
              </tr>

              <tr>
                <th scope="row">Movie Title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minutes ago</td>
              </tr>

              <tr>
                <th scope="row">Movie Title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minutes ago</td>
              </tr>

              <tr>
                <th scope="row">Movie Title</th>
                <td>Movie Test</td>
                <td>user</td>
                <td>1 minutes ago</td>
              </tr>
            </tbody>

          </table>
        </div>


        <div class="d-lg-none my-5">
          <article>

            <div class="p-3 border-top border-secondary">
              <div class="d-flex flex-row justify-content-between">
                <h4 class="fw-bold">Movie Test</h4>
                <h5>user</h5>
              </div>
              <h5>Movie Title</h5>
              <h5>1 minutes ago</h5>
            </div>

            <div class="p-3 border-top border-secondary">
              <div class="d-flex flex-row justify-content-between">
                <h4 class="fw-bold">Movie Test</h4>
                <h5>user</h5>
              </div>
              <h5>Movie Title</h5>
              <h5>1 minutes ago</h5>
            </div>

            <div class="p-3 border-top border-secondary">
              <div class="d-flex flex-row justify-content-between">
                <h4 class="fw-bold">Movie Test</h4>
                <h5>user</h5>
              </div>
              <h5>Movie Title</h5>
              <h5>1 minutes ago</h5>
            </div>

            <div class="p-3 border-top border-secondary">
              <div class="d-flex flex-row justify-content-between">
                <h4 class="fw-bold">Movie Test</h4>
                <h5>user</h5>
              </div>
              <h5>Movie Title</h5>
              <h5>1 minutes ago</h5>
            </div>

          </article>
        </div>
        
      </section>
    </div>
  </div>

  <nav aria-label="Page navigation example">
    <ul class="pagination d-flex justify-content-center my-5">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
```

### Navigation Bar

- Community 강조

```html
<h1 class="text-center active fw-bold display-1 my-5">Community</h1>
```

### 게시판 목록

- 992px 이상 : 좌측 1/6 너비, 미만 : 전체 너비

```html
<aside class="col-12 col-lg-2">  
```



### 게시판

- 992px 이상 : table, 우측 5/6 너비, 미만 : article, 가로선 구분, 전체 너비

```html
<section class="col-12 col-lg-10">
          <div class="d-none d-lg-table w-100">
            <table class="table table-striped table-hover col-none col-lg-10">
            
<div class="d-lg-none my-5">
            <article>
              <div class="p-3 border-top border-secondary">
                <div class="d-flex flex-row justify-content-between">
```

- 탐색기 : 게시판과 같은 가로폭, 좌우 중앙 정렬

```html
<nav aria-label="Page navigation example">
    <ul class="pagination d-flex justify-content-center my-5">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
```

