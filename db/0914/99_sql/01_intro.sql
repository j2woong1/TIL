/* SQL 구문 : 대소문자 구분
기본 문법 (변하지 X) : 대문자
변하는 부분 : 소문자
*/
-- 데이터 전체 조회 --
SELECT * FROM examples;

-- 테이블 생성 --
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- 테이블 삭제 --
DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- 데이터 입력 --
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

SELECT * FROM classmates;

INSERT INTO classmates VALUES ('홍길동', 30, '서울');

SELECT rowid, * FROM classmates;

CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');

SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates;

-- 테이블 삭제 --
DELETE FROM classmates WHERE rowid=5;
INSERT INTO classmates VALUES ('최전자', 28, '부산');

-- 데이터 수정 --
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age >= 30 AND last_name='김';

SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age>=30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age>=30;

SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%-5114-%';

SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;

CREATE TABLE articles(
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번 내용');

ALTER TABLE articles RENAME TO news;
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;

ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news VALUES ('제목', '내용', datetime('now'));
SELECT * FROM news;

ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '임시제목';

