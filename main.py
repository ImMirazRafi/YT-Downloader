from pytube import YouTube
import os
import re

def sanitize_filename(name):
    # Replace invalid characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def download_youtube_videos():
    video_urls = []
    file_names = []
    
    # Collect video URLs and file names from user
    while True:
        url = input("Enter the YouTube video URL (or enter '0' to start downloading): ")
        if url == '0':
            break
        file_name = input("Enter the desired file name (without extension, or '0' to use the original title): ")
        video_urls.append(url)
        file_names.append(file_name)
    
    # Ask user for the desired format
    format_choice = input("Enter 'mp4' to download videos or 'mp3' to download audio: ").lower()
    
    # Download each video one by one
    for url, file_name in zip(video_urls, file_names):
        try:
            # Create a YouTube object with the URL
            yt = YouTube(url)
            
            # Determine the final file name
            final_file_name = file_name if file_name != '0' else yt.title
            final_file_name = sanitize_filename(final_file_name)
            
            # Display video title and downloading message
            print(f"Downloading '{yt.title}' as '{final_file_name}.{format_choice}'...")
            
            if format_choice == 'mp4':
                # Get the highest resolution stream available
                stream = yt.streams.get_highest_resolution()
                
                # Download the video with the specified file name and .mp4 extension
                stream.download(filename=f"{final_file_name}.mp4")
                print(f"'{yt.title}' downloaded successfully as '{final_file_name}.mp4'!")
            
            elif format_choice == 'mp3':
                # Get the audio stream
                stream = yt.streams.filter(only_audio=True).first()
                
                # Download the audio with the specified file name
                out_file = stream.download(filename=final_file_name)
                
                # Save the file with .mp3 extension
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(f"'{yt.title}' downloaded successfully as '{final_file_name}.mp3'!")
            
            else:
                print("Invalid format choice. Please enter 'mp4' or 'mp3'.")
                return
        
        except Exception as e:
            print(f"An error occurred while downloading {url}: {e}")

# Run the downloader
if __name__ == "__main__":
    download_youtube_videos()