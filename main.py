import sys
import colorer
import reader

if len(sys.argv) == 2:
    fileName = sys.argv[1]
    lang = fileName.split(".")[len(fileName.split("."))-1]

    print(colorer.colorize(reader.read(fileName), lang))
else:
    print("no args or to many args")