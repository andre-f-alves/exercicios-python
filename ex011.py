print('Pintando a parede')
l = float(input('Primeiro, diga-me a largura da parede: '))
a = float(input('Agora, me diga a altura da parede: '))
área = l * a
tinta = área / 2
print(f'sua parede mede {l}x{a}, tendo uma área de {área:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.3f}L de tinta.')
