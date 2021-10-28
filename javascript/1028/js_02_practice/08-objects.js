/*
  [Object 요소 접근 연습]
  
	주어진 object에서 items의 첫번째 아이템의 name을 result 변수에 할당하세요.
*/

const data = {
  id: 42,
  items: [
    {
      id: 1,
      name: 'foo',
    },
    {
      id: 2,
      name: 'bar',
    },
  ],
}

// A.
data.items[0].name

/*
[Object 축약 문법]

아래 변수들을 속성으로 가지는 Object를 축약문법을 활용하여 작성하세요.
*/

const username = 'hailey'
const contact = '010-1234-5678'

// A.
const user = {
  username,
  contact,
}

/*
[Object Destructuring]

주어진 함수를 Object 축약 문법과, destructuring을 사용하여 재작성하세요.
*/

const users = [
  {
    name: 'hailey',
    contact: '010-1234-5678',
    age: 25,
  },
  {
    name: 'paul',
    contact: '010-5678-1234',
    age: 27,
  },
]

function saveUserData (users) {
  const userData = users.map((user, index) => {
    return { id: index, name: user.name, contact: user.contact }
  })

  return userData
}

// A.
function saveUserData (users) {
  return users.map(({ name, contact }, index) => ({
    id: index,
    name,
    contact,
  })
)}
