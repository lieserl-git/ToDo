import flet as ft


@ft.control
class TodoApp(ft.Column):
    def init(self):
        self.new_task = ft.TextField(hint_text="What do you want to do today?", expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls = [ft.Row(controls=[self.new_task,ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked, foreground_color = ft.Colors.BLACK, bgcolor = ft.Colors.WHITE),],),self.tasks_view,]

    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


def main(page: ft.Page):
    page.title = "To-Do App"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 500
    page.window.height = 500
    page.window.resizable = False

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)
    
ft.run(main)
