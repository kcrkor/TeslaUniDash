[![Total Downloads](https://img.shields.io/github/downloads/ehendrix23/tesla_dashcam/total)](https://img.shields.io/github/downloads/ehendrix23/tesla_dashcam/total)
[![Latest Downloads](https://img.shields.io/github/downloads/ehendrix23/tesla_dashcam/latest/total)](https://GitHub.com/ehendrix23/tesla_dashcam/releases/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/tesla-dashcam)](https://pypi.python.org/pypi/tesla-dashcam/)

# tesla_dashcam

Python program that provides an easy method to merge saved Tesla Dashcam footage into a single video.

When saving Tesla Dashcam footage a folder is created on the USB drive for each event and within it multiple MP4 video files are created. Currently the dashcam leverages four (4) cameras (front, rear, left repeater, and right repeater) and will create a file for each of them. Every minute is stored into a separate file as well. This means that when saving dashcam footage there is a total of 40 files video files for every 10 minutes, each event of 10 minutes is put into a separate folder.

Using this program, one can combine the 40 video files of an event into one (1), and combine video of multiple events together. The layout of the four (4) different cameras within the resulting video can be determined by choosing one of the available layouts.

This program has multiple options providing a high level of flexibility on the videos to process, cameras to include, layout of the resulting videos, location, format, encoding, etc. See usage section below to read upon all the possibilities.

**Video Input** provides options related to the source videos.

*Trigger Monitor* is to have processing of videos not start upon execution of the program but instead be based on a trigger (i.e. inserting the USB/SD card in the PC).

**Video Layout** provides parameters to define what the resulting video should look like. There are 4 different layouts to choose from. This can then be further adjusted by having the left/right cameras be in perspective or not. Swap left/right or front/rear cameras, change the scale for all cameras and/or for certain cameras, make left/right/rear seem as if you were watching it through a mirror, or as if you turn your head around and looking backwards.

**Camera Exclusion** exclude certain cameras from the resulting video.

**Timestamp** options allow you to define what the timestamp in the resulting video should look like, or just to not have it display at all.

**Timestamp Restriction** provides with the possibility to only create a video of the portion that are important. Instead of uploading a video where the first 5 minutes is nothing, specify the start and end timestamps to shorten the video to the important section instead.

**Event offsets** allows you to skip a portion from the start (and/or the end) for each event.

**Video Output** then further defines what the output should look like. Fast-forward through the Sentry video where nothing is happening, speed up or slow down the video, etc.

**Advanced encoding settings** allows you to further define additional encoding settings.

And **Update Check** will make sure you always have the latest version available.

Check out the Usage section of this README to get more information on all available parameters and what each does.

## Binaries

Stand-alone binaries can be retrieved from:

- Windows: [tesla_dashcam.zip](https://github.com/ehendrix23/tesla_dashcam/releases/latest/download/tesla_dashcam.zip)
- MacOS (OSX): [tesla_dashcam.dmg](https://github.com/ehendrix23/tesla_dashcam/releases/latest/download/tesla_dashcam.dmg)

[ffmpeg](https://www.ffmpeg.org/legal.html) is included within the respective package.
ffmpeg is a separately licensed product under the [GNU Lesser General Public License (LGPL) version 2.1 or later](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
FFmpeg incorporates several optional parts and optimizations that are covered by the GNU General Public License (GPL) version 2 or later. If those parts get used the GPL applies to all of FFmpeg.
For more information on ffmpeg license please see: https://www.ffmpeg.org/legal.html

Windows binary of ffmpeg was downloaded from: https://ffmpeg.zeranoe.com/builds/
MacOS binary of ffmpeg was downloaded from: https://www.osxexperts.net

## Notes

The video files for the same minute between the 4 cameras are not always the same length. If there is a difference in their duration then the background color (black by default) will be shown for the camera which video ended before the others (within the minute).
It is thus possible within a video to see the background color for one of the cameras, and then when that minute has passed for it to show video again.

The date and time shown within the video comes from the timestamp embedded in the saved videos themselves, not from the filename. Date and time shown within resulting videos is converted to timezone set upon the PC it is being run on.

## Requirements

This package relies on [ffmpeg](https://ffmpeg.org) to be installed, this is a free, open source cross-platform solution to convert video. The created executables for Windows and MacOS include an ffmpeg version.

If not using the executables (Windows and MacOS) then [Python](https://www.python.org) 3.8.6 or higher is required.

## Installation

Downloading the respective bundle (ZIP for Windows, DMG for MacOS) and unpacking this in a location of your choosing is sufficient to install this.

If downloading the source files (i.e. for Linux) then Python has to be installed as well. I recommend in that case to install the package from pypi using pip to ensure all package requirements (except for ffmpeg) are met.

This package is available from [pypi](https://pypi.org/project/tesla-dashcam/).

Install from pypi is done through:

```bash
python3 -m pip install tesla_dashcam
```

## Development Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management. To set up the development environment:

1. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate a virtual environment:
```bash
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package in development mode:
```bash
uv pip install -e .
```

For development dependencies:
```bash
uv pip install -e ".[dev]"
```

For build dependencies:
```bash
uv pip install -e ".[build]"
```

The project uses lock files to ensure reproducible builds:
- `uv.lock`: Main dependencies
- `uv-dev.lock`: Development dependencies
- `uv-build.lock`: Build dependencies

## Usage

```bash
usage: tesla_dashcam.py [-h] [--version] [--loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--temp_dir TEMP_DIR] [--no-notification] [--display_ts] [--skip_existing]
                        [--delete_source] [--exclude_subdirs] [--monitor] [--monitor_once] [--monitor_trigger MONITOR_TRIGGER]
                        [--layout {WIDESCREEN,FULLSCREEN,PERSPECTIVE,CROSS,DIAMOND}] [--perspective] [--scale CLIP_SCALE [CLIP_SCALE ...]] [--mirror] [--rear] [--swap] [--no-swap]
                        [--swap_frontrear] [--background BACKGROUND] [--title_screen_map] [--no-front] [--no-left] [--no-right] [--no-rear] [--no-timestamp]
                        [--halign {LEFT,CENTER,RIGHT}] [--valign {TOP,MIDDLE,BOTTOM}] [--font FONT] [--fontsize FONTSIZE] [--fontcolor FONTCOLOR]
                        [--text_overlay_fmt TEXT_OVERLAY_FMT] [--timestamp_format TIMESTAMP_FORMAT] [--start_timestamp START_TIMESTAMP] [--end_timestamp END_TIMESTAMP]
                        [--start_offset START_OFFSET] [--end_offset END_OFFSET] [--sentry_offset] [--sentry_start_offset START_OFFSET] [--sentry_end_offset END_OFFSET] [--output OUTPUT] [--motion_only] [--slowdown SLOW_DOWN] [--speedup SPEED_UP]
                        [--chapter_offset CHAPTER_OFFSET] [--merge [MERGE_GROUP_TEMPLATE]] [--merge_timestamp_format MERGE_TIMESTAMP_FORMAT] [--keep-intermediate] [--keep-events]
                        [--set_moviefile_timestamp {START,STOP,SENTRY,RENDER}] [--no-gpu] [--gpu] [--gpu_type {nvidia,intel,qsv,rpi,vaapi}] [--no-faststart]
                        [--quality {LOWEST,LOWER,LOW,MEDIUM,HIGH}] [--compression {ultrafast,superfast,veryfast,faster,fast,medium,slow,slower,veryslow}] [--fps FPS]
                        [--ffmpeg FFMPEG] [--encoding {x264,x265}] [--enc ENC] [--check_for_update] [--no-check_for_update] [--include_test]
                        [source [source ...]]
```

### Video Layout Options

The following layouts are available:

#### FULLSCREEN (Default)
Resolution: 1920x960
```
+---------------+----------------+----------------+
|               | Front Camera   |                |
+---------------+----------------+----------------+
| Left Camera   |  Rear Camera   |  Right Camera  |
+---------------+----------------+----------------+
```
[Video example](https://youtu.be/P5k9PXPGKWQ)

#### WIDESCREEN
Resolution: 1920x1920
```
+---------------+----------------+----------------+
|                 Front Camera                    |
+---------------+----------------+----------------+
| Left Camera   |  Rear Camera   |  Right Camera  |
+---------------+----------------+----------------+
```
[Video example](https://youtu.be/nPleIhVxyhQ)

#### CROSS
Resolution: 1280x1440
```
+---------------+----------------+----------------+
|               | Front Camera   |                |
+---------------+----------------+----------------+
|     Left Camera      |       Right Camera       |
+---------------+----------------+----------------+
|               | Rear Camera    |                |
+---------------+----------------+----------------+
```

#### DIAMOND
Resolution: 1920x976
```
+---------------+----------------+----------------+
|               |  Front Camera  |                |
+---------------+                +----------------+
|   Left Camera |----------------| Right Camera   |
+               +  Rear Camera   +                +
|---------------|                |----------------|
+---------------+----------------+----------------+
```

### Common Options

- `--perspective`: Show side cameras in perspective mode
- `--scale`: Adjust scale for all cameras or specific ones (e.g. `--scale 0.5` or `--scale camera=front 1`)
- `--mirror`/`--rear`: Control how side/rear cameras are displayed
- `--swap`/`--no-swap`: Control left/right camera swapping
- `--background COLOR`: Set background color (default: black)
- `--no-front`, `--no-left`, `--no-right`, `--no-rear`: Exclude specific cameras

### Text Overlay Options

- `--text_overlay_fmt`: Format string for overlay text
- `--timestamp_format`: Format for timestamps (default: %x %X)
- `--no-timestamp`: Disable timestamp display
- `--halign`: Horizontal alignment (LEFT/CENTER/RIGHT)
- `--valign`: Vertical alignment (TOP/MIDDLE/BOTTOM)
- `--font`: Custom font file
- `--fontsize`: Custom font size
- `--fontcolor`: Font color (default: white)

### Advanced Options

- `--quality`: Video quality (LOWEST to HIGH)
- `--compression`: Compression speed (ultrafast to veryslow)
- `--fps`: Output framerate (default: 24)
- `--gpu`: Enable GPU acceleration
- `--encoding`: Choose encoding (x264/x265)

For complete documentation of all options, use `tesla_dashcam --help`.
