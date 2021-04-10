import json

with open("music.json") as bands:
    json_music = bands.read()

music_dict = json.loads(json_music)

print(music_dict)
