# 15_workshop

## 01_문제

- views.py

```python
from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'pages/one.html')

def two(request):
    return render(request, 'pages/two.html')
```

- urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one),
    path('two/', views.two),
]


```

- base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Base is everywhere!</h1>
    {% block body %}
    {% endblock %}
</body>
</html>
```

- one.html

```html
{% extends 'pages/base.html' %}

{% block body %}
    <h2>I am ONE!</h2>
{% endblock %}
```

- two.html

```html
{% extends 'pages/base.html' %}

{% block body %}
    <h2>I am TWO!</h2>
{% endblock %}
```

