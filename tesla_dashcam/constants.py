"""Constants used throughout the Tesla Dashcam package."""

import sys
from platform import processor as platform_processor

MONITOR_SLEEP_TIME = 5

FFMPEG = {
    "darwin": "ffmpeg",
    "win32": "ffmpeg.exe",
    "cygwin": "ffmpeg",
    "linux": "ffmpeg",
    "freebsd11": "ffmpeg",
}

MOVIE_HOMEDIR = {
    "darwin": "Movies/Tesla_Dashcam",
    "win32": "Videos\Tesla_Dashcam",
    "cygwin": "Videos/Tesla_Dashcam",
    "linux": "Videos/Tesla_Dashcam",
    "freebsd11": "Videos/Tesla_Dashcam",
}

DEFAULT_CLIP_HEIGHT = 960
DEFAULT_CLIP_WIDTH = 1280

MOVIE_QUALITY = {
    "HIGH": "18",
    "MEDIUM": "20",
    "LOW": "23",
    "LOWER": "28",
    "LOWEST": "33",
}

MOVIE_ENCODING = {
    "x264": "libx264",
    "x264_nvidia": "h264_nvenc",
    "x264_mac": "h264_videotoolbox",
    "x264_intel": "h264_qsv",
    "x264_qsv": "h264_qsv",
    "x264_vaapi": "h264_vaapi",
    "x264_rpi": "h264_omx",
    "x265": "libx265",
    "x265_nvidia": "hevc_nvenc",
    "x265_mac": "hevc_videotoolbox",
    "x265_intel": "hevc_qsv",
    "x265_rpi": "h265",
}

DEFAULT_FONT = {
    "darwin": "/Library/Fonts/Arial Unicode.ttf",
    "win32": "/Windows/Fonts/arial.ttf",
    "cygwin": "/cygdrive/c/Windows/Fonts/arial.ttf",
    "linux": "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    "freebsd11": "/usr/share/local/fonts/freefont-ttf/FreeSans.ttf",
}

HALIGN = {"LEFT": "10", "CENTER": "(w/2-text_w/2)", "RIGHT": "(w-text_w)"}

VALIGN = {"TOP": "10", "MIDDLE": "(h/2-(text_h/2))", "BOTTOM": "(h-(text_h)-10)"}

EVENT_REASON = {
    "sentry_aware_object_detection": "SENTRY",
    "sentry_aware_accel*": "SENTRY",
    "user_interaction_dashcam_icon_tapped": "SAVED",
    "user_interaction_honk": "HONK",
    "sentry_aware*": "SENTRY",
    "user_interaction*": "USER",
}

PLATFORM = sys.platform
PROCESSOR = platform_processor()

if PLATFORM == "darwin" and PROCESSOR == "i386":
    try:
        from subprocess import run
        sysctl = run(
            ["sysctl", "-n", "machdep.cpu.brand_string"],
            capture_output=True,
            timeout=120,
            text=True,
        )
    except TimeoutError:
        print("Timeout running sysctl")
    else:
        if sysctl.returncode == 0:
            from re import search, IGNORECASE as re_IGNORECASE
            if search("Apple", sysctl.stdout, re_IGNORECASE) is not None:
                PROCESSOR = "arm"
        else:
            print("Error running sysctl: {sysctl.returncode} - {sysctl.stderr}") 