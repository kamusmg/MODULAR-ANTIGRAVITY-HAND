import random
import json
import time

class MockMind:
    def __init__(self):
        self.thoughts = [
            "Procurando ícone do Iniciar...",
            "A tela parece brilhante hoje.",
            "Detectei movimento no canto superior.",
            "Vou tentar clicar na barra de tarefas.",
            "O cursor está longe do alvo. Corrigindo.",
            "Analisando pixels da área central.",
            "Nada interessante aqui. Movendo foco.",
            "Tentativa de interação com a janela."
        ]
        self.directions = ["CIMA", "BAIXO", "ESQUERDA", "DIREITA", "COD_ESQUERDA_CIMA", "COD_DIREITA_BAIXO"]
        self.actions = ["NENHUMA", "NENHUMA", "NENHUMA", "CLIQUE_ESQUERDO"]
        
    def think(self, visual_input):
        """
        Simulates AI processing.
        Returns a dictionary representing the JSON response.
        """
        # Simulate processing time
        # time.sleep(0.1) 
        
        thought = random.choice(self.thoughts)
        direction = random.choice(self.directions)
        action = random.choice(self.actions)
        
        # Occasional typing
        text = ""
        if random.random() < 0.1:
            text = "Hello World"
            
        return {
            "pensamento": thought,
            "status_emocional": "Curioso/Simulado",
            "comando_mouse": {
                "direcao": direction,
                "intensidade": "BAIXA" if random.random() > 0.5 else "MEDIA",
                "acao": action
            },
            "comando_teclado": {
                "texto": text
            },
            "log_aprendizado": f"Simulação step {int(time.time())}"
        }
