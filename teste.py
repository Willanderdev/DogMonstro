carrinho = [{'id_produto': 4, 'observacoes': '', 'preco': 20.0, 'quantidade': 1}, {
    'id_produto': 3, 'observacoes': '', 'preco': 20.0, 'quantidade': 2}, {'id_produto': 1, 'observacoes': '', 'preco': 20.0, 'quantidade': 8}]
y=1
x = [i['id_produto'] for i in carrinho]
print(x)
print(x.index(y))
# num=0
# for i in x:
    
#     if i == y:
#         print('ok')
#         print(num)
    
       

if y in x:
    carrinho[x.index(y)]['quantidade'] += 1
    print(carrinho)
