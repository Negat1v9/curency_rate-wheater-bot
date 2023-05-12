from lexicon.lexicon_curency import LEXICON, valut_symbol

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

def get_all_curency(curency: dict, message: str) -> str:
    start_msg: str = message + "\n"
    msg: str = f"{start_msg}"
    for i in range(len(valut_symbol)):
        fool_string = []
        #russian name of valut
        name_valut: str = '<b>'+valut_symbol[i].split()[1]+'</b>'
        fool_string.append(name_valut)
        #short name valut
        short_name = __supported_list[i]
        #taken curency of valut
        valut_curency = curency[short_name][0]
        fool_string.append(valut_curency)
        fool_string.append('руб')
        #creating fool string
        msg += " ".join(fool_string) + "\n"
    return msg.rstrip()
        

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