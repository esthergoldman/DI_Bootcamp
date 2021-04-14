# # cakeTop=''.ljust(candles,"i").center(11,'_')
# ask_birthday = input("when it's your birthday?, for example: DD/MM/YYYY\n ")
# day = int(ask_birthday[:1])  # i need convert to interger
# # year = ask_birthday[:-4]  # to get year
# # candles = day

# age = day - 2020

# # if ask_user.find("a") == -1:
# #     print("congratulations")
# # else:
# #     print("oops try again")


#jonathan´s solution

from dateTime import dateTime, timedeltabirthday = input('what is your birthday ex. DD/MM/YYYY')birthday_convert_to_date = datetime.strptime(birthday, "%d/%m/%Y")current_date = datetime.now()age = int((current_date - birthday_convert_to_date) / 365 / timedelta (days=1))age_to_string = str(age)last_digit_of_age = int(age_to_string[-1])candles = 'i' * int(last_digit_of_age)cake = (f'''\t ___{candles}___        | :H:a:p:p:y:  |     __|______________|__    |^^^^^^^^^^^^^^^^^^^^|    | :B:i:r:t:h:d:a:y:  |    |                    |    ~~~~~~~~~~~~~~~~~~~~~~    ''')#check if leap year, print two cakes if yesif birthday_convert_to_date.year % 4 == 0 :if birthday_convert_to_date.year % 100 == 0 :if birthday_convert_to_date.year % 400 == 0 :print(cake * 2)else :print(cake)else :print(cake * 2)else :print(cake)