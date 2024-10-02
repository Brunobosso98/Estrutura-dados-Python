from datetime import date, datetime, timedelta, time

tipo_carro = input("Digite o tamanho do carro, P, M ou G. \n" )
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 2
# data_atual = datetime.today()
data_atual = datetime.utcnow()


if tipo_carro == "p":
  data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
  print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == "m":
  data_estimada = data_atual + timedelta(minutes=tempo_medio)
  print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == "g":
  data_estimada = data_atual + timedelta(days=tempo_grande)
  print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
  print("Digite um valor entre os tamanho P,M ou G.")

print(date.today() - timedelta(days=1))

# Não é possível trabalhar apenas com time, o datetime é necessário
resultado = datetime(2024, 10, 2, 12, 10, 20) - timedelta(hours=1)
print(resultado.time())