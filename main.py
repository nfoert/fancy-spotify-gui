import os

import eel

eel.init('web')

@eel.expose
def get_song_data():
    title = os.popen("playerctl --player=spotify metadata xesam:title").read().replace("\n", "")
    artist = os.popen("playerctl --player=spotify metadata xesam:artist").read().replace("\n", "")
    album = os.popen("playerctl --player=spotify metadata xesam:album").read().replace("\n", "")
    length = os.popen("playerctl --player=spotify metadata mpris:length").read().replace("\n", "")
    cover_art = os.popen("playerctl --player=spotify metadata mpris:artUrl").read().replace("\n", "")
    url = os.popen("playerctl --player=spotify metadata xesam:url").read().replace("\n", "")
    status = os.popen("playerctl --player=spotify status").read().replace("\n", "")

    json = {
        "title": title,
        "artist": artist,
        "album": album,
        "length": length,
        "cover_art": cover_art,
        "url": url,
        "status": status
    }

    return json


eel.start('main.html', mode=False)