
LNG_INDEX = '0'
LNG_LIST = ['ru', 'en']
LNG_MSG = {
    'open_web_page':
    [
        'Открыть домашнюю страницу',
        'Open home page'
    ],

    'hi':
    [
        'Привет',
        'Hello'
    ],
}


def set_lng(language):
    # global LNG_LIST
    index = LNG_LIST.index(language)
    if index >= 0:
        global LNG_INDEX
        LNG_INDEX = index


def lng(msg: str) -> str:
    # global LNG_INDEX
    # global LNG_MSG
    return LNG_MSG[msg][LNG_INDEX]
