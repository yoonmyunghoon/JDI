# OAuth

- API를 이용해서 다른 서비스에 있는 정보를 내가 만들고 있는 앱에 가지고 와서 무엇인가를 할 수 있음
- 이때 다른 서비스에 있는 정보가 아무에게나 공개된 정보가 아니라 개인 사용자들의 정보라고 하면 그것을 사용하기 위해서는 그 사용자의 허락과 해당 정보를 가지고 있는 서비스에서 제시하는 절차를 따라야함
- 여기서 말하는 절자를 OAuth라고 함



## OAuth에 관련된 3개의 주체

- Client: 내가 서비스하고 있는 app or web
- Resource Owner: 내 서비스를 이용하고 있는 사용자
- Resource Server: facebook, google 등 해당 사용자의 정보를 가지고 있는 서비스



## 동작 메커니즘

1. C가 RS에게 정보를 사용하고 싶다고 말함
2. RS가 C에게 Client ID와 Client Secret을 발급해줌
   - Client Secret는 절대 공개되면 안됨
3. C가 RO에게 RS에서 정보를 사용하는 것을 허락해달라고 요구
4. RO는 RS 사이트에 들어가서 동의 버튼을 누름
5. RS가 C에게 code라는 것을 줌
   - RO가 C에게 정보를 제공하는것을 승인했다는 것을 의미하는 것
   - 허락해줬다는 의미
   - 비밀번호 같은 것
6. C는 Client ID, Client Secret, code 이렇게 세가지를 다시 RS에게 보냄
7. RS는 C가 사용자가 허락해준 C인지 검증
8. 검증이 완료되면 RS는 C에게 access token을 발급해줌
   - access token이 진짜 비밀번호라고 할 수 있음
9. C는 access token을 파일이나 데이터베이스에 소중하게 저장함
10. 그 뒤로는 C는 access token을 통해 RS에게 필요한 정보를 요청함
11. RS는 해당 토큰이 발급했던 적이 있는지 확인하고 맞다면 해당 정보를 제공해줌
12. C는 제공받은 데이터를 가공해서 RO에게 가치를 제공해줌



## API 접속하기(구글)

- 구글 클라우드 플랫폼 접속 > 프로젝트 생성 > 사용자 인증 정보 만들기 > OAuth 클라이언트 ID 선택
- 구글이 가지고 있는 전체 정보 중에서 사용할 정보, scope를 설정
- 요청 url을 제공해줌, 단, api key(access token)가 있어야 해당 데이터를 얻을 수 있음

![OAuth](/Users/yoonmyunghoon/JDI/ITknowledge/images/OAuth.png)





## 참고

생홯코딩: https://opentutorials.org/course/2473/16571







