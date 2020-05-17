# 21_homework

## 문제1

```html
{% for comment in question.comment_set.all %}
	<h3>{{ comment.content }}</h3>
{% endfor %}
```



## 문제2

```html
"{% url 'questions:comments_create' question.pk %}"
```

