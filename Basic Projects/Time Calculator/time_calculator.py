def add_time(init_time, add, day=None):
    ret = ""
    to_add = add_hm(change_format(init_time), int(add.split(':')[0]), int(add.split(':')[1]))
    ret += print_format([to_add[1], to_add[2]])
    if day is not None:
        ret = ret + ', ' + get_day(day.capitalize(), to_add[0])
    if to_add[0] == 1:
        ret = ret + " (next day)"
    elif to_add[0] > 0:
        ret = ret + ' ' + f"({to_add[0]} days later)"
    return ret


def get_day(day, add):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    to_add = days.index(day) + add
    while to_add > 6:
        to_add -= 7
    return days[to_add]


def change_format(init_time):
    current_time = init_time.split()
    if init_time == '12:00 AM':
        return [00, 00]
    elif init_time.endswith('PM') and not init_time.startswith('12'):
        return [int(current_time[0].split(':')[0]) + 12, int(current_time[0].split(':')[1])]
    else:
        return [int(current_time[0].split(':')[0]), int(current_time[0].split(':')[1])]


def print_format(print_time):
    ret = []
    if print_time[0] == 00:
        ret = ['12', ':', str(print_time[1]),  ' AM']
    elif print_time[0] > 12:
        ret = [str(print_time[0] - 12), ':', str(print_time[1]), " PM"]
    elif print_time[0] == 12:
        ret = ["12", ":", str(print_time[1]), " PM"]
    else:
        ret = [str(print_time[0]), ":", str(print_time[1]), " AM"]
    if len(ret[2]) == 1:
        ret[2] = '0' + ret[2]
    return ret[0] + ret[1] + ret[2] + ret[3]


def add_hm(time_now, hours, minutes):
    time_now[1] += minutes
    if time_now[1] >= 60:
        time_now[0] += 1
        time_now[1] -= 60
    time_now[0] += hours
    add_day = 0
    while time_now[0] >= 24:
        time_now[0] -= 24
        add_day += 1
    return [add_day, time_now[0], time_now[1]]


