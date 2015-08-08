# coding: utf-8

from django.conf import settings
import pydenticon
import os.path

dir = settings.MEDIA_ROOT + '/identicon'

foreground = ['rgb(45, 79, 255)', 'rgb(254, 180, 44)', 'rgb(226, 121, 234)', 'rgb(30, 179, 253)', 'rgb(232, 77, 65)', 'rgb(49, 203, 115)', 'rgb(141, 69, 170)']

background = 'rgb(224, 224, 224)'

padding = (20, 20, 20, 20)

generator = pydenticon.Generator(5, 5, foreground = foreground, background = background)

def create_identicon(username):
    filename = dir + '/' + username + '.png'
    if os.path.isfile(filename): return

    identicon = generator.generate(username, 200, 200, padding = padding, output_format = 'png')
    with open(filename, 'wb') as f:
        f.write(identicon)
