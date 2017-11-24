'''MIT License
Copyright (c) 2017 nateshmbhat
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
SOFTWARE.'''

import platform
from setuptools import setup

install_requires = ['bs4' , 'urllib3' , 'json']
# if platform.system() == 'windows':
#     install_requires = [
#         'pypiwin32'
#     ]
# elif platform.system() == 'darwin':
#     install_requires = [
#         'pyobjc>=2.4'
#     ]


setup(
    name='yify',
    packages = ['yify'] ,
    version = '1.0',
    description = '''
    This Module is used to get the Top seeded torrents at any given time and get the entire movie details and ratings . 
    This module which uses the Yify APIs to search and download Yify torrents and helps to get all the details of movies which are listed in Yify's website
''' ,
    summary = 'Yify torrenter with movie searching and top seeded torrent finding features.'  ,
    author = 'Natesh M Bhat' ,
    url = 'https://github.com/nateshmbhat/pyttsx3',
    author_email = 'nateshmbhatofficial@gmail.com' ,
    download_url = 'https://github.com/nateshmbhat/pyttsx3/archive/v2.6.tar.gz',
    keywords=['yify' , 'pyyify' , 'Yify' , 'yify torrent' , 'yify download' , 'download yify' , 'yifyer'  , 'yifypy' , 'torrent download' , 'movie torrent' , 'movie downloader', 'movie finder'],
    classifiers = [] ,
    install_requires=install_requires
)