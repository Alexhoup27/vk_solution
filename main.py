import datetime
import datetime as dt
import sys
#т.к. не было условий того, где будут лежать входные данные, будем считать, что они лежат в одной директории
start_time = dt.datetime.strptime(sys.argv[1], '%Y-%m-%d')
result = dict()
start_dir = '' #если хотите изменить директорию запуска измените эту строку
_dir = r'output/'
#считывание данных
for num_days in range(1, 8):
    now_time = start_time - datetime.timedelta(days=num_days)
    data = [i.split(',') for i in\
            open(start_dir + rf'{now_time.strftime("%Y-%m-%d")}.csv').read().split('\n')]
    for now_data in data:
        email = now_data[0]
        action = now_data[1]
        if email not in result.keys():
            result[email] = [email, 0, 0, 0, 0]
        if action == 'CREATE':
            result[email][1] += 1
        elif action == 'READ':
            result[email][2] += 1
        elif action == 'UPDATE':
            result[email][3] += 1
        else:
            result[email][4] += 1
#запись файла
with open(rf'{_dir}{start_time.strftime("%Y-%m-%d")}.csv', mode='w') as writer:
    to_writer = ['email,create_count,read_count,update_count,delete_count']
    for key in result:
        to_writer.append(rf'{",".join([str(g) for g in result[key]])}')
    writer.write('\n'.join(to_writer))
    writer.close()