class Rscord:
    """
数据封装类
把读取的数据封装到类中保证数据安全
    """
    def __init__(self,date,order_id,money,province):
        self.date = date    #日期
        self.order_id = order_id    #订单ID
        self.money= money    #订单金额
        self.province = province  #省份
    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"
