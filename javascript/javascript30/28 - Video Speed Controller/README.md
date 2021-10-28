## Video Speed Controller

```javascript
<script>
  const speed = document.querySelector('.speed');
  const bar = speed.querySelector('.speed-bar');
  const video = document.querySelector('.flex');

  function handleMove(e) {  // 마우스 움직일 시 함수
      const y = e.pageY - this.offsetTop;  // 마우스 위치에서 상단값 빼기
      const percent = y / this.offsetHeight;  // y값에서 총 길이 나눠서 퍼센트 도출
      const min = 0.4;  // 최소, 최대 배속
      const max = 4;
      const height = Math.round(percent * 100) + '%';  // 높이 % 조절 -> 반올림
      const playbackRate = percent * (max - min) + min; // 재생 속도 계산
      bar.style.height = height;  // 속도 변화 -> 바 게이지 높이 변하도록
      bar.textContent = playbackRate.toFixed(2) + '×';  // 속도 변화 -> 글자 변환
      video.playbackRate = playbackRate;  // 재생 속도 적용
    }

  speed.addEventListener('mousemove', handleMove);  // 마우스 움직임에 따라 기능 구현
</script>
```

![image-20211027155609498](C:\Users\j2woo\AppData\Roaming\Typora\typora-user-images\image-20211027155609498.png)

- 마우스 이동으로 영상 재생 속도 조절
  - 우측 바에서 마우스로 흰색 바의 높낮이를 조절하여 영상 속도 조절 기능
- `HTMLMediaElement.playbackRate`
  - 정상 속도 X Value = 현재 속도, 정상 속도 = 1
  - 재생 속도 음수 -> 재생 X

