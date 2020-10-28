# Docker 학습 2 - 설치 및 컨테이너 실행

![1](Docker_images/1.png)

## 1. 도커 설치하기

- 도커는 리눅스 컨테이너 기술이므로 macOS나 윈도우에 설치할 경우, 가상머신에 설치가 됨

- Docker for Mac

  - https://docs.docker.com/docker-for-mac/

  - 설치확인: docker version

  - 결과

    ```shell
    Client: Docker Engine - Community
     Cloud integration  0.1.18
     Version:           19.03.13
     API version:       1.40
     Go version:        go1.13.15
     Git commit:        4484c46d9d
     Built:             Wed Sep 16 16:58:31 2020
     OS/Arch:           darwin/amd64
     Experimental:      false
    
    Server: Docker Engine - Community
     Engine:
      Version:          19.03.13
      API version:      1.40 (minimum version 1.12)
      Go version:       go1.13.15
      Git commit:       4484c46d9d
      Built:            Wed Sep 16 17:07:04 2020
      OS/Arch:          linux/amd64
      Experimental:     false
     containerd:
      Version:          v1.3.7
      GitCommit:        8fba4e9a7d01810a393d5d25a3621dc101981175
     runc:
      Version:          1.0.0-rc10
      GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
     docker-init:
      Version:          0.18.0
      GitCommit:        fec3683
    ```

    

- 네이티브스럽게 설치된 것 같지만 도커는 리눅스 컨테이너이므로 실제로는 가상머신에 설치가 되어있음

- 그런데 그런 느낌이 안들도록 신경써서 설계함

- docker for mac은 xhyve라는 macOS에서 제공하는 가상환경을 이용함

- 버전 정보를 보면 클라이언트와 서버가 나뉘어져있음

  - 도커는 하나의 실행파일이지만 클라이언트와 서버의 역할을 각각 할 수 있음
  - 도커 커맨드를 입력하면 도커 클라이언트가 도커 서버로 명령을 전송하고 결과를 받아 터미널에 출력해줌

![5](Docker_images/5.png)

- 기본값이 도커 서버의 소켓을 바라보고 있기 때문에 사용자는 의식하지 않고 바로 명령을 내리는 것 같은 느낌을 받음
- 이런 설계 덕분에 mac이나 windows의 터미널에서 명령어를 입력했을 때 가상 서버에 설치된 도커가 동작하게 됨



## 2. 컨테이너 실행하기



https://seongjaemoon.github.io/database/2018/02/18/database-oracle6.html



## 참고

- 초보를 위한 도커 안내서
  - https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html

