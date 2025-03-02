# `Music Organizer`

A small script that groups subfolders into groups based on their initial letters. It was meant to organize my musics folder, but can be used for any type of content.

It groups based on the initial letter by creating directories with a fixed target subdirectories count, it counts the number of items in the input that starts with a certain letter, then it accumulates the count until it's bigger than the target.

Each group is after with the first letter and the last letter of the items that are inside it. 
For example: if the `./Music` folder contains the subfolders `Jethro Tull` and `Missing Persons` and they happen to be in the same group, a group dir named `J-M` is created.

## How to use it
It's a terminal-based app. It needs the input and output directories, and an optional flag to specify the target group size (default to 20 items).

Example: `python organizer.py ./Music-Disorganized ./Music --max_size 10`

## Dependencies
This app requires **Python 3**, probably any python3 version will work, not tested.

- **`argparse`**
- **`pathlib`**
