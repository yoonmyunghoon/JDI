# 협업 필터링 추천 시스템(Collaborative Filtering Recommendation System)

- 넷플릭스, 아마존 등 대부분의 서비스 기업이 추천 시스템을 사용함
- 추천 시스템을 구현하는 방법에는 크게 두 가지가 있다.
  - 협업 필터링(Collaborative Filtering)
  - 컨텐츠 기반 필터링(Content-based Filtering)
    - 컨텐츠 자체의 내용을 기반으로 비슷한 컨텐츠를 추천해줌
    - 예를 들어 사용자가 마블사의 영화를 봤다면, 이를 기반으로 마블사의 다른 영화를 추천해 줄 수 있음
    - 혹은 텍스트 기반의 컨텐츠에서는 TF-IDF와 같은 방법을 사용할 수도 있음

## 협업 필터링(Collaborative Filtering)

- 어떤 특정한 인물 A가 한가지 이슈에 관해서 인물 B와 같은 의견을 갖는다면 다른 이슈에 대해서도 비슷한 의견을 가질 확률이 높을 것이라는 사실에 기반
- 기본적으로 협업 필터링의 종류에는 Memory-based, Model-based, Hybrid가 있지만 이중에서 간단하게 구현할 수 있으며, 적당히 합당한 결과를 도출하는 Memory-based 협업 필터링에 대하여 알아보자

## Memory-based 협업 필터링

- Memory-based 협업 필터링의 추천 시스템은 유사도를 기반으로 동작함
- 사용자-사용자 간의 유사도를 기준으로 하는 경우는 사용자 기반(User-Based)
- 아이템-아이템 간의 유사도를 기준으로 하는 경우는 아이템 기반(Item-Based)
- 유사도는 코사인 유사도, 피어슨 유사도 등을 사용함









## 참고

https://scvgoe.github.io/2017-02-01-%ED%98%91%EC%97%85-%ED%95%84%ED%84%B0%EB%A7%81-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-(Collaborative-Filtering-Recommendation-System)/

