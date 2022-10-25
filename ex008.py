print('Convertendo em centímetros e milímetros')
m = float(input('Digite uma distância em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print(f'{m}m é equivalente a:\n{km}km\n{hm}hm\n{dam}dam\n{cm:.0f}cm\n{mm:.0f}mm')
