from pytube import YouTube
from pytube.exceptions import RegexMatchError

video_url = 'https://www.youtube.com/shorts/rfYiMeLMqxs'
save_location = './'

try:
    yt = YouTube(video_url)
    # Setting the quality of the saved video
    stream = yt.streams.filter(res='720p', progressive=True).first()
    if stream:
        stream.download(output_path=save_location)
        print("Video successfully downloaded.")
    else:
        print("Failed to find a suitable stream for the specified resolution.")
except RegexMatchError:
    print("Incorrect video link format or regex match error.")
except Exception as e:
    print("An error occurred:", str(e))
