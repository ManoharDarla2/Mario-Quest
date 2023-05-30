from PIL import Image

original_image = Image.open('ground.png')

new_width = 800 * 10
new_height = 93
new_image = Image.new('RGBA', (new_width, new_height))

for i in range(10):
    new_image.paste(original_image, (i * original_image.width, 0))

new_image.save('ground_pattern.png')
