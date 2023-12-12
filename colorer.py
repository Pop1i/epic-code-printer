import json
import reader
import color2color

def colorize(input: str, lang: str):
    data = input
    try:
        syntax = json.loads(reader.read(f"syntax-highlighting/{lang}.json"))
    except:
        return data

    for thing in syntax:
        word = thing["word"]
        color = thing["color"]
        mode = thing["mode"]

        color = color2color.matchcolor(color)

        match mode:
            case 0:
                word += " "
            case 1:
                pass
            case 2:
                data = data.replace(word, color + word)
                continue

        data = data.replace(word, color + word + color2color.colors.WHITE)
    
    return data + color2color.colors.RESET