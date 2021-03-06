"""
task 4 of computer security lessons
"""

text_carrier = """
Октябрь уж наступил — уж роща отряхает
Последние листы с нагих своих ветвей;
Дохнул осенний хлад — дорога промерзает.
Журча еще бежит за мельницу ручей,
Но пруд уже застыл; сосед мой поспешает
В отъезжие поля с охотою своей,
И страждут озими от бешеной забавы,
И будит лай собак уснувшие дубравы.

II
Теперь моя пора: я не люблю весны;
Скучна мне оттепель; вонь, грязь — весной я болен;
Кровь бродит; чувства, ум тоскою стеснены.
Суровою зимой я более доволен,
Люблю ее снега; в присутствии луны
Как легкий бег саней с подругой быстр и волен,
Когда под соболем, согрета и свежа,
Она вам руку жмет, пылая и дрожа!

III
Как весело, обув железом острым ноги,
Скользить по зеркалу стоячих, ровных рек!
А зимних праздников блестящие тревоги?..
Но надо знать и честь; полгода снег да снег,
Ведь это наконец и жителю берлоги,
Медведю, надоест. Нельзя же целый век
Кататься нам в санях с Армидами младыми
Иль киснуть у печей за стеклами двойными.

IV
Ох, лето красное! любил бы я тебя,
Когда б не зной, да пыль, да комары, да мухи.
Ты, все душевные способности губя,
Нас мучишь; как поля, мы страждем от засухи;
Лишь как бы напоить, да освежить себя —
Иной в нас мысли нет, и жаль зимы старухи,
И, проводив ее блинами и вином,
Поминки ей творим мороженым и льдом.

V
Дни поздней осени бранят обыкновенно,
Но мне она мила, читатель дорогой,
Красою тихою, блистающей смиренно.
Так нелюбимое дитя в семье родной
К себе меня влечет. Сказать вам откровенно,
Из годовых времен я рад лишь ей одной,
В ней много доброго; любовник не тщеславный,
Я нечто в ней нашел мечтою своенравной.

VI
Как это объяснить? Мне нравится она,
Как, вероятно, вам чахоточная дева
Порою нравится. На смерть осуждена,
Бедняжка клонится без ропота, без гнева.
Улыбка на устах увянувших видна;
Могильной пропасти она не слышит зева;
Играет на лице еще багровый цвет.
Она жива еще сегодня, завтра нет.

VII
Унылая пора! очей очарованье!
Приятна мне твоя прощальная краса —
Люблю я пышное природы увяданье,
В багрец и в золото одетые леса,
В их сенях ветра шум и свежее дыханье,
И мглой волнистою покрыты небеса,
И редкий солнца луч, и первые морозы,
И отдаленные седой зимы угрозы.

VIII
И с каждой осенью я расцветаю вновь;
Здоровью моему полезен русской холод;
К привычкам бытия вновь чувствую любовь:
Чредой слетает сон, чредой находит голод;
Легко и радостно играет в сердце кровь,
Желания кипят — я снова счастлив, молод,
Я снова жизни полн — таков мой организм
(Извольте мне простить ненужный прозаизм).

IX
Ведут ко мне коня; в раздолии открытом,
Махая гривою, он всадника несет,
И звонко под его блистающим копытом
Звенит промерзлый дол и трескается лед.
Но гаснет краткий день, и в камельке забытом
Огонь опять горит — то яркий свет лиет,
То тлеет медленно — а я пред ним читаю
Иль думы долгие в душе моей питаю.

X
И забываю мир — и в сладкой тишине
Я сладко усыплен моим воображеньем,
И пробуждается поэзия во мне:
Душа стесняется лирическим волненьем,
Трепещет и звучит, и ищет, как во сне,
Излиться наконец свободным проявленьем —
И тут ко мне идет незримый рой гостей,
Знакомцы давние, плоды мечты моей.

XI
И мысли в голове волнуются в отваге,
И рифмы легкие навстречу им бегут,
И пальцы просятся к перу, перо к бумаге,
Минута — и стихи свободно потекут.
Так дремлет недвижим корабль в недвижной влаге,
Но чу! — матросы вдруг кидаются, ползут
Вверх, вниз — и паруса надулись, ветра полны;
Громада двинулась и рассекает волны.

XII
Плывет. Куда ж нам плыть?
. . . . . . . . . . . . 
"""

message_text = "today,12am,at12housing"
message_text = "влдоарпдлвоарпдлворапл"


def prepare_text(text_string:str):
    lines = text_string.splitlines()
    clean_lines = [line.strip() for line in lines]
    return clean_lines


def iterate_bits(message: bytes):
    """
    Transform

    ``iterate_bits(message_text.encode("utf-8"))``

    :param message: string of bytes
    :return: boolean on each iteration
    """
    for byte in message:
        for bit in "{:08b}".format(byte):
            yield bit == "1"


def encrypt(lines:list, data:bytes):
    """
    encrypt lines and return text
    :return: string of encrypted text
    """

    # TODO make ckeck of text length
    lines_index = 0
    if len(lines) < len(data)*8:    # raise Error, if text are too short
        raise RuntimeError("Error: Text too short to encrypt message")

    for bit in iterate_bits(data):
        if bit:
            lines[lines_index] += " "
        lines_index += 1
    return "\n".join(lines)


def boole_list_to_bytes(bit_message:list):
    """
    message in bits transform to bytes
    :return: byte string
    """
    b_number = 0
    byte_list = []
    one_cool_byte = 0
    for item in bit_message:
        one_cool_byte <<= 1
        if item:
            one_cool_byte += 1
        b_number += 1
        if b_number == 8:
            byte_list.append(one_cool_byte)
            b_number = 0
            one_cool_byte = 0
    return bytes(byte_list).rstrip(b"\x00")     # return byte string

def decrypt(lines:list) -> str:
    bit_message = []
    for line in lines:
        if line and line[-1] == " ":
            bit_message.append(True)
        else:
            bit_message.append(False)

    byte_string = boole_list_to_bytes(bit_message)
    ok_string = byte_string.decode("utf-8")
    # TODO - translate bites (or bytes) - to message
    return ok_string


if __name__ == '__main__':
    message_text = "сообщение"


    with open("text_carrier.txt", "r") as text_file:
        text_carrier = text_file.read()

        # result = [i for i in iterate_bits(message_text.encode("utf-8"))]

        lines = prepare_text(text_carrier)
        encrypted_text = encrypt(lines, message_text.encode("utf-8")) # return string
        with open("encrypted_text.txt", "w") as encrypted_file:
            encrypted_file.write(encrypted_text)

    with open("encrypted_text.txt", "r") as encrypted_file:
        encrypted_text = encrypted_file.read()
        data = decrypt(encrypted_text.splitlines(keepends=False))
        with open("new_text_carrier.txt", "w") as new_file:
            new_file.write(data)

