from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n=== Catálogo de Discos ===")
            print("1 - Cadastrar disco")
            print("2 - Listar discos")
            print("3 - Buscar por ID")
            print("4 - Editar disco")
            print("5 - Deletar disco")
            print("6 - Marcar discoo como ouvido")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_disco()
                
            elif opcao == "0":
                break
            
            elif opcao == "2":
                self.listar_discos()
                
            elif opcao == "3":
                self.buscar_disco_id()
                
            elif opcao == "4":
                self.editar_disco()
                
            elif opcao == "5":
                self.deletar_disco()
                
            elif opcao == "6":
                self.disco_ouvido()
                
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
            
            
    def buscar_disco_id(self):
        try:
            disco_id = int(input("ID do disco: "))
        except ValueError:
            print("Digite um ID inteiro.")
            return
            
        try:
            disco = self.services.get(disco_id)
        except OverflowError:
            print("O ID informado é grande demais.")
            return
        
        if disco is None:
            print("Disco não encontrado")
            
        situacao = "Ouvido" if disco.ouvido else "Não ouvido"
        
        print(f"\nID: {disco.id}")
        print(f"Título: {disco.titulo}")
        print(f"Artista: {disco.artista}")
        print(f"Ano: {disco.ano}")
        print(f"Descrição: {disco.descricao or 'Sem descrição'}")
        print(f"Situação: {situacao}")
        
    def editar_disco(self):
        try:
            disco_id = int(input("ID do disco que deseja editar: "))
        except ValueError:
            print("Digite um ID inteiro.")
            return

        titulo = input("Novo título: ")
        artista = input("Novo artista: ")

        try:
            ano = int(input("Novo ano de lançamento: "))
        except ValueError:
            print("O ano deve ser um número inteiro.")
            return

        descricao = input("Nova descrição (opcional): ")

        try:
            atualizado = self.services.update(
                disco_id=disco_id,
                titulo=titulo,
                artista=artista,
                ano=ano,
                descricao=descricao,
            )
        except ValueError as erro:
            print(erro)
            return
        except OverflowError:
            print("O ID ou o ano informado está fora do intervalo aceito.")
            return

        if atualizado:
            print("Disco atualizado com sucesso!")
        else:
            print("Disco não encontrado.")
            
    def deletar_disco(self):
        try:
            disco_id = int(input("Digite o Id a ser deletado: "))
        except ValueError:
            ("Digite um ID inteiro.")
            return
        try:
            disco_deletar = self.services.get(disco_id)
        except OverflowError:
            print("O ID informado está fora do intervalo aceito.")
            return
        
        if disco_deletar is None:
            print("Disco não encontrado.")
            return
        
        print(f"Disco selecionado: {disco_deletar.titulo} — {disco_deletar.artista} (ID {disco_deletar.id})")
        resposta = input("Confirma a exclusão? [s/n]: ").strip().lower()
        
        if resposta != "s":
            print("Exclusão cancelada.")
            return
        if self.services.delete(disco_id):
            print("Disco excluído com sucesso!")
        else:
            print("Disco não encontrado.")
            
    def disco_ouvido(self):
        try:
            disco_id = int(input("ID do disco que deseja marcar como ouvido: "))
        except ValueError:
            print("Digite um ID inteiro.")
            return

        try:
            atualizado = self.services.marcar_como_ouvido(disco_id)
        except OverflowError:
            print("O ID informado está fora do intervalo aceito.")
            return

        if atualizado:
            print("Disco marcado como ouvido!")
        else:
            print("Disco não encontrado.")
            