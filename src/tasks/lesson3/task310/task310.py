

def day_amount_input_by_user():
    print("Данная программа разабьет вашу сумму денег на купюры и монеты.")
    input_user = input('Введите сумму денег через запятую: ')
    return input_user

def division_into_notes_and_coins(n1:str) ->str:
    input_user_cart = n1.split(",")
    return input_user_cart

def bank_notes(n2:str) ->dict:
    sum_bill = int(n2)

    bank_notes_naminal = (500,100,50,20,10,5,2,1)
    bill_dic = {}
    bank_notes_kol = 0

    while bank_notes_kol <= 7:
        bill = sum_bill / bank_notes_naminal[bank_notes_kol]
        bill_dic[bank_notes_naminal[bank_notes_kol]] = int(bill)
        sum_bill = sum_bill - (bank_notes_naminal[bank_notes_kol] * int(bill))
        bank_notes_kol = bank_notes_kol + 1

    return bill_dic

def coins(n3:str) ->dict:
    sum_coins = int(n3)
    bill = sum_coins / 50
    bill_coins_dic = {50:int(bill)}
    sum_coins = sum_coins - (50 * bill_coins_dic[50])

    bill = sum_coins / 20
    bill_coins_dic.update({20: int(bill)})
    sum_coins = sum_coins - (20 * bill_coins_dic[20])

    bill = sum_coins / 10
    bill_coins_dic.update({10: int(bill)})
    sum_coins = sum_coins - (10 * bill_coins_dic[10])

    bill = sum_coins / 5
    bill_coins_dic.update({5: int(bill)})
    sum_coins = sum_coins - (5 * bill_coins_dic[5])

    bill = sum_coins / 1
    bill_coins_dic.update({1: int(bill)})
    sum_coins = sum_coins - (1 * bill_coins_dic[1])


    return bill_coins_dic



def solution(sentence: str) -> dict:
    #input_user = day_amount_input_by_user()
    input_user_split = division_into_notes_and_coins(sentence)
    input_user_split_bank_note = input_user_split[0]
    input_user_split_coins = input_user_split[1]
    input_user_bank_notes = bank_notes(input_user_split_bank_note)
    input_user_coins = coins(input_user_split_coins)

    return input_user_bank_notes

if __name__ == "__main__":
    main()