# 10_workshop

## 01_문제

```html
<style>
    #ssafy > p:nth-child(2) {
        color: red;
    }
</style>
<div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
</div>

>>>>첫번째 단락

<style>
    #ssafy > p:nth-of-type(2) {
        color:blue;
    }
</style>
<div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
</div>	

>>>>두번째 단락

```









