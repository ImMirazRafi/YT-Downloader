# YouTube Video Downloader

A Python script to download YouTube videos or audio in MP4 or MP3 formats. Users can input multiple video links, specify file names, and choose the desired format. 

## Features
- Download videos in MP4 format.
- Download audio in MP3 format.
- Specify custom file names or use the original YouTube video title.
- Handles invalid characters in file names.

## How to Use
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. **Install dependencies**:
    ```sh
    pip install pytube
    ```

3. **Run the script**:
    ```sh
    python main.py
    ```

4. **Follow the prompts**:
    - Enter YouTube video URLs.
    - Specify file names (or use `0` to use the original title).
    - Choose the format (MP4 or MP3).

## Example Interaction

```plaintext
Enter the YouTube video URL (or enter '0' to start downloading): https://www.youtube.com/watch?v=example1
Enter the desired file name (without extension, or '0' to use the original title): abcde
Enter the YouTube video URL (or enter '0' to start downloading): https://www.youtube.com/watch?v=example2
Enter the desired file name (without extension, or '0' to use the original title): 0
Enter the YouTube video URL (or enter '0' to start downloading): 0
Enter 'mp4' to download videos or 'mp3' to download audio: mp3
Downloading 'Example Video 1' as 'abcde.mp3'...
'Example Video 1' downloaded successfully as 'abcde.mp3'!
Downloading 'Example Video 2' as 'Example Video 2.mp3'...
'Example Video 2' downloaded successfully as 'Example Video 2.mp3'!
```
