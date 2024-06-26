from pytube import Playlist

def download_playlist(playlist_url, download_path='.'):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Print the playlist title
        print(f'Downloading playlist: {playlist.title}')

        # Iterate over all videos in the playlist
        for video in playlist.videos:
            try:
                # Print the title of the video being downloaded
                print(f'Downloading video: {video.title}')

                # Download the video to the specified path
                video.streams.get_highest_resolution().download(download_path)
            except Exception as e:
                print(f'Error downloading {video.title}: {e}')

        print('Playlist download complete!')
    except Exception as e:
        print(f'Error accessing playlist: {e}')

if __name__ == '__main__':

    playlist_url = 'Your-Playlist-Url'
    download_path = './downloads'

    download_playlist(playlist_url, download_path)
