from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n=== Catálogo de Discos ===")
            print("1 - Cadastrar disco")
            print("2 - Listar discos")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_disco()
                
            elif opcao == "0":
                break
            
            elif opcao == "2":
                self.listar_discos()
                
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
        
    def listar_discos(self):
        discos = self.services.list()
        
        if not discos:
            print("Nenhum disco cadastrado.")
            
        for disco in discos:
            situacao = "Ouvido" if disco.ouvido else "Não ouvido"
            
            print(f"\nID: {disco.id}")
            print(f"Título: {disco.titulo}")
            print(f"Artista: {disco.artista}")
            print(f"Ano: {disco.ano}")
            print(f"Descrição: {disco.descricao or 'Sem descrição'}")
            print(f"Situação: {situacao}")
            