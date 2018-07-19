import sys
from subprocess import check_output
from GUI import GUI, GUIRunner

VERSION = "v0.1-dev"

def printHelpOutput():
    output = \
    "options: \n"\
    "    [--help] [-h] ...... help ie. this\n" \
    "    [--version] [-v] ... version information\n"\
    "    [--gui] [-g] ....... graphical user interface\n"
    print(output)

def printVersionOutput():
    print("\nUtilities " + VERSION)
    
    print("    Branch: " + str(check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode('utf-8')[:-1]))
    
    postHash = ''
    if str(check_output(["git", "diff", "--stat"]).decode('utf-8')) != '':
        postHash = '-dirty'
    print("    Hash: " + str(check_output(["git", "rev-parse", "--short", "HEAD"]).decode('utf-8')[:-1] + postHash))
    
    print("    Commit Message: " + str(check_output(["git", "log", "-1", "--pretty=%B"]).decode('utf-8')[:-2])) # Commit messages are apperently have an extra newline?
    print("")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Handle GUI
        if sys.argv[1] in ["-g", "--gui"]:
            GUIRunner(GUI("Utilities"))
        elif sys.argv[1] in ["-h","--help"]:
            print("")
            printHelpOutput()
        elif sys.argv[1] in ["-v","--version"]:
           printVersionOutput()
        else:
            print("")
            print("Unkown option: " + sys.argv[1])
            printHelpOutput()
    else:
        # Handle CLI
        pass