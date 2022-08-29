
from os import listdir, system


ttfs = listdir('ttf')

persian_alphabet = 'ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپو'
persian_numbers = '۱۲۳۴۵۶۷۸۹۰'
persian_signs = '!٬٫﷼٪×،*)(ـ-+؟«»؛'
persian_alphabet_after_no = 'ورزژدذا'
persian_alphabet_both_sides = set(persian_alphabet) - set(persian_alphabet_after_no)

glyphs_after_no = list(persian_alphabet_after_no) + ['\u200d' + c for c in persian_alphabet_after_no]
glyphs_both_sides = list(persian_alphabet_both_sides) + ['\u200d' + c for c in persian_alphabet_both_sides] + \
[c + '\u200d' for c in persian_alphabet_both_sides] + ['\u200d' + c + '\u200d' for c in persian_alphabet_both_sides]

glyphs = list(persian_numbers) + list(persian_signs) + glyphs_after_no + glyphs_both_sides

try:
    for font in ttfs:
        print()
        print('-----------------------------------' + font)
        for glyph in glyphs:
            print(glyph, end=' ')
            system(f'python3 ./ttf_character_to_png.py "{glyph}" {font}')
        open('lastfont', 'w').write(font)
except KeyboardInterrupt:
    exit(1)
