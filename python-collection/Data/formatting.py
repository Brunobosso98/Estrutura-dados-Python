from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-10-03 16:47"
mascara_en = "%Y-%m-%d %H:%M"

# STRFTIME: retorna uma string representando a data
print(data_hora_atual.strftime("%d/%m/%Y %a %H:%M"))

# STRPTIME: cria um objeto datetime a partir de uma string que representa a data e hora
print(datetime.strptime(data_hora_str, mascara_en))