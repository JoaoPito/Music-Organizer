# `Music Organizer`

A small script that groups subfolders into groups based on their initial letters. It was meant to organize my musics folder, but can be used for any type of content.

## How to use it
It's a terminal-based app. It needs the input and output directories, and an optional flag to specify the target group size (default to 20 items).

Example: `python organizer.py ./Music-Disorganized ./Music --max_size 10`

## Dependencies
This app requires **Python 3**, probably any python3 version will work, not tested.

- **`argparse`**
- **`pathlib`**