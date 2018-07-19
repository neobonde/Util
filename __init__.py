import sys
from GUI import GUI, GUIRunner


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Handle GUI
        if sys.argv[1] in ["-g", "--gui"]:
            GUIRunner(GUI("Utilities"))
        # Handle CLI