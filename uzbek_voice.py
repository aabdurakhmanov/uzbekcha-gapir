from pydub import AudioSegment
from pydub.playback import play


path = input('enter value: ')
for char in path:
    music = 'audios\/{file}.wav'.format(file=char)
    song = AudioSegment.from_wav(music)
    song = song.set_frame_rate(196000)
    print(char)
    play(song)


