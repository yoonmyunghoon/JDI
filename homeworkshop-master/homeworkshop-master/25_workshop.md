# 25_workshop

## 문제1

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, related_name='articles')

class Hashtag(models.Model):
    content = models.TextField()
    
```

