# 38_workshop

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
    <select v-model="count">
      <option v-for="number in numbers" :value="number">{{ number }}</option>
    </select>
    <button @click="getDogImage">Get {{ count }} Dogs!</button>
    <br>
    <div v-for="image in images">
      <img :src="image">
    </div>
  </div>
  
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

  <script>
    const app = new Vue({
      el: '#app',
      data: {
        images: [],
        numbers: 9,
        count: 1,
      },
      methods: {
        getDogImage: function() {
          const URL = `https://dog.ceo/api/breeds/image/random/${this.count}`
          axios.get(URL)
          .then(res => {
            this.images = res.data.message
          })
        }
      }
    })
  </script>
</body>
</html>
```



## 문제2

```
// 20191118103523
// https://dog.ceo/api/breeds/image/random/3

{
  "message": [
    "https://images.dog.ceo/breeds/newfoundland/n02111277_4292.jpg",
    "https://images.dog.ceo/breeds/terrier-patterdale/320px-05078045_Patterdale_Terrier.jpg",
    "https://images.dog.ceo/breeds/hound-afghan/n02088094_3653.jpg"
  ],
  "status": "success"
}
```

