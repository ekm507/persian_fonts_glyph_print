
# convert font character to image

# کتابخانه‌ها
from os import makedirs
from PIL import Image, ImageDraw, ImageFont
from sys import argv

# تنظیمات
output_image_name = 'output.png'
font_path = './Vazir'
font_size = 350
image_size = (600, 600)
print_location = (100, 100)

text = argv[1]
font_name = argv[2]
font_path = 'ttf/'+font_name
makedirs(f'png/{text}', exist_ok=True)
output_image_name = f'png/{text}/{font_name}.png'

# چیزهای اولیه
my_image = Image.new('RGB', image_size, color = 'black')
# my_image = Image.open('input.png')
my_font = ImageFont.truetype(font_path, font_size)
my_color = (255, 255, 255)

# چاپ نوشته روی عکس
image_editable = ImageDraw.Draw(my_image)

image_editable.text(print_location, text, my_color, font=my_font, direction='ltr', align='right')

# ذخیره کردن عکس
my_image.save(output_image_name)