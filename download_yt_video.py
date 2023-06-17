import argparse
from pytube import YouTube


def download_mp4(url, output_path):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_audio_only("mp4")
        video.download(output_path)
        print("下載完成！")
    except Exception as e:
        print("下載失敗：", str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="下載 YouTube 影片的 MP4 檔案")
    parser.add_argument("--video_url", "-v", type=str, help="要下載的 YouTube 影片連結")
    parser.add_argument("--output_directory", "-o", type=str, default="./", help="儲存的目錄路徑")
    args = parser.parse_args()

    download_mp4(args.video_url, args.output_directory)
