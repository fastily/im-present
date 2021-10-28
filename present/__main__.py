import logging

from contextlib import suppress
from time import sleep

with suppress(Exception): # only on macOS
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
    log.addHandler(RichHandler(rich_tracebacks=True))
    log.setLevel(logging.INFO)

    try:
        while True:
            log.info("Current position: %s", (curr := pyautogui.position()))

            max_x, max_y = pyautogui.size()
            pyautogui.moveTo(_next_valid_position(curr.x, max_x - 1), _next_valid_position(curr.y, max_y - 1))

            log.info("New Position: %s", pyautogui.position())
            sleep(0.5)

            pyautogui.moveTo(curr.x, curr.y)
            log.info("Moved back to: %s.  Now sleeping for 10 mins...", pyautogui.position())
            sleep(600)

    except KeyboardInterrupt:
        print("\n")


if __name__ == '__main__':
    _main()
