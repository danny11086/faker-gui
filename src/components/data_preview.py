import flet as ft

class DataPreview(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.data = []

    def build(self):
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("序号")),
                ft.DataColumn(ft.Text("数据")),
            ],
            rows=[],
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("数据预览", size=20, weight=ft.FontWeight.BOLD),
                    self.data_table,
                ],
                spacing=20,
            ),
            padding=20,
        )

    def update_preview(self, data: list):
        """更新预览数据"""
        self.data = data
        self.data_table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(i + 1))),
                    ft.DataCell(ft.Text(str(item))),
                ]
            )
            for i, item in enumerate(data)
        ]
        self.update() 