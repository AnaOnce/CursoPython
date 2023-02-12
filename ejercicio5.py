print('Proporcione los siguientes datos del libro:')
Nombre=input('Proporciona el nombre: ')
ID=int(input('Proporciona el ID: '))
precio=float(input('Proporcione el precio: '))
Envio=input('Indica si el envio es gratuito (True / False): ')

if Envio=='True':
     Envio=True
elif Envio=='False':
    Envio=False
else:
    Envio= 'Valor incorrecto, debe escribir True/False'       



print(f'''
  Nombre: {Nombre}
  ID: {ID}
  Precio: {precio}
  Envio Gratuito?: {Envio}
''')