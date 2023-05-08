from lexicon.lexicon import LEXICON, valut_symbol

__supported_list: list = ["Usd", "Eur", "Cny", "Gbp",
                  "Jpy100", "Chf", "Try", "Aed"]

def get_done_msg(curency: dict, message: str) -> str:
    #find in list pisision valut
    short_name = _find_meaning(message)
    #get out curency from dict
    curency_valut: list = curency[short_name]
    name_valut = _delete_symbol(message)
    #form message
    msg = f"{LEXICON['start']} {name_valut}: {LEXICON['buy']} "\
        f"{curency_valut[0]}, {LEXICON['sell']} {curency_valut[1]}"
    return msg
        

def _find_meaning(message: str) -> str:
    #in list with valut find index
    index = valut_symbol.index(message)
    #index in valut == index in supported list
    name_valut = __supported_list[index]
    #return short name valut to find in db list
    return name_valut

def _delete_symbol(message: str) -> str:
    data = message.split()
    #return only name valut on russian
    return "".join(data[1])