# 35_workshop

## 문제1

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
  <div id="app">
    <div>
      <button @click="addCounter">+1</button>
      <p><b>Counter: {{ count }}</b></p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        count: 0,
      },
      methods: {
        addCounter: function() {
          this.count += 1
        },
      },
    })
  </script>
</body>
</html>
```

