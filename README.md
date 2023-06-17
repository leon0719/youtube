# YouTube MP4 下載程式

這是一個使用 Pytube 庫的 Python 程式，用於下載 YouTube 影片的 MP4 檔案。

## 安裝

請確保已經安裝了 Pytube 庫，可以使用以下指令進行安裝：

```shell
pip install pytube
```

## 使用方法

使用下列步驟來下載 YouTube 影片的 MP4 檔案：

1. 打開終端機或命令提示字元。
2. 執行以下指令：

```shell
python download_yt_video.py -v [影片連結] -o [目錄路徑] --audio_only
```

3. 替換 `[影片連結]` 為你要下載的 YouTube 影片連結。
4. 替換 `[目錄路徑]` 為你想要儲存檔案的目錄路徑。

程式將會嘗試下載提供的影片並將其儲存到指定的目錄中。

## 範例

以下是使用範例：

```shell
python download.py -v "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o "./downloads/" --audio_only
```

這將會下載 `https://www.youtube.com/watch?v=dQw4w9WgXcQ` 這個 YouTube 影片並儲存到 `./downloads/` 目錄中。

