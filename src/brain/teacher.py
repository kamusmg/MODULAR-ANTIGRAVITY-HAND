import time

class TeacherMind:
    def __init__(self):
        self.steps = [
            {
                "pensamento": "PASSO 1: Preciso encontrar o menu Iniciar. Vou apertar a tecla Windows.",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {"teclas_especiais": ["win"]}
            },
            {
                "pensamento": "PASSO 2: O menu abriu. Agora vou digitar o nome do programa: 'mspaint'.",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {"texto": "mspaint"}
            },
            {
                "pensamento": "PASSO 3: Vejo o ícone do Paint. Vou confirmar com ENTER.",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {"teclas_especiais": ["enter"]}
            },
            {
                "pensamento": "TAREFA CONCLUÍDA: O Paint deve estar abrindo agora. Aguardando...",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {}
            }
        ]
        self.current_step = 0
        self.start_time = time.time()
        self.last_action_time = 0

    def think(self, visual_input):
        current_time = time.time()
        
        # Wait 3 seconds between steps to mimic "thinking" / observing
        if current_time - self.last_action_time < 4.0:
             return {
                "pensamento": "Observando resultado...",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {}
            }

        if self.current_step < len(self.steps):
            action = self.steps[self.current_step]
            self.current_step += 1
            self.last_action_time = current_time
            return action
        else:
            return {
                "pensamento": "Aguardando novas instruções do Mestre Antigravity...",
                "comando_mouse": {"direcao": "PARADO"},
                "comando_teclado": {}
            }
