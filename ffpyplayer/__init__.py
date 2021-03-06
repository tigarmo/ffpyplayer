'''
FFPyPlayer library
==================
'''
import sys
import os
from os.path import join, isdir
import platform

__version__ = '4.0.dev0'
version = __version__

# Dec 2015, the ffmpeg src git version tested and upto date with, including this commit
_ffmpeg_git = 'c413d9e6356e843aa492be9bb0ddf66ae6c97501'
# skipped all show modes and subtitle display related functionality commits

# TODO:
# * Implement CONFIG_SDL to be able to compile without needing SDL at all.
# * Currently, it only supports text subtitles - bitmap subtitles are ignored.
#   Unless one uses a filter to overlay the subtitle.
# * We can not yet visualize audio to video. Provide a filter chain link between
#   audio to video filters to acomplish this.

_ffmpeg = join(sys.prefix, 'share', 'ffpyplayer', 'ffmpeg', 'bin')
if isdir(_ffmpeg):
    os.environ["PATH"] += os.pathsep + _ffmpeg

_sdl = join(sys.prefix, 'share', 'ffpyplayer', 'sdl', 'bin')
if isdir(_sdl):
    os.environ["PATH"] += os.pathsep + _sdl

if 'SDL_AUDIODRIVER' not in os.environ and platform.system() == 'Windows':
    os.environ['SDL_AUDIODRIVER'] = 'DirectSound'
