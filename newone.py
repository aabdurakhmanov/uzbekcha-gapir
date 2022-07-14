from pydub import AudioSegment
from pydub.playback import play

def char_to_path(agrument):
    match agrument:
        case "ch":
            return "ch"
        case "g'":
            return "g'"
        case "o'":
            return "o'"
        case "ng":
            return "ng"
        case "sh":
            return "sh"
        case default:
            return agrument


def main():
    path = input('enter value: ')
    i = 0
    while i <= len(path) - 1:
        if (i < len(path)):
            agrument = path[i] + path[i + 1]
            audio = char_to_path(agrument)
        else:
            agrument = path[i]
            audio = char_to_path(agrument)
         #  audio = switch(argument, default)
        music = 'audios\/{file}.wav'.format(file=audio)
        song = AudioSegment.from_wav(music)
        song = song.set_frame_rate(196000)
        play(song)

if __name__ == "__main__":
    main()

