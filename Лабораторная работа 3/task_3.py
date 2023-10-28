def count_letters(text):
    total_dict = {}
    text_low_register = text.lower()
    for symbol in text_low_register:
        if symbol.isalpha() and total_dict.get(symbol) == None:
            total_dict[symbol] = 1
        elif symbol.isalpha() and total_dict.get(symbol) != None:
            total_dict[symbol] += 1
    return total_dict


def calculate_frequency(dict_):
    dict_for_frequency = {}
    count = 0
    for item1 in dict_:
        count += dict_[item1]
    for item2 in dict_:
        dict_for_frequency[item2] = dict_[item2] / count
    return dict_for_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

our_dict = calculate_frequency(count_letters(main_str))

for item in our_dict:
    print(f'{item}: {our_dict[item]:.2f}')
