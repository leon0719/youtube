import argparse
from pytube import YouTube


def on_progress(stream, chunk, file_handle, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    print(f"下載進度：{progress:.2f}%")


def download_mp4(video_url, output_directory, audio_only=False):
    try:
        youtube = YouTube(video_url)
        if audio_only:
            video = youtube.streams.get_audio_only()
        else:
            video = youtube.streams.get_highest_resolution()
        video.download(output_directory, on_progress=on_progress)
        print("下載完成！")
    except Exception as e:
        print("下載失敗：", str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="下載 YouTube 影片的 MP4 檔案")
    parser.add_argument("--video_url", "-v", type=str, help="要下載的 YouTube 影片連結")
    parser.add_argument("--output_directory", "-o", type=str, default="./", help="儲存的目錄路徑")
    parser.add_argument("--audio_only", "-a", action="store_true", default=False, help="是否只下載音檔")
    args = parser.parse_args()

    download_mp4(args.video_url, args.output_directory, args.audio_only)
