import json
from file_Define import Rscord
class Reader:
    pass
    """
    数据读取顶层类
    """
    #数据读取父类方法
    def read_data(self)-> list[Rscord]:
        pass
#txt文本读取子类
class Txt_Read_Data(Reader): #继承
    def __init__(self,path):   #path为文件打开地址
        self.path = path
    def read_data(self) -> list[Rscord]:   #实现复写
        txt_list: list[Rscord]= []
        f = open(self.path,'r',encoding='UTF-8')
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            rscord = Rscord(data_list[0],data_list[1],int(data_list[2]),data_list[3])#难点
            txt_list.append(rscord)
        f.close()
        return txt_list
class Json_Read_Data(Reader): #继承
    def __init__(self,path):
        self.path = path  #文件地址
    def read_data(self) -> list[Rscord]:  #复写
        f = open(self.path,'r',encoding='UTF-8')
        json_list:list[Rscord] = []
        for line in f.readlines():#把数据读出来
            data_dict:dict = json.loads(line)  #把json数据转为python数据
            rscord = Rscord(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            json_list.append(rscord)
        f.close()
        return json_list
if __name__ == '__main__':
    json_test =Json_Read_Data("D:/二月.txt")
    data_dict = json_test.read_data()
    print(data_dict)












