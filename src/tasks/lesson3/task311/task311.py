

def division_into_email(n1:str) ->str:
    input = n1.split("@")
    return input

def email_look(n2:str) ->int:
    email_info = 1
    if n2 == 'gmail.com':
        email_info = 2
    return email_info




def solution(sentence: str) -> int:
    input_user = division_into_email(sentence)
    email = input_user[1]
    email_info = email_look(email)
    return email_info

if __name__ == "__main__":
    main()