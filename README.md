<h1 align="center" style="font-size: 3rem;">
tiktok-api
</h1>
<p align="center">
<em>TikTok Web Api and Bot.</em></p>
<p>

   ![PyPI](https://img.shields.io/pypi/v/tiktok-api.svg) ![](https://img.shields.io/pypi/dm/tiktok-api.svg) 

</p></p>
<h2>Install with pip:</h2><p>

Gui:
Click download
unpack folder
create test.py with quickstart
run inside a terminal:
cd tiktok-api (cd to the folder dir)
python test.py


Terminal:
git clone https://github.com/instabotai/tiktok-api.git
cd tiktok-api
python test.py

<p>

## Quickstart
```python
from tiktokapi import bot

tiktok = bot.Bot()
tiktok.download_user_videos("maskofgod")

```
<p>
<h2>Endpoints</h2><p>
''' Get all username videos data '''<p>
api.get_user_videos(username)<p>
''' Get all username video url '''<p>
api.get_video_url(video)<p>
''' Get how many users have commented a video '''<p>
api.get_comment_count(video)<p>
''' Get how many users have liked a video '''<p>
api.get_likes_count(video)<p>
''' download user video '''<p>
api.download_user_video(video_url)<p>
''' Download users videos '''<p>
bot.download_user_videos(username)<p>
Use this function to get more user data, if you want to build new functions or fix some "scraping errors".<p>
api.get_home_page(username)
