# :arrow_forward: YouTube Video Downloader :arrow_forward:

<p align="center">
<img title="Logo" alt="ç" src="./images/Logo PNG.png">
</p>

As I am tired of youtube video downloaders that are malicious and full of ads or paid I have created one with [Python](https://www.python.org/), Qt for Python ([PySide 6.7](https://doc.qt.io/qtforpython-6/)) and [PyTube-fix](https://github.com/JuanBindez/pytubefix).

## How to use?

**_It is highly recommended to install FFmpeg manually before running the program_**, the program can install FFmpeg automatically but during the testing of the program there were a few occasions when it did not install properly.

### 1. Installing FFmpeg

```bash
# Using Winget (recommended)
winget install "FFmpeg (Essentials Build)"

# Using Chocolatey
choco install ffmpeg
```

### 2. Downloading the program executable

1. Go to releases and download the `.zip`
2. Extract and run `.exe`

## Contributing

> Remember to contribute according to the [license](LICENSE).

### Setting up the workspace

```bash
# Clone the repo
git clone https://github.com/ExoticGamerrrYT/youtube-video-downloader.git

# Move to the repo dir
cd youtube-video-downloader

# Make virtual enviroment
## If virtualenv is installed
virtualenv .venv
## If not
py -m venv .venv

# Activating virtualenviroment (for Windows)
.venv/Scripts/activate.ps1

# Installing libraries
pip install -r requirements.txt
```

> virtualenv package web [here](https://virtualenv.pypa.io/en/latest/).

Built using [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe).

## License

This project is under [GNU General Public License v3.0](LICENSE).
