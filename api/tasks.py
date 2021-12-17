from celery import shared_task
from googleapiclient.discovery import build
from api.models import YoutubeAPIResult
from datetime import datetime

#Celery task for saving youtube query results to the DB
@shared_task
def save_youtube_results(current_key, random_query):

    # Using youtube data API v3, Fetching Data
    youtubeAPI = build("youtube", "v3", developerKey=current_key)
    req = youtubeAPI.search().list(
        q=random_query,
        part="snippet",
        type="video",
        order="date",
        maxResults=50,
        publishedAfter=datetime.utcfromtimestamp((datetime.now().timestamp())).strftime(
            "%Y-%m-%dT%H:%M:%S.0Z"
        ),
    )
    res = req.execute()
    print(res)

    # Create DB Object
    if len(res["items"]) != 0:
        for i in res["items"]:
            YoutubeAPIResult.objects.create(
                video_title=i["snippet"]["title"],
                description=i["snippet"]["description"],
                publish_datetime=datetime.strptime(
                    (i["snippet"]["publishedAt"]), "%Y-%m-%dT%H:%M:%SZ"
                ),
                thumbnail_url=i["snippet"]["thumbnails"]["default"]["url"],
            )
