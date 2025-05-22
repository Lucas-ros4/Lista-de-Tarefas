import flet as ft #importa flet com o apelido como ft
from custom_checkbox import Checkbox

def main(page: ft.Page):
    #configurações da pagina
    page.title = "Lista de Tarefas"  #titulo
    page.theme_mode = ft.ThemeMode.LIGHT  #define o tema como claro ou escuro
    page.window.width = 450                #tamanho da largura
    page.window.height = 650               #tamanho da altura
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)    #coloca espaços em todos os lados
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER         #alinhas o conteudo das linhas no centro da pagina

    WIDTH: int = page.width     
    HEIGHT: int = page.height
    print(WIDTH, HEIGHT)       # imprime a largura e autra da pagina

    def add_task(e):   #função para adiconar tarefas e o paremero e é o evento
        #print(new_task.value)
        if new_task.value == "":   #se o campo estiver vazio foca no campo e não adiciona nada
            new_task.focus()
            return
        task_list.controls.append(Checkbox(new_task.value))   #adiciona um elemento novo a lista do tipo checkbox e recebe o valor digitado
        new_task.value = ''  #limpa a parte de escrever
        page.update() #atualiza a pagina
        new_task.focus()  #volta o foco para o campo de escrita
    
  
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True,  #autofocus é para adiconar automaticament ao precionar enter
                            autofocus=True, on_submit=add_task)
    new_button = ft.FloatingActionButton(icon="ADD", on_click=add_task)  #adiciona o icone adicionar chamado add_task

    task_list = ft.Column(spacing=0, height=HEIGHT-170, scroll=ft.ScrollMode.ADAPTIVE)   #coluna onde as tarefas vão aparecer com rolagem adaptativa(muito util para quanti tiver muitas tarefas)
  
    card = ft.Column(    #card é o conteiner principal com a lihas princial que tem o campo de escrita e o botão para adiconar a lista
        width=450,
            controls=[
                ft.Row(
                    controls=[
                        new_task,   #campo de escrita 
                        new_button  #botao para adiconar a lissta
                    ]
                ),
                task_list,
            ]
        )


    page.add(card)  #aciona card a interface da pagina
    

ft.app(target=main)