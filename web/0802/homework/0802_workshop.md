# 1. img tag

```html
<img src="C:Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt "ssafy">
```



# 2. 파일 경로

```html
<!-- a: 절대 경로, b: 상대 경로 -->
<img src="C:Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt "ssafy">
```



# 3. Hyper Link

```html
<a href="https://www.ssafy.com">
	<img src="C:Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt "ssafy">
</a>
```



# 4. 선택자

1) Red

   ```html
   <div id="ssafy">
       <h2>어떻게 선택 될까?</h2>
       <p>첫번째 단락</p>
       <p>두번째 단락</p>
       <p>세번째 단락</p>
       <p>네번째 단락</p>
   </div>
   
   #ssafy > p:nth-child(2) { <!-- 자식 중에 2번째가 p 태그면 red로 바꿈 -->
   	color: red;
   } <!-- 첫 단락 red -->
   ```

2) Blue

   ```html
   #ssafy > p:nth-of-type(2) { <!-- p타입인 자식 중에 2번째가 p 태그면 blue로 바꿈 -->
   	color: blue;
   } <!-- 첫 단락 blue -->
   ```

3) nth-child, nth-of-type 차이점

   - nth-child : 전체 자식 중 특정 순서의 자식
   - nth-of-type : 특정 자식 중 특정 순서의 자식