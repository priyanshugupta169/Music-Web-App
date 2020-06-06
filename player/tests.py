from django.test import TestCase

# Create your tests here.
import mutagen
from mutagen.mp3 import MP3,EasyMP3
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3

# print(mutagen.File("E:/songs/eminem-love the way you.mp3").keys())

# audio=MP3("E:/songs/Mere_Rashke_Qamar.mp3")
# print(audio.info.name)
audio=EasyMP3("E:/songs/lahore.mp3")
print(audio.tags)
print(audio.tags['title'][0])
print(audio.tags['album'][0])
print(audio.tags['artist'][0])
# print(audio.tags['track_number'][0])
print(audio.info.length)
# print(audio.tags._EasyID3__id3._DictProxy__dict['APIC'].data)
