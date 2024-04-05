# Lista dos produtos disponíveis
produtos = ["Guaravita", "Salgado", "Limao", "Laranja"]  
# Lista dos preços correspondentes aos produtos
preco = [2.00, 5.00, 3.00, 1.50]  
# Inicialização do total do pedido como zero
total_pedido = 0  
# Lista para armazenar os produtos escolhidos pelo cliente
produtos_escolhidos = []  
# Exibe os produtos disponíveis ao cliente
print("Produtos disponíveis:", produtos)
# Loop principal que permite ao cliente fazer pedidos até decidir sair

while True:
    # Solicita ao cliente que digite seu pedido
    pedido = input("Digite o Seu Pedido (Digite 'Sair' para Encerrar): ").capitalize()  

    # Verifica se o cliente decidiu sair
    if pedido == "Sair":
        # Exibe os produtos escolhidos se houver algum
        print("Produtos escolhidos:")
        if produtos_escolhidos:
            for produto in produtos_escolhidos:
                print(produto)
            print(f"Total a pagar: R$ {total_pedido:.2f}")
        else:
            print("Nenhum produto escolhido.")
        print("Obrigado por comprar!")
        break

    # Verifica se o pedido do cliente está na lista de produtos disponíveis
    if pedido in produtos:
        # Obtem o índice do produto na lista de produtos
        index_produto = produtos.index(pedido)  
        # Adiciona o preço do produto ao total do pedido
        total_pedido += preco[index_produto]  
        # Adiciona o produto à lista de produtos escolhidos
        produtos_escolhidos.append(pedido)  
        # Informa ao cliente sobre o pedido realizado e seu preço
        print(f"Você escolheu {pedido}, que custa R$ {preco[index_produto]:.2f}")
    else:
        # Informa ao cliente que o produto não existe
        print("Esse produto não existe.")