生成验证码 图片 ～（BytesIO，image file， base64）， 文字
# install
```shell
pip install simpel_captcha
```
# use
## 文字验证码
```python
from simpel_captcha import captcha
code = captcha()
```
## 图片验证码（本地保存）
```python
from simpel_captcha import img_captcha
img, code = img_captcha()
```
## 图片验证码（BytesIO）- 可使用`Web框架`直接通过流的形式返回
``` python
from simpel_captcha import img_captcha
img, code = img_captcha(byte_stream=True)
```
### fastapi example
```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from simpel_captcha import img_captcha

app = FastAPI()


@app.get("/captcha", summary='图片验证码')
def image_captcha():
    image, text = img_captcha(byte_stream=True)
    # todo 将验证码缓存到Redis中 
    return StreamingResponse(content=image, media_type='image/jpeg')
```
![postman result](https://gitee.com/zy7y/simpel_captcha/raw/master/example/image/postman.png)
## base64字符串（推荐使用）
```python
from simpel_captcha import b64_captcha
obj, code = b64_captcha()
```
### fastapi example
```python
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from simpel_captcha import b64_captcha

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/captcha", summary='图片验证码')
def image_captcha():
    image, text = b64_captcha()
    # todo 将验证码缓存到Redis中 
    return {"captcha_img": image, "captcha_code": text}
```
```vue
<!-- vue3 -->
<template>
   <img :src="captcha" />
</template>
<script setup>
import { ref } from "vue";
import axios from "axios"
const captcha = ref("")
axios({
  method: 'get',
  url: 'http://127.0.0.1:8000/captcha'
}).then(res => captcha.value = res.data.captcha_img)

</script>
```

# API
## captcha
> 生成文字验证码，接受一个num参数，关系到生成的验证码位数

```python
from simpel_captcha import captcha

print(f'验证码: {captcha(6)}')
```
output:
```shell
验证码: TjXP
```
## img_captcha
> 生成图片验证码, 返回数据为元组 `(Image| BytesIO, captcha)`

```python
from simpel_captcha import img_captcha

image, text = img_captcha()

print(f'图片对象: {image}')
print(f'验证码: {text}')
```
output:
```shell
图片对象: <PIL.Image.Image image mode=RGB size=100x30 at 0x1C7A0CAA7C0>
验证码: TjXP
```
## 生成图片base64
```python
from simpel_captcha import b64_captcha

image, text = b64_captcha()
print(f'base64图片: {image}')
print(f'验证码: {text}')
```
output:
```shell
# 直接将base64字符串 复制到浏览器
base64图片: data:image/jpeg;base64,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
验证码: Q2of
```

# LICENSE
```text
MIT License

Copyright (c) 2022 柒意

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```