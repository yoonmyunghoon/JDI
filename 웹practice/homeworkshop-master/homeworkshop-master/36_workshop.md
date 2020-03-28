# 36_workshop

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
    <button v-on:click="changecolor">Toggle</button>
    <h3 v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">빨강과 파랑을 섞으면 보라색이 됩니다.</h3>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
  const app = new Vue({
    el: '#app',
    data: {
      activeColor: 'red',
      fontSize: 30,
    },
    methods: {
      changecolor: function() {
        if ( this.activeColor === 'red'){
          this.activeColor = 'blue'
        }
        else {
          this.activeColor = 'red'
        }
      }
    }
  })
  </script>
</body>
</html>
```

```html
<강사님코드>
    
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
      .red {
          color: red;
      }
      .blue {
          color: blue;
      }
  </style>
    
</head>
<body>
  <div id="app">
    <button @click="toggleColor">Toggle</button>
    <div :class="red ? 'red' : 'blue'">
        빨강과 파랑을 섞으면 보라색이 됩니다.
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
  const app = new Vue({
    el: '#app',
    data: {
      red: true
    },
    methods: {
      toggleColor() {
          this.red = !this.red
      }
    }
  })
  </script>
</body>
</html>
```

