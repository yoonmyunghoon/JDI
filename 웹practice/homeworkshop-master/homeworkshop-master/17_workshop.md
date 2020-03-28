# 17_workshop

## 문제1

```python
from django import forms
from .models import Student

#1. Form Class
class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'my-name',
                'placeholder': 'Enter the name!',
            }
        )
    )
    age = forms.IntegerField(
        label='나이',
        widget=forms.Textarea(
            attrs={
                'class': 'my-age',
                'placeholder': 'Enter the age!',
            }
        )
    )
    
#2. Model Form
class StudentForm(forms.ModelForm):
	class Meta:
		model = student
		fields = ('name', 'age', )
```

## 문제2

```html
<form action="/students/create/" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="submit">
</form>
```

