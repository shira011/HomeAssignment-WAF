from datetime import datetime


def addToDate(date_g, num):
    """
    :param date_g: given date
    :param num:  number of days to add
    :return: the date after adding the number of days
    """
    date_split = date_g.split('.')
    date_splitI = list(map(int, date_split))
    days = date_splitI[0] + num
    if days > 30:
        date_splitI[0] = days - 30
        if date_splitI[1] + 1 == 13:
            date_splitI[1] = 1
            date_splitI[2] += 1
        else:
            date_splitI[1] += 1
    else:
        date_splitI[0] = days
    finalDateFormat = str(datetime(date_splitI[2], date_splitI[1], date_splitI[0])).split(' ')
    finalDate = finalDateFormat[0].split('-')
    finalDate.reverse()
    return '.'.join(finalDate)


print(addToDate('29.06.2020', 8))
