# Maven on Ecllipse 학습



## 1. 메이븐(Maven)이란?

### Maven 이란?

- 프로젝트를 만들 때, 가장 많이 사용하는 빌드 툴 중에 하나임
- 프로젝트 빌드 툴

### 프로젝트 빌드 과정

- 프로젝트 생성 > 라이브러리 설정 > 코드 작업 > 컴파일 > 테스트 > 패키지 만들기 > 배포 > 레포팅
- 이런 빌드 과정들에서 반복되는 부분들을 효율적으로 할 수 있도록 도와주는게 빌드 툴
- 메이븐을 사용하면 빌드 과정을 경량화해서 쉽게 구현할 수 있음

### IDE와 별개인 빌드 도구

- 그런데 이클립스도 프로젝트 생성하고 라이브러리 설정하고, 코드 작업, 컴파일, 테스트같은 것들을 할 수 있지 않나?
  - 이클립스도 빌드 툴 아닌가?
  - 이클립스나 비쥬얼스튜디오코드, Intellij 등은 빌드 툴이 아님
    - IDE라고 함
    - 개발 통합 환경이라고 할 수 있음
- 메이븐은 특정 IDE에 종속된 것이 아니라 빌드라는 것을 도와주는 역할에 특화된 도구임
  - 이클립스나 비쥬얼스튜디오코드, Intellij 등 IDE가 메이븐을 이용할 수 있음
  - 메이븐에 없는 편집기능, 디버깅 기능, 협업관련 기능 등은 IDE를 통해서 사용

![1](Maven_images/1.png)

### Build Tool in IDE(Eclipse, VS Code, etc)

- 그러면 이클립스에서 프로젝트를 만드는게 메이븐을 사용한 것인가?
  - 꼭 그런것은 아님
  - 그렇게 할 수도 있고, 안 할수도 있음

![2](Maven_images/2.png)

### 최근 IDE에 프로젝트 관리와 관련되어 포함되어 있는 전문화된 도구들

- IDE에 형상관리, 빌드관리, 테스트관리 툴 등의 전문 도구들을 올려서 사용하게 됨
- 프로젝트 생성 같은 기능 등이 이클립스에도 이미 있는데 굳이 메이븐을 사용하는 이유는 뭔가?
  - 메이븐을 사용해보면 그 이유를 알게 됨

![3](Maven_images/3.png)

### 이클립스가 제공하지 않는 Maven만의 기능

![4](Maven_images/4.png)



## 2. Maven 설치하기

- homebrew로 설치하기
- 설치 확인

![5](Maven_images/5.png)



## 3. Maven으로 자바 프로젝트 생성하기

### Maven 자바 프로젝트 생성

![6](Maven_images/6.png)

![7](Maven_images/7.png)

- 코드

```shell
mvn archetype:generate -DgroupId=com.newlecture -DartifactId=javaprj -DarchetypeArtifactId=maven-archetype-quickstart
```

- 결과

![8](Maven_images/8.png)



## 4. 컴파일과 실행하기







## 참고

- 유튜브 뉴렉처 채널
  - 재생목록 - 메이븐 