# SQL vs NoSQL

 ## NoSQL ??

- Not only SQL
- Not SQL
- 딱 한가지 종류의 DB만을 의미하는 것이 아님
- 거대한 DB의 그룹이라고 할 수 있음
- 한국음식 vs Non 한국음식



## SQL

- MySQL, PostgreSQL, SQLite ...
- 조금씩 다르지만 결국엔 SQL이라는 점에서는 같음



## NoSQL의 종류 ??

![NoSQL](images\NoSQL.png)

https://docs.microsoft.com/ko-kr/dotnet/architecture/cloud-native/relational-vs-nosql-data

### 1. Document

- mongoDB
  - 데이터를 json document 형태로 저장
  - 원하는 어떤 종류의 어떤 모양의 데이터든 저장할 수 있음

### 2. Graph

- column이나 document가 필요없을 때, 그러나 각 노드 사이 관계를 알아야할 때 사용됨
- 페이스북같은 소셜 네트워크를 만든다면 필요함
- document나 column을 저장하는 것이 아니라 각각의 entity를 저장하고 이를 관계망으로 연결함
- Tao
  - 페이스북이 만들었음
- neo4j

### 3. Key-Value

- CassandraDB
  - Column wide database로 유명함
  - 읽고 쓰기가 엄청 빠름
  - 애플이 카산드라를 이용해서 10페타바이트 데이터를 저장하고 있음
  - 넷플릭스, 인스타그램, 우버 등 많은 회사가 사용함
  - 이런 회사들은 엄청 많은 양의 데이터를 빠르게 저장하고 검색엔진처럼 많은 양의 데이터를 빠르게 읽어야함

- DynamoDB
  - 서버리스, 분산된 key valueDB
  - 아마존이 만들었음
  - 빠르게 쓰고 읽을 수 있음

- document DB랑의 비교
  - key value DB는 얻을 수 있는 데이터의 종류가 좀 제한적임, 저장하기 전에 DB에서 무엇을 어떻게 얻을 것인지 미리 생각해둬야함
  - SQL에서처럼 쿼리를 할 수 없음
  - 반드시 저장하기전에 어떻게 얻을 것인지 고민해야됨



## 결론

- SQL과 NoSQL을 비교하는 것은 말이 안됨
- NoSQL이 종류가 많음
- 만약 그냥 평범한 프로젝트, 화려하지 않은 프로젝트라면 거의 대부분의 경우 SQL을 선택, 대부분의 경우 SQL로 다 커버가 가능하기 때문에
- NoSQL은 특별한 경우, 특별한 이슈에 대응하기에 좋은 DB들임
- 인스타그램도 처음에는 PostgreDB를 사용하다가 엄청나게 성장하면서 graphDB로 옮겼음
- 처음에는 최대한 평범한 SQL로 시작해서 해보고 나중에 필요하면 그때가서 찾아서 바꿔도 늦지않음

