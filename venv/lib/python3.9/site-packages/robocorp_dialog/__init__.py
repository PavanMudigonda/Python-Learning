import platform
from pathlib import Path


def executable() -> str:
    curdir = Path(__file__).parent.resolve()

    if platform.system() == "Windows":
        return str(curdir / "Dialog" / "dialog.exe")
    elif platform.system() == "Darwin":
        return str(curdir / "Dialog.app" / "Contents" / "MacOS" / "dialog")
    else:
        return "robocorp-dialog"
