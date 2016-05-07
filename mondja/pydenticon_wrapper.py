from django.conf import settings
import pydenticon
import os.path

dir = settings.MEDIA_ROOT + '/identicon/'

foreground = ['rgb(63, 81, 181)', 'rgb(255, 152, 0)', 'rgb(156, 39, 176)', 'rgb(33, 150, 243)', 'rgb(244, 67, 54)', 'rgb(76, 175, 80)', 'rgb(156, 39, 176)']

background = 'rgb(237, 231, 246)'

padding = (20, 20, 20, 20)

generator = pydenticon.Generator(5, 5, foreground = foreground, background = background)

def create_identicon(username):
    filename = dir + username + '.png'
    if os.path.isfile(filename): return

    identicon = generator.generate(username, 200, 200, padding = padding, output_format = 'png')
    with open(filename, 'wb') as f:
        f.write(identicon)
