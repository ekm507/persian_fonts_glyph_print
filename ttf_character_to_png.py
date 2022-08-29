
# convert font character to image

# کتابخانه‌ها
from os import makedirs
from PIL import Image, ImageDraw, ImageFont
from sys import argv
from unicodedata import name

# تنظیمات
output_image_name = 'output.png'
font_path = './Vazir'
font_size = 350
image_size = (600, 600)
print_location = (100, 100)

text = argv[1]
font_name = argv[2]
font_path = 'ttf/'+font_name

persian_alphabet = 'ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپو'
persian_numbers = '۱۲۳۴۵۶۷۸۹۰'
only_char = text.strip('\u200d')
variation = ''

if only_char in persian_alphabet:
    char_name = name(only_char).split(' ')[-1]
    if text[0] == '\u200d':
        if text[-1] == '\u200d':
            variation = 'MIDDLE'
        else:
            variation = 'FINAL'
    elif text[-1] == '\u200d':
        variation = 'INITIAL'
    else:
        variation = 'INDEPENDANT'
else:
    if only_char in persian_numbers:
        char_name = name(only_char).split(' ')[-1]
    else:
        char_name = name(only_char)

full_char_name = char_name + ' ' + variation
full_char_name = full_char_name.rstrip(' ')

print(full_char_name)

output_image_name = f'png/{full_char_name}/{font_name}.png'
makedirs(f'png/{full_char_name}', exist_ok=True)

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