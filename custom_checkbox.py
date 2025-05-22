import flet as ft

class Checkbox(ft.Row):  #cria a classe Checkbox qeu herda de ft.row(a linha horizontal)
    def __init__(self, text):
        super().__init__()  #inicializa com o construtor da Row
        self.text_view = ft.Text(text)   #texto visivel
        self.text_edit = ft.TextField(text, visible=False)  #campo de texto invisivel, usado ao editar uma tarefa
        self.edit_button = ft.IconButton(icon="EDIT", on_click=self.edit)
        self.save_button = ft.IconButton(icon="SAVE", on_click=self.save,    #botoes editar salvar e deletar invisiveis(até adicionar um elemento a lista)
                                         visible=False, icon_color="green") #por que isso continua dando problema, editar deopis !!
        self.delete_button = ft.IconButton(icon="DELETE", on_click=self.delete,
                                           icon_color="red")

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN  #serara os botões de a esquerda e a direita

        self.controls = [
            ft.Row(  # lado esquerdo checkbox + texto
                controls=[
                    ft.Checkbox(),
                    self.text_view,
                    self.text_edit,
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,  # ocupa o máximo de espaço possível
            ),
            ft.Row(  # lado direito botões
                controls=[
                    self.edit_button,
                    self.save_button,
                    self.delete_button,
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.END,
            )
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.delete_button.visible = False
        self.text_view.visible = False
        self.save_button.visible = True
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.save_button.visible = False
        self.text_edit.visible = False
        self.edit_button.visible = True
        self.delete_button.visible = True
        self.text_view.visible = True
        if self.text_edit.value == "":
            return
        self.text_view.value = self.text_edit.value
        self.update()

    def delete(self, e):
        self.visible = False
        self.update()


