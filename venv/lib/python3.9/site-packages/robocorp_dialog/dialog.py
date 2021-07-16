import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, List

import webview  # type: ignore
from robocorp_dialog.bridge import Bridge  # type: ignore

LOGGER = logging.getLogger(__name__)


def static() -> str:
    # NB: pywebview uses sys.argv[0] as base
    base = Path(sys.argv[0]).resolve().parent
    path = Path(__file__).resolve().parent / "static"
    return os.path.relpath(str(path), str(base))


def output(obj: Any) -> None:
    print(json.dumps(obj), flush=True)


def run(
    elements: List,
    title: str,
    width: int,
    height: int,
    auto_height: bool,
    on_top: bool,
    debug: bool,
) -> None:
    """Spawn the dialog and wait for user input. Print the result into
    stdout as JSON.

    :param elements: Elements as list
    :param title: Title text for window
    :param width: Window width in pixels
    :param height: Window height in pixels
    :param auto_height: Automatic height resize
    :param on_top: Always on top
    :param debug: Allow developer tools
    """
    try:
        url = os.path.join(static(), "index.html")

        LOGGER.info("Serving from '%s'", url)
        LOGGER.info("Displaying %d elements", len(elements))

        bridge = Bridge(elements=elements, auto_height=auto_height, on_top=on_top)
        window = webview.create_window(
            url=url,
            js_api=bridge,
            resizable=True,
            text_select=True,
            background_color="#0b1025",
            title=title,
            width=width,
            height=height,
            on_top=True,
        )
        bridge.window = window

        LOGGER.info("Starting dialog")
        webview.start(debug=debug)

        if bridge.error is not None:
            output({"error": bridge.error})
        if bridge.result is not None:
            output({"value": bridge.result})
        else:
            output({"error": "Aborted by user"})
    except Exception as err:  # pylint: disable=broad-except
        output({"error": str(err)})
    finally:
        LOGGER.info("Dialog stopped")
