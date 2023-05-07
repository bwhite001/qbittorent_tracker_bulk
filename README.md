qbittorent\_tracker\_bulk
=========================

qbittorent\_tracker\_bulk is a command line tool that enables you to add multiple trackers to a qBittorrent torrent in bulk.

Installation
------------

You can install qbittorent\_tracker\_bulk via [Poetry](https://python-poetry.org/docs/):

``sh
poetry install
``

Usage
-----

``sh
python -m qbittorent_tracker_bulk [-h] [-v] [-u URL] [-i FILE] [--version] TORRENT_FILE
``

### Arguments

*   `TORRENT_FILE` - Path to the torrent file
*   `-h, --help` - Show help message and exit
*   `-v, --verbose` - Increase output verbosity
*   `-u URL, --url URL` - Add a single tracker URL
*   `-i FILE, --input FILE` - Path to a file containing a list of tracker URLs
*   `--version` - Show program's version number and exit

### Examples

Add a single tracker:

``sh
python -m qbittorent_tracker_bulk -u https://example.com/tracker/announce http://example.com/path/to/torrent/file.torrent
``

Add multiple trackers from a file:

``sh
python -m qbittorent_tracker_bulk -i path/to/tracker_file.txt http://example.com/path/to/torrent/file.torrent
``

Contributing
------------

Contributions are welcome! Please submit a pull request or open an issue.

License
-------

This project is licensed under the terms of the MIT license.
