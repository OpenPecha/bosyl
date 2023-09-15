from bosyl.tools import get_bo_symbols


def test_get_bo_symbols():
    test_str = 'རྨོ་རྨོ་ལགས་ཧམ་པ་ཚ་པོ་རེད། སྲོག་ལ་རྐྱོན་མེད།'
    expected_syls = [
        'རྨོ','་','རྨོ', '་','ལ','ག','ས', '་','ཧ','མ', '་','པ','་', 'ཚ','་', 'པོ','་','རེ','ད','། ',
        'སྲོ','ག', '་','ལ', '་','རྐྱོ','ན', '་','མེ','ད', '།'
    ]

    bo_symbols = get_bo_symbols(test_str)

    assert bo_symbols == expected_syls

