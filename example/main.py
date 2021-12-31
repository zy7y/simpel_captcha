from simpel_captcha import img_captcha
from simpel_captcha import captcha

print(f'验证码: {captcha}')

image, text = img_captcha()

image.save('demo.png')
print(f'图片对象: {image}')
print(f'验证码: {text}')
