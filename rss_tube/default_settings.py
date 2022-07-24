import os

from pathlib import Path

from .__version__ import __title__


DEFAULT_SETTINGS = {
    "theme": "light",
    "logging/level": "Disabled",
    "tasks/interval": 240,
    "proxies/enabled": False,
    "proxies/socks/host": "127.0.0.1",
    "proxies/socks/port": 9050,
    "MainWindow/icon/width": 32,
    "MainWindow/icon/height": 32,
    "MainWindow/menu/show": True,
    "MainWindow/start_minimized": False,
    "Channels/export_path": os.path.join(Path.home(), f"{__title__.replace(' ', '-').lower()}-channels.json"),
    "Filters/export_path": os.path.join(Path.home(), f"{__title__.replace(' ', '-').lower()}-filters.bytes"),
    "Settings/export_path": os.path.join(Path.home(), f"{__title__.replace(' ', '-').lower()}-settings.bytes"),
    "MainWindow/entries_to_fetch": 1000,
    "MainWindow/category_icon/show": True,
    "MainWindow/feed_icon/show": True,
    "tray/show": True,
    "tray/minimize": True,
    "feeds/update_interval/minutes": 10,
    "feeds/refresh_entries": True,
    "youtube/show_description": True,
    "player": "mpv",
    "player/mpv/path": "mpv",
    "player/mpv/args": "",
    "player/mpv/quality": "1080p",
    "player/vlc/path": "vlc",
    "player/vlc/args": "",
    "cache/preload_thumbnails": False,
    "delete/added_more_than": False,
    "delete/added_more_than_days": 14,
    "delete/interval/hours": 2,
    "delete/keep_unviewed": True,
    "shortcuts/filter": "Ctrl+F",
    "shortcuts/quit": "Ctrl+Q",
    "shortcuts/refresh": "F5",
    "shortcuts/new_feed": "Ctrl+N",
    "shortcuts/new_category": "Ctrl+Shift+N",
    "shortcuts/play": "Ctrl+O",
    "shortcuts/play_audio": "Ctrl+Alt+O",
    "shortcuts/play_in_browser": "Ctrl+Shift+O",
    "shortcuts/previous_entry": "Ctrl+,",
    "shortcuts/next_entry": "Ctrl+.",
    "shortcuts/toggle_star": "Ctrl+S"
}
