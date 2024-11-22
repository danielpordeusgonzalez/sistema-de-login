import Controller

print("olá, seja bem vindo! escolha o número 1 para cadastrar um usuario e número 2 para logar na sua conta e 3 para sair do programa.")
opcao = int(input('Qual a sua escolha? 1, 2 ou 3? '))

while True:
    
    if opcao == 1:
        nome = str(input("digite seu nome: "))
        email = str(input("digite seu email: "))
        senha = str(input("digite sua senha: "))
        Controller.ControllerCadastro.cadastro(nome=nome, email=email, senha=senha)
        opcao = int(input('voce quer cadastrar mais alguém digite 1 ou se algo der errado quer tentar de novo digite 2, se não digite 3: '))
        if opcao == 3:
            break
        
    elif opcao == 2:
        email = str(input("digite seu email: "))
        senha = str(input("digite sua senha: "))
        Controller.ControllerLogin.login(email=email, senha=senha)
        break
        
        
    else:
        break