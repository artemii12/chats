decode = 3

ALPHA = u'яю эь[ыъщшчцх]футсрЯЮ{ЭЬЫЪЩzyxw}vuts@rqpo#nmlk!' \
        u'`jih;gfedcb:aШЧ$Ц|ХФ=УТСР>ПО%НМЛ\КЙ+Иa/bcd<efghi' \
        u'j-klm^nop&qrst~uvwxyz_ЖЁЕД(ГВБ*Апонм)лкйиз?жёе,дгвба'

def encode_(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))


def decode_(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))
