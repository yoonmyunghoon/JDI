# HTML, CSS, JavaScript 간단 정리

- 갖다놓고, 꾸미고, 시킨다
- 오늘날의 HTML, CSS, 자바스크립트는 웹사이트, 즉 브라우저에서 동작하는 소프트웨어에만 국한되지 않음
  - React Native나 Native Script처럼 이것들, 혹은 비슷한 변형들로 모바일 앱을 만드는 기술들이 이미 널리 사용되고 있고
  - 심지어 Electron.js 같은 걸로 웹사이트가 아닌 컴퓨터 프로그램까지 이제는 이 세가지로 만들 수가 있음
- HTML과 CSS는 프로그래밍 언어에 못낌
- HTML
  - HTML(Hypertext Markup Language)은 이름과 같이 '마크업 언어'인데
  - 단순히 생각해서, 화면에 이것들이 이런 구조로 놓여 있어라하고 갖다놓는 수단이라고 할 수 있음
- CSS
  - CSS(Cascading Style Sheets)는 언어라는 말도 안들어감
- HTML과 CSS
  - HTML로 구조를 짜고, CSS로 그 구조 위를 예쁘게 꾸미는 것
  - 이렇게 보여라하고 꾸며주는 '문서'임
- 자바스크립트
  - 자바스크립트만이 프로그래밍 언어에 속함
  - 원래는 브라우저에서 웹사이트를 돌리는 목적으로 만들어졌었음
  - 계속해서 발전하고 특히, Node.js가 이걸 브라우저 바깥 세상으로 꺼내오면서 지금은 위상이 높아짐
  - 웹사이트에서 돌아가는 자바스크립트는 브라우저에서 다양한 일을 수행하고 HTML으로 올려놓은 요소들을 변형시키거나 직접 만들어내기까지 함

## 간단한 계산기 웹앱을 만들어보자

- HTML, CSS, 자바스트립트를 한 폴더 안에 만든다
- HTML(index.html)
  - html태그 안에 head와 body가 있음
  - head는 각종 설정을 넣는 곳
    - 여기에서 CSS와 자바스크립트를 연결함
  - body는 화면의 요소들을 넣는 곳

```html
<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <script defer type="text/javascript" src="script.js"></script>
    </head>
    <body>
        <div id="calculator">
            <span>얄팍한 계산기</span><br>
            <input id="formula-input"
                type="text"
                placeholder="수식을 입력하세요."/>
            <div id="calc-history"></div>
        </div>
        
    </body>
</html>
```

- CSS(style.css)

```css
#calculator {
    background-color: #ffbb24;
    border-radius: 12px;
    width: 240px;
    margin: 24px;
    padding: 24px;
    text-align: center;
}

#calculator span {
    font-size: 1.5em;
    font-weight: bold;
    color: white;
    text-shadow: 0px 0px 2px rgba(0, 0, 0, 0.33);
}

#calculator #formula-input {
    width: 100%;
    margin-top: 8px;
    height: 36px;
    line-height: 36px;
    font-size: 1.1em;
    letter-spacing: 3px;
    border: 0;
    text-align: center;
}

#calculator #formula-inout:focus {
    outline-width: 0;
}

#calculator #calc-history div {
    height: 36px;
    line-height: 36px;
    margin-top: 1px;
    background-color: rgba(255, 255, 255, 0.8);
}

#calculator #calc-history div.invalid {
    color: tomato;
    font-weight: bold;
}
```

- JavaScript(script.js)

```javascript
var formulaInput = document.getElementById("formula-input");
var calcHistDiv = document.getElementById("calc-history");

formulaInput.addEventListener("keyup", function(e) {
    if (e.code === "Enter")
        calculate();
})

function calculate() {

    // 입력칸의 문자열이 사칙연산 형식이 맞는지 확인
    var fm = formulaInput.value;
    var formulaRegex = /^\d+(.\d+)?[+\-*/]{1}\d+(.\d+)?$/;
    var formulaValid = formulaRegex.test(fm);

    var resultText = "노";
    if (formulaValid) {
        // 형식에 맞을 시 식을 계산하고 결과 문자열을 설정
        var answer;
        eval('answer=' + fm);
        resultText = fm + " = ";
        resultText 
            += (answer % 1 > 0 ? answer.toFixed(2) : answer.toString()); 
    }

    // clac-history 상자에 넣을 또 다른 상자를 생성하고 내용을 설정한 뒤 삽입
    var resultDiv = document.createElement("DIV");
    resultDiv.appendChild(document.createTextNode(resultText));
    if (!formulaValid)
        resultDiv.classList.add("invalid");
    calcHistDiv.insertBefore(resultDiv, calcHistDiv.firstChild);

    // 입력칸은 빈칸으로
    formulaInput.value = "";
}
```



## 결론

- HTML과 CSS는 배우기는 쉽지만 연습과 경험도 많이 필요함
- 같은 구조와 모습도, 구현하는 방법이 다양한데 어느쪽이 효율적이고 여러 환경이나 기기에 유연하게 적용 가능한지는 많이 만들어보고 겪어봐야 알 수 있음
- 공신력 있는 사이트들에 들어가서 크롬 개발자 도구 같은 툴들로 분석해보면 좋은 방법론들을 많이 얻을 수 있음
- 자바스크립트는 지금도 빠른 속도록 발전해나가는 언어라 끊임없이 공부할 게 생길 것
- 예전에는 대부분이 jQuery라는 강력한 라이브러리로 순수 자바스크립트보다 훨씬 코딩을 편하고 쉽게 하곤 했는데
- 요새는 자바스크립트도 파워풀해지고, jQuery의 성능문제도 있고 프론트엔드 프레임워크같은 새로운 개발방식들이 나오면서 jQuery의 입지가 줄고 있음
- 우선 자바스크립트를 탄탄히 배워놓은 다음, 이런 라이브러리나 프레임워크를 필요에 따라 배워나가면 좋음
- 웹사이트를 만들 때 HTML, CSS, 자바스크립트의 최신 기술들을 다 이용하려하면 곤란하다는 것
- 웹사이트는 결국 브라우저에서 동작하는 소프트웨어인데 이 브라우저들 중 일부에서 최신 기술들을 지원하지 않거나 혼자 이상하게 돌아가는 경우가 있기 때문에 호환성을 확인하고 테스트하면서 개발하는게 중요함

## 참고

- 유튜브 얄팍한 코딩사전
- https://www.youtube.com/watch?v=ffENjt7aEdc&list=PLpO7kx5DnyIFQ4XuYirD--DvRyUgaHD9w&index=3