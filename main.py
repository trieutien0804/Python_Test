class Bai1:
    def InHCN(self,n):
        print("hinh chu nhat theo vong lap for")
        for i in range(0,n):
            print("*"*5)

        print("Hinh chu nhat theo vong lap while")
        i =0
        while i < n:
            print("*"*5)
            i = i+1
    def InTG(self,n):
        print("hinh tam giac vuong theo vong lap for")
        for i in range(1,n+1):
            print("*"*i)

        print("hinh tam giac vuong nguoc theo vong lap for")
        for i in range(1,n+1):
            print(" " * (n-i) + "*"*i)

        print("hinh tam giac can theo vong lap for")
        for i in range(1,n+1):
            print(" " * (n-i) + "*" * ((2*i)-1))

        print("hinh tam giac deu theo tam giac can theo vong lap for")
        for i in range(1,int((n+1)/2)+1):
            print(" " * (n-i) + "*" * ((2*i)-1))

        print("hinh tam giac deu theo vong lap for")
        for i in range(1, n + 1):
            nSpace = n-i
            nStar = n - nSpace
            if (nSpace%2 == 0):
                print(round(nSpace/2)* " " + nStar * "*" + round(nSpace/2)* " ")
    def InTheoDinhDang(self,n):
        print("hinh chu nhat theo vong lap for")
        for i in range(0, n):
            print("*" * 5)

        print("hinh tam giac vuong theo vong lap for")
        for i in range(1, n + 1):
            print(("*" * i).ljust(n))

        print("hinh tam giac vuong nguoc theo vong lap for")
        for i in range(1, n + 1):
            print(("*" * i).rjust(n))

        print("hinh tam giac can theo vong lap for")
        for i in range(1, n + 1):
            if i%2!=0:
                print(("*" * i).center(n))

class Bai2:
    def IntArr(self):
        n =int (input("Nhap so phan tu cua mang: "))
        a = []
        for i in range(n):
            a.append(int(input("Nhap vao phan tu thu %d: "%(i+1))))
        return a
    def FindMaxMin(self,a,n):
        highest = max(a)
        lowest = min(a)
        if highest < 0:
            print("So duong lon nhat la:  " )
        else:
            print("So duong lon nhta la: ", highest)
        if lowest>0:
            print("So am lon nhat la: ")
        else:
            print("So am nho nhat la: ",lowest)

class Bai3:
    dict={'developer': 'lap trinh vien', 'tester': 'kiem thu vien', 'project Manager': 'nha quan ly du an'}
    def Add(self,key,value):
        if(key not in self.dict.keys()):
            self.dict[key] = value
    def AllItems(self):
        return self.dict.items()
    def Search(self,keyword):
        temp = ""
        for key in self.dict.keys():
            if(key == keyword):
                print(keyword + ": " + self.dict[keyword])
                temp = self.dict[keyword]
                return
            if temp == "" :
                print("Khong tim thay")

    def DeleteItem(self,keyword):
        if(keyword in self.dict.keys()):
            del self.dict[keyword]
            print("Xoa thanh cong")
            return
        else:
            print("Xoa khong thanh cong")
            return

class Bai4:
    allEmployee = [{"ma_nv": "1","ten nv": "Nguyen Van A" },
                   {"ma_nv": "2", "ten nv": "Duong Trong C",
                    "ma_nv": "3", "ten nv": "Nguyen Thanh N"}]
    n = len(allEmployee)
    def GetEmp(self):
        for i in range(0,self.n):
            print("Ma nhan vien: {0} ".format(self.allEmployee[i]["ma_nv"]))
            print("Ten nhan vien: {0} ".format(self.allEmployee[i]["ten nv"]))
    def FindEmp(self,name):
        for i in range(0,self.n):
            if(self.allEmployee[i]["ten nv"].find(name) != -1):
                print("Ma nhan vien: {0} ".format(self.allEmployee[i]["ma_nv"]))
                print("Ten nhan vien: {0} ".format(self.allEmployee[i]["ten nv"]))

    def AddEmp(self):
        print("Nhap ma nhan vien: ")
        id = str(input())
        for i in range(0,self.n):
            if(self.allEmployee[i]["ma_nv"] == id):
                print("Ma nhan vien da ton tai!")
                return -1

        print("Nhap ten nhan vien: ")
        name = str(input())
        newemp = {"ma_nv": id, "ten nv": name}
        self.allEmployee.append(newemp)
        self.n = len(self.allEmployee)
        self.GetEmp()

    def DeleteEmp(self,id):
        for i in range(0,self.n):
            if(self.allEmployee[i]["ma_nv"] == str(id)):
                del self.allEmployee[i]
                self.n = len(self.allEmployee)
                print(self.n)
                self.GetEmp()
                return
#n = int(input("Nhap gia tri n: "))
#test1 = Bai1()
#test1.InTheoDinhDang(n)
#test2 = Bai2()
#a= test2.IntArr()
#print(a)
#test2.FindMaxMin(a,len(a))
#test1.InHCN(n)
#test1.InTG(n)
#test3 = Bai3()
#test3.Add("IT", "ABC")
#print(test3.AllItems())
#print(len(test3.dict))
#test3.Search("tester")
#test3.DeleteItem("IT")
#print(test3.dict.items())
test4 = Bai4()
test4.GetEmp()
test4.FindEmp("Van")
test4.AddEmp()
test4.DeleteEmp("2")
