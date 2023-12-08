# im-present
[![Python 3.11+](https://upload.wikimedia.org/wikipedia/commons/6/62/Blue_Python_3.11%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Simple utility which moves your mouse by 1 pixel and then back, at a specified interval.  Useful for pretending to be at your computer and fooling the apps which track your productivity.

## Installation
```bash
pip install im-present
```

## Usage
```
usage: __main__.py [-h] [-i secs] [-j secs] [-t secs]

periodically shakes the mouse pointer to prove you're here

optional arguments:
  -h, --help  show this help message and exit
  -i secs     number of seconds to wait in between mouse movements. Defaults to 600.
  -j secs     number of seconds to wait in between mouse jitters. Defaults to 0.5.
  -t secs     if set, exit after this many seconds have elapsed from the time this program was first started.
```