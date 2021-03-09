
def division_into_notes_and_coins(n1: str) -> str:
    serach1 = n1.find(",")
    serach2 = n1.find(".")
    if serach1 >= 0:
        input_user_cart = n1.split(",")
    if serach2 >= 0:
        input_user_cart = n1.split(".")
    n1_note = n1[0].isdigit()
    n1_coins = n1[1].isdigit()
    input_user_bank_notes = {}
    input_user_cons = {}

    if not n1_note == True:
        if not n1_coins == True:
            raise ValueError("function does not support sentences with > 2 words")
            return input_user_bank_notes, input_user_coins
    return input_user_cart


def bank_notes(n2: str) -> dict:
    sum_bill = int(n2)

    bank_notes_naminal = (500, 100, 50, 20, 10, 5, 2, 1)
    bill_dic = {}
    bank_notes_kol = 0

    while bank_notes_kol <= 7:
        bill = sum_bill / bank_notes_naminal[bank_notes_kol]
        if int(bill) > 1:
            bill_dic[bank_notes_naminal[bank_notes_kol]] = int(bill)
            sum_bill = sum_bill - (bank_notes_naminal[bank_notes_kol] * int(bill))
        bank_notes_kol = bank_notes_kol + 1

    return bill_dic


def coins(n3: str) -> dict:
    sum_coins = int(n3)

    coins_naminal = (50, 20, 10, 5, 2, 1)
    bill_coins_dic = {}
    coins_kol = 0

    while coins_kol <= 5:
        bill = sum_coins / coins_naminal[coins_kol]
        if int(bill) > 1:
            bill_coins_dic[coins_naminal[coins_kol]] = int(bill)
            sum_coins = sum_coins - (coins_naminal[coins_kol] * int(bill))
        coins_kol = coins_kol + 1

    return bill_coins_dic


def solution(sentence: str) -> dict:
    input_user_split = division_into_notes_and_coins(sentence)
    input_user_split_bank_note = input_user_split[0]
    input_user_split_coins = input_user_split[1]
    input_user_bank_notes = bank_notes(input_user_split_bank_note)
    input_user_coins = coins(input_user_split_coins)

    return input_user_bank_notes, input_user_coins

