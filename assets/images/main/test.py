from PIL import Image

original_image = Image.open('clouds.png')

new_width = 1600 * 9
new_height = original_image.height
new_image = Image.new('RGBA', (new_width, new_height))

for i in range(9):
    new_image.paste(original_image, (i * original_image.width, 0))

new_image.save('clouds_pattern.png')
