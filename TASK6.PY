print('Преобразование минут в часы и минуты')
print()
minutes = 90
hours = minutes // 60
remaining_minutes = minutes % 60
print(f'{minutes} минут = {hours} часов {remaining_minutes} минут')
print(f'Часы: {hours}')
print(f'Минуты: {remaining_minutes}')
