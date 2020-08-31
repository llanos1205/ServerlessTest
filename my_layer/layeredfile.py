import envcon


def layered_test(content):
    return "this is host=:" + envcon.region + content
