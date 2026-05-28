import flet as ft


class Task(ft.Column):
    def __init__(self, task_name: str, on_task_delete=None):
        super().__init__()
        self.task_name = task_name
        self.on_task_delete = on_task_delete if on_task_delete else lambda task: None

        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.display_task, ft.Row(spacing=0, controls=[ft.IconButton(icon=ft.Icons.CREATE_OUTLINED, tooltip="Edit To-Do", on_click=self.edit_clicked,),ft.IconButton(ft.Icons.DELETE_OUTLINED, tooltip="Delete To-Do", on_click=self.delete_clicked,),],),],)

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.edit_name, ft.IconButton( icon=ft.Icons.DONE_OUTLINE, icon_color=ft.Colors.WHITE, tooltip="Update To-Do", on_click=self.save_clicked,),],)
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.on_task_delete(self)


class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What do you want to do today?", expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls = [ft.Row(controls=[self.new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked, foreground_color=ft.Colors.BLACK,bgcolor=ft.Colors.WHITE,),],),self.tasks_view]

    def add_clicked(self, e):
        task = Task(
            task_name=self.new_task.value,
            on_task_delete=self.task_delete
        )
        self.tasks_view.controls.append(task)   
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks_view.controls.remove(task)   
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