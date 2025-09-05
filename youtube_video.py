from pytube import YouTube

url = input("Enter the YouTube video URL: ")
try:
    yt = YouTube(url)
    print(f"Title: {yt.title}")
    print("Downloading...")
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!")
except Exception as e:
    print(f"Error: {e}")