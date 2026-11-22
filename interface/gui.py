from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n=== Catálogo de Discos ===")
            print("1 - Cadastrar disco")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_disco()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
                
    def cadastrar_disco(self):
        titulo = input("Título: ")
        artista = input("Artista: ")

        try:
            ano = int(input("Ano de lançamento: "))
        except ValueError:
            print("O ano deve ser um número inteiro.")
            return

        descricao = input("Descrição (opcional): ")

        try:
            disco_id = self.services.create(
                titulo=titulo,
                artista=artista,
                ano=ano,
                descricao=descricao
                )
        except ValueError as erro:
            print(erro)
            return

        print(f"Disco cadastrado com sucesso! ID: {disco_id}")