
"""import sqlite3

conn = sqlite3.connect('system_data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)')

def data_entry():
    password = 15091986
    name = "artrwenhg"
    c.execute("INSERT INTO data (name, password) VALUES(?, ?)",
              (name, password))

    conn.commit()


print(                c.execute(fSELECT password from data
                                    where name like ("artrwenhg")).fetchall()[0][0])

c.close()
conn.close()"""
ALPHA = u'яю эь[ыъщшчцх]футсрЯЮ{ЭЬЫЪЩzyxw}vuts@rqpo#nmlk!`jih;gfedcb:aШЧ$Ц|ХФ=УТСР>ПО%НМЛ\КЙ+Иa/bcd<efghij-klm^nop&qrst~uvwxyz_ЖЁЕД(ГВБ*Апонм)лкйиз?жёе,дгвба'

def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))

def decode(text, step):
    return text.translate(
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))
dec = 'привет что you делаешь Как тебя, зовут?(WHY you)'
dec = decode(dec, 3)
print(dec)
dec = encode(dec, 3)
print(dec)