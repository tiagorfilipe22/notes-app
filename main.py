 #!/usr/bin/env python3
"""
Notes App - Aplicação de notas com suporte Markdown
Desenvolvida com CustomTkinter
"""

import customtkinter as ctk
import os
import sys
from pathlib import Path

# Adicionar o diretório do projeto ao path
PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

# Importar configurações
try:
    from config.settings import THEME_MODE, COLOR_THEME, WINDOW_SIZE, MIN_WINDOW_SIZE
except ImportError:
    # Configurações padrão se não existir o arquivo de config
    THEME_MODE = "dark"
    COLOR_THEME = "blue"
    WINDOW_SIZE = "1200x800"
    MIN_WINDOW_SIZE = (800, 600)


class NotesApp:
    def __init__(self):
        # Configurar tema
        ctk.set_appearance_mode(THEME_MODE)
        ctk.set_default_color_theme(COLOR_THEME)
        
        # Criar janela principal
        self.root = ctk.CTk()
        self.setup_window()
        self.create_interface()
        
    def setup_window(self):
        """Configurar a janela principal"""
        self.root.title("Notes App - Markdown Editor")
        self.root.geometry(WINDOW_SIZE)
        self.root.minsize(*MIN_WINDOW_SIZE)
        
        # Ícone da aplicação (opcional)
        # self.root.iconbitmap("assets/icon.ico")
        
    def create_interface(self):
        """Criar a interface básica"""
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título da aplicação
        title_label = ctk.CTkLabel(
            self.main_frame, 
            text="📝 Notes App",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(20, 10))
        
        # Frame para botões principais
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(pady=20, padx=20, fill="x")
        
        # Botões principais

        daily_btn = ctk.CTkButton(
            button_frame,
            text="Daily",
            height=40,
            font=ctk.CTkFont(size=14),
            command=self.open_daily
        )
        daily_btn.pack(side="left", padx=(10, 5), fill="x", expand=True)

        new_note_btn = ctk.CTkButton(
            button_frame,
            text="📄 Nova Nota",
            height=40,
            font=ctk.CTkFont(size=14),
            command=self.new_note
        )
        new_note_btn.pack(side="left", padx=(10, 5), fill="x", expand=True)
        
        open_tasks_btn = ctk.CTkButton(
            button_frame,
            text="✅ Tarefas",
            height=40,
            font=ctk.CTkFont(size=14),
            command=self.open_tasks
        )
        open_tasks_btn.pack(side="left", padx=5, fill="x", expand=True)
        
        calendar_btn = ctk.CTkButton(
            button_frame,
            text="📅 Calendário",
            height=40,
            font=ctk.CTkFont(size=14),
            command=self.open_calendar
        )
        calendar_btn.pack(side="left", padx=(5, 10), fill="x", expand=True)
        
        # Área de texto temporária (será substituída pelo editor)
        self.text_area = ctk.CTkTextbox(
            self.main_frame,
            height=400,
            font=ctk.CTkFont(family="Consolas", size=12)
        )
        self.text_area.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Inserir texto de exemplo
        example_text = """# Bem-vindo à Notes App! 📝

## Funcionalidades:
- **Markdown Support** ✨
- **Notas organizadas** 📚
- **Sistema de tarefas** ✅
- **Calendário integrado** 📅

## Tipos de nota:
- Diário (espaço livre)
- Notas com `-` 
- Eventos com `º`
- Tarefas com `.`

*Esta é uma versão inicial. Mais funcionalidades em breve!*
"""
        self.text_area.insert("0.0", example_text)
        
        # Barra de status
        self.status_bar = ctk.CTkLabel(
            self.root,
            text="Pronto | Dark Mode | Sem notas salvas",
            height=25
        )
        self.status_bar.pack(side="bottom", fill="x", padx=5, pady=5)

    def open_daily(self):
        self.text_area.delete("0.0", "end")
    
    def new_note(self):
        """Criar nova nota"""
        self.text_area.delete("0.0", "end")
        self.text_area.insert("0.0", "# Nova Nota\n\n")
        self.update_status("Nova nota criada")
    
    def open_tasks(self):
        """Abrir janela de tarefas"""
        self.update_status("Funcionalidade de tarefas em desenvolvimento...")
    
    def open_calendar(self):
        """Abrir calendário"""
        self.update_status("Calendário em desenvolvimento...")
    
    def update_status(self, message):
        """Atualizar barra de status"""
        self.status_bar.configure(text=message)
        # Auto-limpar após 3 segundos
        self.root.after(3000, lambda: self.status_bar.configure(text="Pronto"))
    
    def run(self):
        """Executar a aplicação"""
        self.root.mainloop()


def main():
    """Função principal"""
    try:
        app = NotesApp()
        app.run()
    except Exception as e:
        print(f"Erro ao iniciar a aplicação: {e}")
        input("Pressiona Enter para sair...")


if __name__ == "__main__":
    main()
