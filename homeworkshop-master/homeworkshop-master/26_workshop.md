# 26_workshop

## 문제1

- views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from IPython import embed

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
        
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)
```

- signup.html

```html
{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block body %}
    <h1>SIGNUP</h1>
    <form action="" method="POST">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% buttons submit="회원가입" reset="Cancel" %}{% endbuttons %}
    </form>
{% endblock %}
```

