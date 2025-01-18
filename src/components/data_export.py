import flet as ft
import pandas as pd
from pathlib import Path
from src.utils.logger import setup_logger

class DataExport(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.data = []
        self.export_formats = ["CSV", "JSON", "TXT"]
        self.logger = setup_logger("faker_gui.export")

    def build(self):
        self.format_dropdown = ft.Dropdown(
            label="导出格式",
            options=[ft.dropdown.Option(f) for f in self.export_formats],
            width=200,
        )

        self.export_button = ft.ElevatedButton(
            text="导出数据",
            on_click=self.export_data
        )

        self.status_text = ft.Text(
            value="",
            color=ft.colors.GREY,
            size=14
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("数据导出", size=20, weight=ft.FontWeight.BOLD),
                    self.format_dropdown,
                    self.export_button,
                    self.status_text,
                ],
                spacing=20,
            ),
            padding=20,
        )

    def update_data(self, data: list):
        """更新要导出的数据"""
        self.data = data
        self.logger.info(f"更新导出数据: {len(data)}条")

    def export_data(self, e):
        """导出数据到文件"""
        try:
            if not self.data:
                self.status_text.value = "没有可导出的数据"
                self.status_text.color = ft.colors.RED
                self.status_text.update()
                self.logger.warning("尝试导出空数据")
                return

            export_format = self.format_dropdown.value
            if not export_format:
                self.status_text.value = "请选择导出格式"
                self.status_text.color = ft.colors.RED
                self.status_text.update()
                self.logger.warning("未选择导出格式")
                return

            # 创建导出目录
            export_dir = Path("exports")
            export_dir.mkdir(exist_ok=True)

            # 导出数据
            df = pd.DataFrame(self.data, columns=["数据"])
            file_path = export_dir / f"fake_data.{export_format.lower()}"

            if export_format == "CSV":
                df.to_csv(file_path, index=False, encoding="utf-8")
            elif export_format == "JSON":
                df.to_json(file_path, force_ascii=False, indent=2)
            elif export_format == "TXT":
                df.to_csv(file_path, index=False, sep="\t", encoding="utf-8")

            self.status_text.value = f"数据已导出到: {file_path}"
            self.status_text.color = ft.colors.GREEN
            self.status_text.update()
            self.logger.info(f"数据成功导出到: {file_path}")

        except Exception as e:
            error_msg = f"导出数据时发生错误: {str(e)}"
            self.status_text.value = error_msg
            self.status_text.color = ft.colors.RED
            self.status_text.update()
            self.logger.error(error_msg, exc_info=True) 