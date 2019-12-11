# 21_workshop

## 문제1

```html
<h1>회식메뉴 추천</h1>
{% for choice in question.choice_set.all %}
	<li>{{ choice.content }} : {{ choice.votes }}표</li>
{% endfor %}
```

