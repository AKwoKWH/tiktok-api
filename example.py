from tiktokapi import api

api = api.Api()

videos = api.get_user_videos("maskofshiva")

x = 1
for video in videos:
    print(video)
    video_urls = api.get_video_url(video)
    print(video_urls)
    try:
        api.download_user_video(video_urls, str(x))
    except Exception as e:
        print(e)
    print(api.get_meta_title(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")
    x += 1
