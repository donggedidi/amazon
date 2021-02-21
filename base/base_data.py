class BaseData:

    def get_data_file(self,filename):
        path="./data/{}".format(filename)
        with open(path,"r",encoding="utf-8") as f:
            return f.readlines()

    def read_data(self,filename):
        arrs = []
        for data in self.get_data_file(filename):
            arrs.append(tuple(data.strip().split(",")))
        return arrs[1::]

if __name__ == '__main__':
    print(BaseData().read_data("../data/login.yaml"))
    # print(GetData().read_data("cart.txt"))