from entities.task import Task
from repository.task_repository import TaskRepository

class TaskService:

    def __init__(self):
        self.repository = TaskRepository()

    def create_task(self, title, description):
        # Validar dados
        # Criar entidade
        # Solicitar persistência
        pass

    def list_tasks(self):
        return self.repository.find_all()

    def get_task(self, task_id):
        return self.repository.find_by_id(task_id)

    def update_task(self, task_id, title, description):
        # Validar e atualizar tarefa
        pass

    def delete_task(self, task_id):
        return self.repository.delete(task_id)