import flet as ft
from src.components.data_generator import DataGenerator
from src.components.data_preview import DataPreview
from src.components.data_export import DataExport
from src.utils.logger import setup_logger

class FakerGUI:
    def __init__(self):
        self.page = None
        self.data_generator = None
        self.data_preview = None
        self.data_export = None
        self.logger = setup_logger("faker_gui.app")

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Faker GUI"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        
        try:
            # 初始化组件
            self.data_generator = DataGenerator()
            self.data_preview = DataPreview()
            self.data_export = DataExport()
            
            # 设置组件间的数据流
            self.data_generator.on_data_generated = self.on_data_generated
            
            # 创建主布局
            self.page.add(
                ft.Row(
                    controls=[
                        ft.Text("Faker GUI", size=30, weight=ft.FontWeight.BOLD)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Tabs(
                    selected_index=0,
                    tabs=[
                        ft.Tab(
                            text="数据生成",
                            content=self.data_generator
                        ),
                        ft.Tab(
                            text="数据预览",
                            content=self.data_preview
                        ),
                        ft.Tab(
                            text="数据导出",
                            content=self.data_export
                        ),
                    ],
                    expand=True,
                )
            )
            
            self.logger.info("应用程序初始化完成")
            
        except Exception as e:
            self.logger.error(f"应用程序初始化失败: {str(e)}", exc_info=True)
            raise

    def on_data_generated(self, data: list):
        """处理新生成的数据"""
        try:
            self.logger.info(f"收到新生成的数据: {len(data)}条")
            # 更新预览
            self.data_preview.update_preview(data)
            # 更新导出组件
            self.data_export.update_data(data)
            self.logger.info("数据更新完成")
        except Exception as e:
            self.logger.error(f"处理新数据时发生错误: {str(e)}", exc_info=True)

def main():
    app = FakerGUI()
    ft.app(target=app.main)
