# Faker GUI

一个基于Python Faker和Flet框架开发的假数据生成工具，提供友好的图形界面，支持多种数据类型的生成和导出。

## 功能特点

- 支持多种数据类型生成：
  - 基础类型：姓名、地址、电话号码、电子邮件等
  - 扩展类型：身份证号、银行卡号、车牌号等
- 批量数据生成
- 数据预览功能
- 多格式数据导出（CSV、JSON、TXT）
- 完整的日志记录系统

## 安装要求

- Python >= 3.8
- 依赖包：
  - flet >= 0.25.0
  - faker >= 20.0.0
  - pandas >= 2.0.0
  - flet-desktop >= 0.25.2

## 快速开始

1. 克隆项目：
```
bash
git clone https://github.com/danny11086/faker-gui.git
cd faker-gui
```
2. 安装依赖：
```
bash
pip install -r requirements.txt
```
3. 运行程序：
```
bash
python main.py
```

## 使用说明

- 在图形界面中，选择需要生成的数据类型和数量。
- 点击“生成”按钮，程序将生成相应的假数据。
- 点击“预览”按钮，可以查看生成的数据。
## 项目结构

```

faker-gui/
├── src/ # 源代码目录
│ ├── init.py
│ ├── app.py # 主应用程序
│ ├── components/ # UI组件
│ │ ├── init.py
│ │ ├── data_generator.py
│ │ ├── data_preview.py
│ │ └── data_export.py
│ └── utils/ # 工具函数
│ ├── init.py
│ ├── faker_utils.py
│ └── logger.py
├── logs/ # 日志目录
├── exports/ # 数据导出目录
├── run.py # 启动脚本
├── README.md
└── pyproject.toml # 项目配置
```

## 使用说明

1. 数据生成
   - 从下拉菜单选择要生成的数据类型
   - 输入需要生成的数据数量
   - 点击"生成数据"按钮

2. 数据预览
   - 在预览标签页查看生成的数据
   - 支持表格形式展示

3. 数据导出
   - 选择导出格式（CSV/JSON/TXT）
   - 点击"导出数据"按钮
   - 导出的文件将保存在 exports 目录下

## 日志系统

- 所有操作日志保存在 `logs` 目录下
- 日志文件名格式：`YYYYMMDD_HHMMSS.log`
- 记录内容包括：
  - 应用程序启动和初始化
  - 数据生成操作
  - 导出操作
  - 错误和异常信息

## 开发说明

### 添加新的数据类型
在 `src/utils/faker_utils.py` 中的 `FakerUtils` 类中添加新的数据生成方法：

### 自定义导出格式
在 `src/components/data_export.py` 中的 `DataExport` 类中扩展导出功能：

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

[MIT License](LICENSE)

## 联系方式

- 项目维护者：Your Name
- 邮箱：your.email@example.com
- 项目链接：[GitHub](https://github.com/danny11086/faker-gui)

## 更新日志

### v0.1.0 (2024-01-18)
- 初始版本发布
- 实现基本的数据生成功能
- 添加数据预览和导出功能
- 集成日志系统