import datetime

DAYS = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
MONTHS = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')


def main(): 
    while True:
        print('Enter a year for the calendar to generate')
        response = input('> ')

        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break 
        else:
            print('Please enter a numeric year')
    
    while True:
        print('Enter the month for the calendar to generate')
        response = input('> ')

        if response.lower() in MONTHS:
            month = response.lower()
            break

    calendar_text = get_calendar_for(year, month)
    print(calendar_text)
    calendar_file_name = f"calendar_{year}_{month}.txt"
    with open(calendar_file_name, 'w') as f_handler:
        f_handler.write(calendar_text)
    print('Saved to ' + calendar_file_name + '\n')


def get_calendar_for(year, month):
    calendar_text = ''
    calendar_text += (' ' * 34) + month.capitalize() + ' ' + str(year) + '\n'
    calendar_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    week_separator = ('+----------' * 7) + '+\n'
    blank_row = ('|          ' * 7) + '|\n'
    current_date = datetime.date(year, MONTHS.index(month) + 1, 1)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        calendar_text += week_separator

        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += '|\n'

        calendar_text += day_number_row
        for i in range(3):
            calendar_text += blank_row
        if current_date.month != MONTHS.index(month) + 1:
            break
    
    calendar_text += week_separator
    return calendar_text


if __name__ == '__main__':
    main() 
