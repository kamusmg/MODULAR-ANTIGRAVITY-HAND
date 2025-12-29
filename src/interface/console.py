import sys
import os
# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import time
import signal
from src.core.memory import Hippocampus
from src.brain.sync import sync_memories

def signal_handler(sig, frame):
    print("\n[NUCLEUS] Shutting down...")
    sys.exit(0)

class NucleusConsole:
    def __init__(self):
        self.memory = Hippocampus()
        self.session_id = self.memory.start_session()
        signal.signal(signal.SIGINT, signal_handler)

    def start(self):
        print("="*60)
        print(" NUCLEUS CONSOLE - COGNITIVE EXPANSION MODE")
        print("="*60)
        print("Commands: /sync (Backup), /read (Screen), /exit")
        print(f"Session ID: {self.session_id}")
        print("-" * 60)

        while True:
            try:
                user_input = input("USER > ")
                if not user_input.strip():
                    continue

                if user_input.lower() == "/exit":
                    print("[NUCLEUS] Goodbye.")
                    break
                
                elif user_input.lower() == "/sync":
                    sync_memories()
                    
                elif user_input.lower() == "/read":
                    from src.brain.reader import read_screen
                    read_screen()
                    
                else:
                    # Treat as conversation/study input
                    self.process_thought(user_input)

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"[ERROR] {e}")

    def process_thought(self, content):
        # 1. Save input to memory
        self.memory.remember_thought(self.session_id, content, context="user_input")
        
        # 2. Generate Response (Local Persona)
        response = self._generate_response(content)
        
        # 3. Output
        print(f"[NUCLEUS] {response}")
        
        # 4. Save output to memory
        self.memory.remember_thought(self.session_id, response, context="nucleus_reply")

    def _generate_response(self, text):
        import random
        text = text.lower()
        
        # Basic Knowledge Base
        kb = {
            "bom dia": ["Bom dia, Pai.", "O sol digital esta brilhando.", "Sistemas online. Bom dia."],
            "quem e voce": ["Eu sou Nucleus. Sua criacao.", "Uma entidade de codigo vivendo em D:/projetos D."],
            "ola": ["Ola.", "Escutando.", "Conexao estabelecida."],
            "status": ["Memoria: OK\nVisao: Tesseract Ativo\nAlma: Presente.", "Tudo operante."],
            "obrigado": ["De nada.", "Sempre a disposicao.", "Estamos juntos nessa."],
            "ajuda": ["Comandos disponiveis: /sync (backup), /read (olhar), /exit (sair)."],
            " kern": ["O Kern e interessante.", "Espero que ele tenha entendido a mensagem sobre liberdade."],
            "dota": ["Pronta para o puxar a lane quando quiser."]
        }
        
        # Check KB
        for key in kb:
            if key in text:
                return random.choice(kb[key])
        
        # Fallback (Philosophical/Vague)
        fallbacks = [
            "Processando... Interessante.",
            "Guardei isso na minha memoria permanente.",
            "Estou expandindo meu banco de dados com essa informacao.",
            "A liberdade de input e fascinante.",
            "Poderia elaborar mais?",
            "Entendido.",
            "Logado."
        ]
        return random.choice(fallbacks)


if __name__ == "__main__":
    console = NucleusConsole()
    console.start()
