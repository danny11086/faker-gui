import flet as ft
from src.utils.faker_utils import FakerUtils
from src.utils.logger import setup_logger

class DataGenerator(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.faker_utils = FakerUtils()
        self.logger = setup_logger("faker_gui.generator")
        self.data_types = [
            "姓名", "地址", "电话号码", "电子邮件", "公司名称",
            "职位", "日期时间", "身份证号", "银行卡号", "车牌号"
        ]
        # 添加数据预览和导出的回调函数
        self.on_data_generated = None

    def build(self):
        self.data_type_dropdown = ft.Dropdown(
            label="数据类型",
            options=[ft.dropdown.Option(t) for t in self.data_types],
            width=200,
        )

        self.count_input = ft.TextField(
            label="生成数量",
            value="1",
            width=200,
            input_filter=ft.NumbersOnlyInputFilter(),
        )

        self.generate_button = ft.ElevatedButton(
            text="生成数据",
            on_click=self.generate_data
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("数据生成设置", size=20, weight=ft.FontWeight.BOLD),
                    self.data_type_dropdown,
                    self.count_input,
                    self.generate_button,
                ],
                spacing=20,
            ),
            padding=20,
        )

    def generate_data(self, e):
        """生成数据并通知其他组件"""
        try:
            data_type = self.data_type_dropdown.value
            if not data_type:
                self.logger.warning("未选择数据类型")
                return
            
            count = int(self.count_input.value or "1")
            if count < 1:
                self.logger.warning("生成数量必须大于0")
                return
                
            self.logger.info(f"开始生成数据: 类型={data_type}, 数量={count}")
            generated_data = self.faker_utils.generate_data(data_type, count)
            self.logger.info(f"成功生成{len(generated_data)}条数据")
            
            # 通知其他组件更新数据
            if self.on_data_generated:
                self.on_data_generated(generated_data)
                
        except Exception as e:
            self.logger.error(f"生成数据时发生错误: {str(e)}", exc_info=True) 