import xmltodict

with open("music.xml") as xmlMusic:
    music = xmlMusic.read()

xml_dict = xmltodict.parse(music)
