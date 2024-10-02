from datetime import date, datetime, time

# Somente dia
data = date(2024, 10, 1)
print(data)
print(data.today())

# Dia e horário
data_hora = datetime(2024, 10, 1, 20, 12)
print(data_hora)
print(data_hora.today())

# Somente horário
hora = time(20, 12, 0)
print(hora)
