from datetime import datetime
def get_user_choice():
    print('1-Processing date data\n2-Character data\n3-Quit')
    while True:
        user_choice = input('your choice: ')
        if user_choice.isdigit() and 1<=int(user_choice)<=3:
            return int(user_choice)
        else:
            user_choice = input('error. please enter again')
def date_data():
    date_fomat = '%d/%m/%Y'
    while True:
        date_string = input('enter date in fomat dd/mm/yyyy: ')
        try:
            datetime.strptime(date_string, date_fomat)
            return True
        except:
            print('error')
            return False
def character_data():
    while True:
        a = input('enter first character: ')
        b = input('enter second character: ')
        if len(a) == 1 and len(b) == 1:
            print(f'ASCII codes of {a} and {b} are {ord(a)} and {ord(b)}')
            break
        else:
            print('error')
def main():
    choice = get_user_choice()
    if choice == 1:
        if date_data() == True:
            print('valid')
        else:
            print('not valid')
    if choice == 2:
        character_data()
    if choice == 3:
        print('quit')
if __name__ == "__main__":
    main()