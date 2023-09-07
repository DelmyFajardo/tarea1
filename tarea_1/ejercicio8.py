precio = input  ("ingrese el precio de su producto con dos decimales  \n ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')