# Bootstrap

## 1. Component

![image-20210804174717367](0804_homework.assets/image-20210804174717367.png)

```html
<div class="d-grid gap-2 col-6 mx-auto p-5">
        <button class="btn btn-success" type="button">Sign in</button>
    </div>
```

- block button : d-grid gap-2
- half-width : col-6
- center horizontally : mx-auto
- green button : btn-success

## 2. Component

![image-20210804185953659](0804_homework.assets/image-20210804185953659.png)

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><img class="ms-1" src="C:\Users\j2woo\Desktop\ssafy6\3. hws\0804\logo.png" width=50 alt="ssafy"></a>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  프로젝트
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <!-- <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li> -->
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  그룹툴
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                </ul>
              </li>
              <li class="nav-item ms-2">
                <a class="nav-link active" aria-current="page" href="#">활동</a>
              </li>
              <li class="nav-item ms-1">
                <a class="nav-link active" aria-current="page" href="#">마일스톤</a>
              </li>
              <li class="nav-item ms-2">
                <a class="nav-link active" aria-current="page" href="#">스니펫</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
```



## 3. Component

![image-20210804190044294](0804_homework.assets/image-20210804190044294.png)

```html
<nav aria-label="...">
        <ul class="pagination fw-bold justify-content-center">
          <li class="page-item disabled">
            <a class="page-link text-grey" href="#" tabindex="-1" aria-disabled="true">Prev</a>
          </li>
          <li class="page-item active"><a class="page-link" href="#">1</a></li>
          <li class="page-item" aria-current="page">
            <a class="page-link text-dark" href="#">2</a>
          </li>
          <li class="page-item"><a class="page-link text-dark" href="#">3</a></li>
          <li class="page-item"><a class="page-link text-dark" href="#">4</a></li>
          <li class="page-item">
            <a class="page-link text-dark" href="#">Next</a>
          </li>
        </ul>
      </nav>
```



## 4. Login Page

```html
<div class="container">
        <div class="row">
          <div class="col-6 m-2">
            <div class="alert alert-danger d-flex flex-row align-items-center" role="alert">
              Invalid Login or password.
            </div>
            <div class="h1 fw-bold">
              SSAFY 전용 GitLab 시스템
            </div>
            <hr class="mb-4">
            <div class="border border-2 rounded">
              <div class="p-3 d-flex justify-content-center">
                <span class="fw-bold">Sign in</span>
              </div>
              <hr class="m-0" style="color: blue">
              <form class="px-4 py-3">
                <div class="mb-3">
                  <label for="exampleDropdownFormEmail1" class="form-label fw-bold">Username or email</label>
                  <input type="email" class="form-control" id="exampleDropdownFormEmail1" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                  <label for="exampleDropdownFormPassword1" class="form-label fw-bold">Password</label>
                  <input type="password" class="form-control" id="exampleDropdownFormPassword1" placeholder="Password">
                </div>
                <div class="mb-3 d-flex flex-row justify-content-between">
                  <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="dropdownCheck">
                    <label class="form-check-label" for="dropdownCheck">
                      Remember me
                    </label>
                  </div>
                  <a href="#" class="text-decoration-none">Forgot your password?</a>
                </div>
              <div class="d-grid col-12 mx-auto">
                  <button class="btn btn-success" type="button">Sign in</button>
              </div>
              </form>
            </div> 
          </div> 
        </div>
      </div>
```

