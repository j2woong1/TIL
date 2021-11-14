<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation">
    </div>
    <button>회원가입</button>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {}
  },
  methods: {
    signup: function () {
      
    }
  }
}
</script>
