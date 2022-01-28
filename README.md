# 프로젝트 Descroption

에이블러를 위한 스터디 게시판 구현

&nbsp;
### 환경 설치

채팅 사용을 위한 설치

```
docker run -p 6379:6379 -d redis:5(도커의 redis를 사용함)

python -m pip install -U channels

python -m pip install channels_redis
```

다른 포트 연결

```
redis 서버를 다시만들고 config 부분에 CHANNEL_LAYERS 부분 구성을 다시해줌
```

## 프로젝트 정보

windows 환경에서 VSCode를 사용하여 개발

&nbsp;
### 개발 환경 및 사용 기술

개발 언어

```
Python,HTML,CSS,JavaScript
```
framework
```
Django
```

Django Channel을 이용하여 웹소켓 연동
```
도커에 redis port를 구성하여 Django와 연동하여 웹소켓을 사용함
```

## 프로젝트 결과물

기능 및 결과 예시 화면
&nbsp;

### 회원가입/로그인/로그아웃 구현
```

```
### 실시간 채팅 구현
```

```
### Q&A 및 자유게시판 구현
```

```
### Ranking 시스템
```
![랭크](https://user-images.githubusercontent.com/96154446/151490568-d780c1b8-793f-4342-8f96-175f9d3d97d8.PNG)

```
### 학습 
```
- AIVLE 수업 때 수강했던 모든 강의 및 PDF 다운 지원
![aivle 강의](https://user-images.githubusercontent.com/96154446/151490651-b039e1c6-eadd-4266-b576-c1f0236a687d.PNG)

```
### 퀴즈 구현
```

```



