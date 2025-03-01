question=input('What Is The Answer to the Great Question of Life, the Universe and Everything? ')
casein=question.strip().casefold()
match casein:
    case "42" | "forty two" | "forty-two":
        print('Yes')
    case _:
        print('no')