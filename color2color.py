import colors

def matchcolor(color: str):
    match color:
        case "blue":
            return colors.BLUE
        case "yellow":
            return colors.YELLOW
        case "cyan":
            return colors.CYAN
        case "magenta":
            return colors.MAGENTA
        case "light red":
            return colors.LIGHTRED_EX
        case "light magenta":
            return colors.LIGHTMAGENTA_EX
        case "green":
            return colors.GREEN
    return colors.WHITE