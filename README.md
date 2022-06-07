# 33기 1차 프로젝트 1팀 남바완
![namba1_logo](https://user-images.githubusercontent.com/72453080/171790066-206e9591-15f3-4ba0-97be-413f21d13694.png)

[🍽️시연영상 보러가기](https://youtu.be/KlmscbOsnMc)
[🍽️배포 바로가기](http://35.89.113.177:8000/)
<br/>

## 🌼 프로젝트 소개 🌼


* 밀키트를 판매하는 커머스 사이트를 선정했습니다.
* 짧은 기간동안 개발에 집중할 수 있도록 디자인과 기획 일부를 [쿡킷 사이트](https://www.cjcookit.com/pc/main)를 참조하여 학습목적으로 만들었습니다.
* 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다.

<br/>

## 🌼 개발 인원 및 기간 🌼
**개발기간** : 2022/05/24~2022/06/04

<br/>

**개발인원 및 파트** : 
#### Frontend
- 김혜수 🐷 : Signup Page, Signin Page, Footer
- 박주영 🍋 : Review Page
- 천은별 🌟 : Menu Page
- 최현민 🐜 : Main Page, Nav

#### Backend
- 임한구 🎅🏻

<br/>

## 🌼 기술 🌼
**Front-End** : React.js 
<br/>
**Back-End** : Python, Django web framework, Bcrypt, MySQL, pyjwt, AWS
<br/>
**Common** : Git-Hub, slack, trello

<br/>

## 🌼 페이지별 구현 사항 🌼

### Users APP
#### 1. SignupView
 - POST메소드로 body에서 json을 담아 통신
 - 정규표현식 총 4개 : <br>
   - 이메일 ('@','.' 순서대로 포함하는 양식)
   - 비밀번호(숫자,영문,특수문자 1자 이상 총 8자 이상)
   - 핸드폰번호(01로시작하며 세번째자리가 0,1,6,7,8,9중 1개인 정수 - 3~4자리정수 - 4자리정수)
   - 생년월일(년도4자리 - 월 - 일)
 - 각각의 정규표현식을 통과못할때 에러메세지 반환기능
 - bcrypt hashpw메소드를 활용해 비밀번호 암호화 기능 
 - 기타사항 : eamil은 unique, agreemanet는 json형태로 받아 저장
#### 2. LoginView
 - POST메소드로 body에서 json을 담아 통신
 - 이메일, 비밀번호 정규표현식 기능
 - bcrypt의 checkpw메소드로 비밀번호 확인기능
 - 비밀번호 확인후 jwt패키지 활용하여 token발행하여 성공메세지와 함께 반환


### Products APP
#### 1. ProductListView
 - GET메소드를 활용, queryparameter활용
 - 상품 theme관련 filter기능 
 - 상품 정렬 기능(새상품, 가격내림/오름순) 
 - 상품검색 기능 
 - 패킹/언패킹을 이용한 request의 queryparameter 값들을 ORM의 키워드파라미터로 전달
 - 기타사항 : 메뉴리스트에서만 사용하는것이 아닌 main페이지에서도 같이 사용

#### 2. ProductDetailView
 - GET메소드를 활용, pathparameter활용
 - ProductListView에서 반환해준 product의 id값을 request에 담아 요청할시 path를 받아 조회하여 해당 detail값을 반환
 - 기타사항 : 메뉴리스트에서만 사용하는것이 아닌 main페이지에서도 같이 사용


### Orders APP
#### 1. CartView
 - READ : GET메소드 활용, userid로 조회, user_id는 token을 이용하여 획득, total_price는 DB에 저장하지는 않지만 price와 quantity를 이용해 계산하여 반환
 - CREATE : POST메소드 활용, body에서 json형식으로 제품id와 수량을 받고 token을 이용해 id값을 추가해 DB에 저장, get_or_create 메소드를 활용 존재하지않을땐 생성하고, 이미 존재할땐 수량만 업데이트
 - UPDATE : PATCH메소드 활용, pathparameter에서 주는 cart_id와 token을 이용한 user_id를 이용해 DB조회후 json데이터로 보내준 제품수량 수정
 - DELETE : DELETE메소드 활용, token에서 받은 user_id, pathparameter로 받은 cart_id를 이용해 DB조회하여 delete메소드 활용해서 삭제

### Reviews APP
#### 1. ReviewView
 - 로그인한사람만 작성할 수 있도록 데코레이터로 token검사 
 - CREATE : POST메소드 활용, json으로 title,content,product_id를 받아 저장, 이미지정보도 실제로 받아 저장하고자 하였으나 이번 1차프로젝트에서는 미구현(더미데이터 활용)
 - READ : GET 메소드 활용, 페이지네이션 기능활용 10페이지씩 반환, 리뷰 검색기능, 포토리뷰만 필터기능, 딕셔너리패킹, 언패킹을 이용한 if문 활용
 - UPDATE : PATCH메소드 활용, pathparameter에서 주는 review_id와 token을 이용한 user_id를 이용해 DB조회후 json데이터로 보내준 리뷰내용으로 수정
 - DELETE : DELETE메소드 활용, token에서 받은 user_id, pathparameter로 받은 review_id를 이용해 DB조회하여 delete메소드 활용해서 삭제


<br/>

## 🌼 프로젝트 진행 과정 🌼
||Trello|Daily Standup Meeting|
|------|---|---|
|협업 방식|칸반보드를 활용한 회의록 작성 및 진행상황 공유|매일 아침 30분동안 진행사항과 오늘 할 작업 내용 공유|
|IMG|![image](https://user-images.githubusercontent.com/72453080/172017656-5a83e3f5-34c4-44b8-b600-39ed7c6600d0.png)|![image](https://user-images.githubusercontent.com/72453080/172017691-c160d276-3004-4dbc-966b-d761d8c749b8.png)|



