# 28_workshop

## 문제1

|        CRUD         | HTTP Method |            URL            |
| :-----------------: | :---------: | :-----------------------: |
|    리소스의 목록    |     GET     |     ```/articles/```      |
|    리소스의 생성    |    POST     |      ```/article/```      |
| 리소스 중 하나 표시 |     GET     | ```/articles/<int:pk>/``` |
|     리소스 수정     | PUT, PATCH  | ```/articles/<int:pk>/``` |
|     리소스 삭제     |   DELETE    | ```/articles/<int:pk>/``` |

