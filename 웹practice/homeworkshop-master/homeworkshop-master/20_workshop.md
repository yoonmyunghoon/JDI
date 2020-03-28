# 20_workshop

## 문제1 

- models.py

```python
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=20)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)
    votes = models.IntegerField()

```

