from faker import Faker
from typing import List, Any

class FakerUtils:
    def __init__(self):
        self.faker = Faker(['zh_CN'])
        self.data_type_mapping = {
            "姓名": self.faker.name,
            "地址": self.faker.address,
            "电话号码": self.faker.phone_number,
            "电子邮件": self.faker.email,
            "公司名称": self.faker.company,
            "职位": self.faker.job,
            "日期时间": self.faker.date_time,
            "身份证号": self.faker.ssn,
            "银行卡号": self.faker.credit_card_number,
            "车牌号": lambda: "".join([self.faker.random_element(['京','沪','粤','津','冀','晋','蒙','辽','吉','黑']),
                                   self.faker.random_letter().upper(),
                                   self.faker.numerify('#####')])
        }

    def generate_data(self, data_type: str, count: int = 1) -> List[Any]:
        """
        生成指定类型和数量的假数据
        """
        if data_type not in self.data_type_mapping:
            raise ValueError(f"Unsupported data type: {data_type}")
            
        generator = self.data_type_mapping[data_type]
        return [generator() for _ in range(count)] 