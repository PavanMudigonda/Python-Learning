import argparse
import json
import logging
import traceback
import sys
from robocorp_dialog import dialog

LOGGER = logging.getLogger(__name__)


def error(message: str) -> None:
    print(json.dumps({"error": f"Unhandled error: {message}"}), flush=True)


def main() -> None:
    try:
        parser = argparse.ArgumentParser()

        parser.add_argument("elements")
        parser.add_argument("--title", default="Dialog")
        parser.add_argument("--width", default=480, type=int)
        parser.add_argument("--height", default=640, type=int)
        parser.add_argument("--auto_height", action="store_true")
        parser.add_argument("--on_top", action="store_true")
        parser.add_argument("--debug", action="store_true")

        args = parser.parse_args()

        logging.getLogger("pywebview").setLevel(logging.WARNING)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        )

        elements = json.loads(args.elements)
        if not isinstance(elements, list):
            raise ValueError("Elements should be a list")

        dialog.run(
            elements=elements,
            title=args.title,
            width=args.width,
            height=args.height,
            auto_height=args.auto_height,
            on_top=args.on_top,
            debug=args.debug,
        )
    except Exception:  # pylint: disable=broad-except
        error(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
