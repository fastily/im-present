import argparse
import logging

from contextlib import suppress
from time import time, sleep

with suppress(Exception):  # only for macOS
    from AppKit import NSBundle
    NSBundle.mainBundle().infoDictionary()["LSBackgroundOnly"] = "1"  # hide dock icon

import pyautogui

from rich.logging import RichHandler


pyautogui.FAILSAFE = False

log = logging.getLogger(__name__)


def _next_valid_position(v: int, end_index: int) -> int:
    """Determines the next valid position that the specified coordinate value can be moved to.  Works simillarly to clamp in numpy.

    Args:
        v (int): The current index value
        end_index (int): The maximum index value (just the max size of the axis on the screen - 1)

    Returns:
        int: The next valid position for teh specified coordinate value.
    """
    if v <= 0:
        return 1
    elif v >= end_index:
        return end_index - 1

    return v - 1


def _main() -> None:
    """Main driver, to be run if this script is invoked directly."""
    cli_parser = argparse.ArgumentParser(description="periodically shakes the mouse pointer to prove you're here")
    cli_parser.add_argument('-i', type=int, default=600, metavar="secs", help="number of seconds to wait in between mouse movements.  Defaults to 600.")
    cli_parser.add_argument('-j', type=float, default=0.5, metavar="secs", help="number of seconds to wait in between mouse jitters.  Defaults to 0.5.")
    cli_parser.add_argument('-t', type=int, metavar="secs", help="if set, exit after this many seconds have elapsed from the time this program was first started.")
    args = cli_parser.parse_args()

    log.addHandler(RichHandler(rich_tracebacks=True))
    log.setLevel(logging.INFO)

    if args.t and args.t < args.i:
        log.error("time to exit (-t) cannot be less than time to wait between mouse movements (-i)")
        return

    start_ts = time()
    curr = pyautogui.position()

    try:
        while True:
            log.info("Current position: %s", (new_curr := pyautogui.position()))
            if new_curr != curr:
                curr = new_curr
                log.info("Human mouse movement detected, sleeping for %ds...", args.i / 2)
                sleep(args.i / 2)
                continue

            max_x, max_y = pyautogui.size()
            pyautogui.moveTo(_next_valid_position(curr.x, max_x - 1), _next_valid_position(curr.y, max_y - 1))

            log.info("New Position: %s", pyautogui.position())
            sleep(args.j)

            pyautogui.moveTo(curr.x, curr.y)
            log.info("Moved back to: %s.  Now sleeping for %ds...", pyautogui.position(), args.i)
            sleep(args.i)

            if args.t and time() - start_ts > args.t:
                break
    except KeyboardInterrupt:
        print("\n")


if __name__ == '__main__':
    _main()
