from simpel_captcha import b64_captcha, captcha, img_captcha

print(f"验证码: {captcha}")

image, text = img_captcha()

image.save("demo.png")
print(f"图片对象: {image}")
print(f"验证码: {text}")

# base64字符
image, text = b64_captcha()
print(f"base64图片: {image}")
print(f"验证码: {text}")
