operation_num=0
round_num=0
import time
from unicodedata import name

print("\n\n--------------------Copyright @Clapping Technology Co., Ltd || Clapping Studio All Rights Reserved--------------------\n\n\n")
print("欢迎使用化学终端v0.1，本应用为纯Python开发，访问官网https://Jefferyz070607以查看详情\n\n\n")
class inorganic_substance():
    def __init__(self):
        self.f_e=0
        self.f_n=0
        self.s_e=0
        self.s_n=0
        self.t_e=0
        self.t_n=0
        self.ff_e=0
        self.ff_n=0
        self.name="error"
    def build(self):
        print("\n\n运算中……\n\n")
        time.sleep(2)
        print("f_e:",self.f_e," f_n:",self.f_n," s_e:",self.s_e," s_n:",self.s_n," t_e:",self.t_e," t_n:",self.t_n," ff_e:",self.ff_e," ff_n:",self.ff_n)
        print("\n\n运算完成\n\n\n")
        #氧和氢
        if self.f_e==1 and self.f_n==2 and self.s_e==8 and self.s_n==1:
            self.name="水"
        elif self.f_e==1 and self.f_n==2 and self.s_e==8 and self.s_n==2:
            self.name="过氧化氢"
        elif self.f_e==1 and self.f_n==2 and self.s_e==0 and self.s_n==0:
            self.name="氢气"
        elif self.f_e==8 and self.f_n==2 and self.s_e==0 and self.s_n==0:
            self.name="氧气"
        elif self.f_e==8 and self.f_n==3 and self.s_e==0 and self.s_n==0:
            self.name="臭氧"
        #硫
        elif self.f_e==16 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="硫单质"
        elif self.f_e==16 and self.f_n==1 and self.s_e==8 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="二氧化硫"
        elif self.f_e==16 and self.f_n==1 and self.s_e==8 and self.s_n==3 and self.t_e==0 and self.t_n==0:
            self.name="三氧化硫"
        elif self.f_e==1 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="硫酸"
        elif self.f_e==1 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="亚硫酸"
        elif self.f_e==1 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="硫化氢"
        elif self.f_e==29 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="硫化铜"
        #碳
        elif self.f_e==6 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="碳单质"
        elif self.f_e==6 and self.f_n==1 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="一氧化碳"
        elif self.f_e==6 and self.f_n==1 and self.s_e==8 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="二氧化碳"
        elif self.f_e==1 and self.f_n==2 and self.s_e==6 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="碳酸"
        #铁
        elif self.f_e==26 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="铁单质"
        elif self.f_e==26 and self.f_n==2 and self.s_e==8 and self.s_n==3 and self.t_e==0 and self.t_n==0:
            self.name="氧化铁"
        elif self.f_e==26 and self.f_n==3 and self.s_e==8 and self.s_n==4 and self.t_e==0 and self.t_n==0:
            self.name="四氧化三铁"
        elif self.f_e==26 and self.f_n==1 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氧化亚铁"
        elif self.f_e==26 and self.f_n==1 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="硫酸亚铁"
        elif self.f_e==26 and self.f_n==2 and self.s_e==16 and self.s_n==3 and self.t_e==8 and self.t_n==12:
            self.name="硫酸铁"
        elif self.f_e==26 and self.f_n==1 and self.s_e==17 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="氯化亚铁"
        elif self.f_e==26 and self.f_n==1 and self.s_e==17 and self.s_n==3 and self.t_e==0 and self.t_n==0:
            self.name="氯化铁"
        elif self.f_e==26 and self.f_n==1 and self.s_e==8 and self.s_n==2 and self.t_e==1 and self.t_n==2:
            self.name="氢氧化亚铁"
        elif self.f_e==26 and self.f_n==1 and self.s_e==8 and self.s_n==3 and self.t_e==1 and self.t_n==3:
            self.name="氢氧化铁"
        #铜
        elif self.f_e==29 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="铜单质"
        elif self.f_e==29 and self.f_n==1 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氧化铜"
        elif self.f_e==29 and self.f_n==2 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氧化亚铜"
        elif self.f_e==29 and self.f_n==1 and self.s_e==17 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="氯化铜"
        elif self.f_e==29 and self.f_n==1 and self.s_e==8 and self.s_n==2 and self.t_e==1 and self.t_n==2:
            self.name="氢氧化铜"
        elif self.f_e==29 and self.f_n==1 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="硫酸铜"
        #氯
        elif self.f_e==17 and self.f_n==2 and self.s_e==0 and self.s_n==0:
            self.name="氯气"
        elif self.f_e==1 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="盐酸"
        elif self.f_e==1 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==1:
            self.name="次氯酸"
        elif self.f_e==1 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==2:
            self.name="亚氯酸"
        elif self.f_e==1 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="正氯酸"
        elif self.f_e==1 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="高氯酸"
        elif self.f_e==17 and self.f_n==2 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="一氧化二氯"
        elif self.f_e==17 and self.f_n==1 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="一氧化氯"
        elif self.f_e==17 and self.f_n==2 and self.s_e==8 and self.s_n==3 and self.t_e==0 and self.t_n==0:
            self.name="三氧化二氯"
        elif self.f_e==17 and self.f_n==2 and self.s_e==8 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="二氧化氯"
        elif self.f_e==17 and self.f_n==2 and self.s_e==8 and self.s_n==5 and self.t_e==0 and self.t_n==0:
            self.name="五氧化二氯(暂未被合成)"
        elif self.f_e==17 and self.f_n==2 and self.s_e==8 and self.s_n==6 and self.t_e==0 and self.t_n==0:
            self.name="六氧化二氯"
        elif self.f_e==17 and self.f_n==1 and self.s_e==8 and self.s_n==7 and self.t_e==0 and self.t_n==0:
            self.name="七氧化二氯"
        #钠
        elif self.f_e==11 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="钠单质"
        elif self.f_e==11 and self.f_n==1 and self.s_e==1 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氢化钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==16 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="硫化钠"
        elif self.f_e==11 and self.f_n==2 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氧化钠"
        elif self.f_e==11 and self.f_n==2 and self.s_e==8 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="过氧化钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==8 and self.s_n==1 and self.t_e==1 and self.t_n==1:
            self.name="氢氧化钠"
        elif self.f_e==11 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="硫酸钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==1 and self.s_n==1 and self.t_e==16 and self.t_n==1 and self.ff_e==8 and self.ff_n==4:
            self.name="硫酸氢钠"
        elif self.f_e==11 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="亚硫酸钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==1 and self.s_n==1 and self.t_e==16 and self.t_n==1 and self.ff_e==8 and self.ff_n==3:
            self.name="亚硫酸氢钠"
        elif self.f_e==11 and self.f_n==2 and self.s_e==16 and self.s_n==2 and self.t_e==8 and self.t_n==5 and self.ff_e==0 and self.ff_n==0:
            self.name="亚硫酸氢钠"
        elif self.f_e==11 and self.f_n==2 and self.s_e==6 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="碳酸钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==1 and self.s_n==1 and self.t_e==6 and self.t_n==1 and self.ff_e==8 and self.ff_n==3:
            self.name="碳酸氢钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氯化钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==1:
            self.name="次氯酸钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==2:
            self.name="亚氯酸钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="氯酸钠"
        elif self.f_e==11 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="高氯酸钠"
        #钙
        elif self.f_e==20 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="钙单质"
        elif self.f_e==20 and self.f_n==1 and self.s_e==1 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="氢化钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==16 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="硫化钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==8 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氧化钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==8 and self.s_n==2 and self.t_e==0 and self.t_n==0:
            self.name="过氧化钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==8 and self.s_n==2 and self.t_e==1 and self.t_n==2:
            self.name="氢氧化钙"
        elif self.f_e==20 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==4:
            self.name="硫酸钙"
        elif self.f_e==20 and self.f_n==2 and self.s_e==16 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="亚硫酸钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==1 and self.s_n==2 and self.t_e==16 and self.t_n==2 and self.ff_e==8 and self.ff_n==8:
            self.name="硫酸氢钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==1 and self.s_n==2 and self.t_e==16 and self.t_n==2 and self.ff_e==8 and self.ff_n==6:
            self.name="亚硫酸氢钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==6 and self.s_n==1 and self.t_e==8 and self.t_n==3:
            self.name="碳酸钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==1 and self.s_n==2 and self.t_e==6 and self.t_n==2 and self.ff_e==8 and self.ff_n==6:
            self.name="碳酸氢钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==17 and self.s_n==1 and self.t_e==0 and self.t_n==0:
            self.name="氯化钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==17 and self.s_n==2 and self.t_e==8 and self.t_n==2:
            self.name="次氯酸钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==17 and self.s_n==2 and self.t_e==8 and self.t_n==4:
            self.name="亚氯酸钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==17 and self.s_n==2 and self.t_e==8 and self.t_n==6:
            self.name="氯酸钙"
        elif self.f_e==20 and self.f_n==1 and self.s_e==17 and self.s_n==2 and self.t_e==8 and self.t_n==8:
            self.name="高氯酸钙"
        #稀有气体
        elif self.f_e==2 and self.f_n==1 and self.s_e==0 and self.s_n==0:
            self.name="氦气"
        else:
            print("fatal error!!! No such inorganic substance")
    def call(self):
        print(self.name)
        print("\n\n\n")
        print("结果为:",self.name)
        print("\n\n\n")
def element_print():
    print("H(1)                                                     He(2)\n")
    print("Li(3) Be                               B  C(6)  N  O(8)  F  Ne\n")
    print("Na(11) Mg                            Al Si P  S(16)  Cl(17) Ar\n")
    print("K Ca(20) Sc Ti V Cr Mn Fe(26) Co Ni Cu(29) Zn Ga Ge As Se Br Kr\n")
    print("Rb Sr Y  Zr  Nb  Mo  Tc Ru   Rh  Pd  Ag  Cd In Sn Sb  Te I  Xe\n")
    print("Cs Ba    Hf Ta  W   Re  Os  Ir  Put  Au  Hg Tl  Pb Bi Po At Rn\n")
    print("Fr Ra    Lf Db  Sg  Bh  Hs  Mt  Ds Rg   Cn  Nh Fl  Mc Lv Ts Og\n")
    print("La ~ Lu  La Ce  Pr  Nd  Pm Sm  Eu Gd  Td  Dy  Ho  Er Tm  Yb Lu\n")
    print("Ac ~ Lr  Ac Th Pa U  Np Pu (括号内有数字的元素可用)\n\n\n")
    print("酸根(算作一种元素):OH(8.1)  SO₄(16.8)  SO₃(16.8.0)  CO₃(6.8) HCO₃(1.6.8) HSO₄(1.16.8) HSO₃(1.16.8.0) ClO(17.8.0.1) ClO₂(17.8.0.2) ClO₃(17.8.0.3) ClO₄(17.8.0.4)")
def element_choic():
    global element_choice
    element_print()
    print("开始组成化学物质\n\n")
    print("请输入您想选择的元素旁边括号的数字，若元素旁边没有括号，则该元素暂未开放\n\n")
    print("输入元素的顺序必须按官网文档的格式(a化b，a前b后；酸按氢，酸根；碱按金属离子，氢氧根；盐按金属离子，酸根进行排列)\n\n")
    strr="请选择您想组成的化学物质的第"+str(round_num+1)+"种元素:"
    element_choice=input(strr)
    element_available_list=["1","1.6.8","1.16.8","1.16.8.0","2","3","6","6.8","8","8.1","11","16","16.8","16.8.0","17","17.8.0.1","17.8.0.2","17.8.0.3","17.8.0.4","20","26","29"]
    while(element_choice not in element_available_list):
        print("您的输入有误，请重新输入")
        element_choice=input("请输入您想选择的元素的序号:")
def element_judge():
    global element
    print("\n")
    if element_choice=="1":
        print("您选择的元素为氢(H)")
        element="H"
        print("\n")
    if element_choice=="1.6.8":
        print("您选择的元素为碳酸氢根(HCO₃)")
        element="HCO₃"
        print("\n")
    if element_choice=="1.16.8":
        print("您选择的元素为硫酸氢根(HSO₃)")
        element="HSO₄"
        print("\n")
    if element_choice=="1.16.8.0":
        print("您选择的元素为亚硫酸氢根(HSO₃)")
        element="HSO₃"
        print("\n")
    if element_choice=="6":
        print("您选择的元素为碳(C)")
        element="C"
        print("\n")
    if element_choice=="6.8":
        print("您选择的元素为碳酸根(CO₃)")
        element="CO₃"
        print("\n")
    if element_choice=="8":
        print("您选择的元素为氧(O)")
        element="O"
        print("\n")
    if element_choice=="8.1":
        print("您选择的元素为氢氧根(OH)")
        element="OH"
        print("\n")
    if element_choice=="11":
        print("您选择的元素为钠(Na)")
        element="Na"
        print("\n")
    if element_choice=="16":
        print("您选择的元素为硫(S)")
        element="S"
        print("\n")
    if element_choice=="16.8":
        print("您选择的元素为硫酸根(SO₄)")
        element="SO₄"
        print("\n")
    if element_choice=="16.8.0":
        print("您选择的元素为亚硫酸根(SO₃)")
        element="SO₃"
        print("\n")
    if element_choice=="17":
        print("您选择的元素为氯(Cl)")
        element="Cl"
        print("\n")
    if element_choice=="17.8.0.1":
        print("您选择的元素为次氯酸根(ClO)")
        element="ClO"
        print("\n")
    if element_choice=="17.8.0.2":
        print("您选择的元素为亚氯酸根(ClO₂)")
        element="ClO₂"
        print("\n")
    if element_choice=="17.8.0.3":
        print("您选择的元素为氯酸根(ClO₃)")
        element="ClO₃"
        print("\n")
    if element_choice=="17.8.0.4":
        print("您选择的元素为高氯酸根(ClO₄)")
        element="ClO₄"
        print("\n")
    if element_choice=="20":
        print("您选择的元素为钙(Ca)")
        element="Ca"
        print("\n")
    if element_choice=="26":
        print("您选择的元素为铁(Fe)")
        element="Fe"
        print("\n")
    if element_choice=="29":
        print("您选择的元素为铜(Cu)")
        element="Cu"
        print("\n")
def inorganic_substance_build():
    global round_num
    global operation_num
    global i_s
    global element
    while (operation_num>0):
        if round_num==1:
            print("\n\n")
            print("请选择该化合物的第2种元素")
            time.sleep(2)
            element_choic()
            element_judge()
            print("\n")
            strr="请输入该无机物的"+element+"原子数量:"
            atom_num=input(strr)
            print("\n")
            available_list=[]
            for i in range(0,1000):
                available_list.append(str(i))
            while atom_num not in available_list:
                print("您的输入有误，请重新输入")
                strr="请输入该无机物的"+element+"原子数量:"
                atom_num=input(strr)
                print("\n")
            if element_choice=="16.8":
                i_s.s_e=16
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=4*(int(atom_num))
            elif element_choice=="8.1":
                i_s.s_e=8
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=1
                i_s.t_n=1*(int(atom_num))
            elif element_choice=="6.8":
                i_s.s_e=6
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=3*(int(atom_num))
            elif element_choice=="16.8.0":
                i_s.s_e=16
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=3*(int(atom_num))
            elif element_choice=="1.6.8":
                i_s.s_e=1
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=6
                i_s.t_n=1*(int(atom_num))
                i_s.ff_e=8
                i_s.ff_n=3*(int(atom_num))
            elif element_choice=="1.16.8":
                i_s.s_e=1
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=16
                i_s.t_n=1*(int(atom_num))
                i_s.ff_e=8
                i_s.ff_n=4*(int(atom_num))
            elif element_choice=="1.16.8.0":
                i_s.s_e=1
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=16
                i_s.t_n=1*(int(atom_num))
                i_s.ff_e=8
                i_s.ff_n=3*(int(atom_num))
            elif element_choice=="17.8.0.1":
                i_s.s_e=17
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=1*(int(atom_num))
            elif element_choice=="17.8.0.2":
                i_s.s_e=17
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=2*(int(atom_num))
            elif element_choice=="17.8.0.3":
                i_s.s_e=17
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=3*(int(atom_num))
            elif element_choice=="17.8.0.4":
                i_s.s_e=17
                i_s.s_n=1*(int(atom_num))
                i_s.t_e=8
                i_s.t_n=4*(int(atom_num))
            else:
                i_s.s_e=int(element_choice)
                i_s.s_n=int(atom_num)
            operation_num-=1
            round_num+=1
            if operation_num==0:
                break
        if round_num==2:
            print("\n\n")
            print("请选择该化合物的第3种元素")
            time.sleep(2)
            element_choic()
            element_judge()
            strr="请输入该无机物的 "+element+" 原子数量:"
            atom_num=input(strr)
            print("\n")
            available_list=[]
            for i in range(0,1000):
                available_list.append(str(i))
            while atom_num not in available_list:
                print("您的输入有误，请重新输入")
                strr="请输入该无机物的 "+element+" 原子数量:"
                atom_num=input(strr)
                print("\n")
            i_s.t_e=int(element_choice)
            i_s.t_n=int(atom_num)
            operation_num-=1
            round_num+=1
    round_num=0
def inorganic_substance_build2():
    global round_num
    global operation_num
    global i_s2
    while (operation_num>0):
        if round_num==1:
            print("\n\n")
            print("请选择该化合物的第2种元素")
            time.sleep(3)
            element_choic()
            element_judge()
            print("\n\n")
            strr="请输入该无机物的 "+element+" 原子数量:"
            atom_num=input(strr)
            print("\n")
            available_list=[]
            for i in range(0,1000):
                available_list.append(str(i))
            while atom_num not in available_list:
                print("您的输入有误，请重新输入")
                strr="请输入该无机物的 "+element+" 原子数量:"
                atom_num=input(strr)
                print("\n")
            if element_choice=="16.8":
                i_s2.s_e=16
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=4*(int(atom_num))
            elif element_choice=="8.1":
                i_s2.s_e=8
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=1
                i_s2.t_n=1*(int(atom_num))
            elif element_choice=="6.8":
                i_s2.s_e=6
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=3*(int(atom_num))
            elif element_choice=="16.8.0":
                i_s2.s_e=16
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=3*(int(atom_num))
            elif element_choice=="1.6.8":
                i_s2.s_e=1
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=6
                i_s2.t_n=1*(int(atom_num))
                i_s2.ff_e=8
                i_s2.ff_n=3*(int(atom_num))
            elif element_choice=="1.16.8":
                i_s2.s_e=1
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=16
                i_s2.t_n=1*(int(atom_num))
                i_s2.ff_e=8
                i_s2.ff_n=4*(int(atom_num))
            elif element_choice=="1.16.8.0":
                i_s2.s_e=1
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=16
                i_s2.t_n=1*(int(atom_num))
                i_s2.ff_e=8
                i_s2.ff_n=3*(int(atom_num))
            elif element_choice=="17.8.0.1":
                i_s2.s_e=17
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=1*(int(atom_num))
            elif element_choice=="17.8.0.2":
                i_s2.s_e=17
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=2*(int(atom_num))
            elif element_choice=="17.8.0.3":
                i_s2.s_e=17
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=3*(int(atom_num))
            elif element_choice=="17.8.0.4":
                i_s2.s_e=17
                i_s2.s_n=1*(int(atom_num))
                i_s2.t_e=8
                i_s2.t_n=4*(int(atom_num))
            else:
                i_s2.s_e=int(element_choice)
                i_s2.s_n=int(atom_num)
            operation_num-=1
            round_num+=1
            if operation_num==0:
                i_s2.build()
                i_s2.call()
                print("\n\n")
                if i_s.name=="硫酸" or i_s2.name=="硫酸":
                    choice=input("请选择硫酸的浓度(输入1或2指定浓或稀，输入其他内容将显示所有相关反应) 1.稀 2.浓:")
                    if choice=="1":
                        process(i_s.name,i_s2.name,0,1)
                    elif choice=="2":
                        process(i_s.name,i_s2.name,0,2)
                    else:
                        process(i_s.name,i_s2.name,0,0)
                process(i_s.name,i_s2.name)
                break
        if round_num==2:
            print("\n\n")
            print("请选择该化合物的第3种元素")
            time.sleep(3)
            element_choic()
            element_judge()
            strr="请输入该无机物的 "+element+" 原子数量:"
            atom_num=input(strr)
            print("\n")
            available_list=[]
            for i in range(0,1000):
                available_list.append(str(i))
            while atom_num not in available_list:
                print("您的输入有误，请重新输入")
                strr="请输入该无机物的 "+element+" 原子数量:"
                atom_num=input(strr)
                print("\n")
            i_s2.t_e=int(element_choice)
            i_s2.t_n=int(atom_num)
            operation_num-=1
            round_num+=1
            if operation_num==0:
                i_s2.build()
                i_s2.call()
                if i_s.name=="硫酸" or i_s2.name=="硫酸":
                    choice=input("请选择硫酸的浓度(输入1或2指定浓或稀，输入其他内容将显示所有相关反应) 1.稀 2.浓:")
                    if choice=="1":
                        process(i_s.name,i_s2.name,0,1)
                    elif choice=="2":
                        process(i_s.name,i_s2.name,0,2)
                    else:
                        process(i_s.name,i_s2.name,0,0)
            else:
                inorganic_substance_build2()
def operation():
    global operation_num
    global round_num
    global i_s
    global i_s2
    global element
    operation_num=0
    if operation_num==0:
        print("\n\n元素数量为您想组成的化合物或单质所含元素种类的多少，酸根算作一种元素!!!输入必须正确否则将无法判断物质!!!!")
        print("\n如水(H₂O)的元素种类数量为2(H和O元素)硫酸(H₂SO₄)或氢氧化铁(Fe(OH)₃)的元素种类数量为2，因为酸根算作一种元素!!!\n\n")
        element_num=input("请输入组成该无机物的元素数量:")
        print("\n")
        if element_num!="1" and element_num!="2" and element_num!="3":
            print("您的输入有误，请重新输入")
            element_num=input("请输入组成该无机物的元素数量:")
            print("\n")
        operation_num=int(element_num)
    strr="请输入该无机物的 "+element+" 原子数量:"
    atom_num=input(strr)
    print("\n")
    available_list=[]
    for i in range(0,1000):
        available_list.append(str(i))
    while atom_num not in available_list:
        print("您的输入有误，请重新输入")
        strr="请输入该无机物的 "+element+" 原子数量:"
        atom_num=input(strr)
        print("\n")
    i_s=inorganic_substance()
    i_s.f_e=int(element_choice)
    i_s.f_n=int(atom_num)
    operation_num-=1
    round_num+=1
    if operation_num>0:
        inorganic_substance_build()
    if operation_num==0:
        i_s.build()
        i_s.call()
        operation=input("请输入您想对此化合物的操作 1.查询 2.多物质反应 3.单物质反应:")
        while (operation!="1" and operation!="2" and operation!="3"):
            print("error:Unknown Command!")
            operation=input("请输入您想对此化合物的操作 1.查询 2.多物质反应 3.单物质反应:")
        if operation=="3":
            process(i_s.name,"none")
        if operation=="2":
            round_num=0
            print("\n\n")
            print("请输入第二种化合物的第1种元素")
            time.sleep(3)
            element_choic()
            element_judge()
            print("\n\n元素数量为您想组成的化合物或单质所含元素种类的多少，酸根算作一种元素!!!输入必须正确否则将无法判断物质!!!!")
            print("\n如水(H₂O)的元素种类数量为2(H和O元素)硫酸(H₂SO₄)或氢氧化铁(Fe(OH)₃)的元素种类数量为2，因为酸根算作一种元素!!!\n\n")
            element_num=input("请输入组成该无机物的元素种类数量:")
            print("\n")
            if element_num!="1" and element_num!="2" and element_num!="3":
                print("您的输入有误，请重新输入")
                element_num=input("请输入组成该无机物的元素数量:")
                print("\n")
            operation_num=int(element_num)
            strr="请输入该无机物的 "+element+" 原子数量:"
            atom_num=input(strr)
            print("\n")
            available_list=[]
            for i in range(0,1000):
                available_list.append(str(i))
            while atom_num not in available_list:
                print("您的输入有误，请重新输入")
                strr="请输入该无机物的 "+element+" 原子数量:"
                atom_num=input(strr)
                print("\n")
            i_s2=inorganic_substance()
            i_s2.f_e=int(element_choice)
            i_s2.f_n=int(atom_num)
            operation_num-=1
            round_num+=1
            if operation_num==0:
                i_s2.build()
                i_s2.call()
                print("\n\n")
                if i_s.name=="硫酸" or i_s2.name=="硫酸":
                    choice=input("请选择硫酸的浓度(输入1或2指定浓或稀，输入其他内容将显示所有相关反应) 1.稀 2.浓:")
                if choice=="1":
                    process(i_s.name,i_s2.name,0,1)
                elif choice=="2":
                    process(i_s.name,i_s2.name,0,2)
                else:
                    process(i_s.name,i_s2.name,0,0)
            else:
                inorganic_substance_build2()
def process(name1,name2,name3=0,name4=0):
    print("\n\n\n–––––––––––反应器––––––––\n\n\n")
    print("参加反应物质:",name1,",",name2,"\n\n\n")
    print("反应器开始运作\n\n\n")
    print("正在准备反应物质\n\n")
    time.sleep(0.5)
    print("反应物质准备完毕\n\n")
    time.sleep(0.5)
    print("开始搭建反应仪器\n\n")
    time.sleep(0.5)
    print("搭建中……\n\n")
    time.sleep(0.5)
    print("搭建完毕\n\n")
    time.sleep(0.25)
    print("开始反应\n\n")
    time.sleep(1)
    print("反应中…\n\n")
    time.sleep(1)
    print("反应中……\n\n")
    time.sleep(1)
    print("反应中………\n\n")
    time.sleep(1)
    print("反应完毕\n\n\n")
    print("反应结果:\n\n")
    name_list=[name1,name2]
    if "铜单质" in name_list and "硫单质" in name_list and name3==0:
        print("      高温")
        print("2Cu+S======Cu₂S")
    #分解反应
    if "过氧化氢" in name_list and name2=="none":
        print("     MnO₂")
        print("2H₂O₂======2H₂O+O₂↑")
    elif "硫酸铜" in name_list and name2=="none":
        print("       Δ")
        print("CuSO₄======CuO+SO₃")
    elif "氢氧化铜" in name_list and name2=="none":
        print("         Δ")
        print("Cu(OH)₂======CuO+H₂O")
    elif "碳酸" in name_list and name2=="none":
        print("       Δ")
        print("H₂CO₃======H₂O+CO₂↑")
    elif "次氯酸" in name_list and name2=="none":
        print("      光照")
        print("2HClO======2HCl+O₂↑")
    elif "臭氧" in name_list and name2=="none":
        print("  氟氯代烃")
        print("2O₃======3O₂")
    elif "氢氧化铁" in name_list and name2=="none":
        print("          Δ")
        print("2Fe(OH)₃======Fe₂O₃+3H₂O")
    elif "碳酸氢钠" in name_list and name2=="none":
        print("         Δ")
        print("2NaHCO₃======Na₂CO₃+H₂O+CO₂↑")
    elif "次氯酸" in name_list and name2=="none":
        print("      光照")
        print("2HClO======2HCl+O₂↑")
    elif "碳酸钙" in name_list and name2=="none":
        print("      高温")
        print("CaCO₃======CaO+CO₂↑")
    elif "碳酸氢钙" in name_list and name2=="none":
        print("           Δ")
        print("Ca(HCO₃)₂======CaCO₃↓+H₂O+CO₂↑")
    #单质和酸反应
    #铁
    elif "铁单质" in name_list and "硫酸" in name_list and name3==0 and name4==0:
        print("Fe+H₂SO₄(稀)=====FeSO₄+H₂↑")
        print("3Fe+4H₂SO₄(浓)=====Fe₃O₄+4SO₂↑")
        print("               Δ")
        print("2Fe+6H₂SO₄(浓)======Fe₂(SO₄)₃+3SO₂↑+6H₂O")
    elif "铁单质" in name_list and "硫酸" in name_list and name3==0 and name4==1:
        print("Fe+H₂SO₄(稀)=====FeSO₄+H₂↑")
    elif "铁单质" in name_list and "硫酸" in name_list and name3==0 and name4==2:
        print("3Fe+4H₂SO₄(浓)=====Fe₃O₄+4SO₂↑")
        print("            Δ")
        print("2Fe+6H₂SO₄======Fe₂(SO₄)₃+3SO₂↑+6H₂O")
    elif "铁单质" in name_list and "盐酸" in name_list and name3==0:
        print("Fe+2HCl=====FeCl₂+H₂↑")
    #铜
    elif "铜单质" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name4==2):
        print("               Δ")
        print("Cu+2H₂SO₄(浓)======CuSO₄+SO₂↑+2H₂O")
    #碳
    elif "碳单质" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name4==2):
        print("             Δ")
        print("C+2H₂SO₄(浓)======CO₂↑+2H₂O+2SO₂↑")
    #硫
    elif "硫单质" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name4==2):
        print("             Δ")
        print("S+2H₂SO₄(浓)======3SO₂↑+2H₂O")
    #钠
    #!反应去除
    # elif "钠单质" in name_list and "硫酸" in name_list and name3==0 and name4==1:
    #     print("2Na+H₂SO₄(稀)======Na₂SO₄+H₂↑")
    # elif "钠单质" in name_list and "硫酸" in name_list and name3==0 and name4==2:
    #     print("2Na+2H₂SO₄(浓)======Na₂SO₄+SO₂↑+2H₂O")
    # elif "钠单质" in name_list and "硫酸" in name_list and name3==0 and name4==0:
    #     print("2Na+H₂SO₄(稀)======Na₂SO₄+H₂↑")
    #     print("2Na+2H₂SO₄(浓)======Na₂SO₄+SO₂↑+2H₂O")
    elif "钠单质" in name_list and "硫酸" in name_list and name3==0:
        print("2Na+H₂SO₄======Na₂SO₄+H₂↑")
    elif "钠单质" in name_list and "盐酸" in name_list and name3==0:
        print("2Na+2HCl=====2NaCl+H₂↑")
    #钙
    elif "钙单质" in name_list and "硫酸" in name_list and name3==0:
        print("Ca+H₂SO₄======CaSO₄+H₂↑")
    elif "钙单质" in name_list and "盐酸" in name_list and name3==0:
        print("Ca+2HCl=====CaCl₂+H₂↑")
    #单质和化合物置换反应
    elif "铁" in name_list and "硫酸铜" in name_list and name3==0:
        print("Fe+CuSO₄======FeSO₄+Cu")
    elif "铁" in name_list and "氯化铜" in name_list and name3==0:
        print("Fe+CuCl₂======FeCl₂+Cu")
    #氧化反应
    #单质
    elif "氧气" in name_list and "氢气" in name_list and name3==0:
        print("      点燃     ")
        print("2H₂+O₂======2H₂O")
    elif "铜单质" in name_list and "氧气" in name_list and name3==0:
        print("        Δ")
        print("2Cu+O₂======2CuO")
    elif "铁单质" in name_list and "氧气" in name_list and name3==0:
        print("        点燃")
        print("3Fe+2O₂======Fe₃O₄")
        print("         Δ")
        print("4Fe+3O₂======2Fe₂O₃")
    elif "碳单质" in name_list and "氧气" in name_list and name3==0:
        print("     点燃")
        print("C+O₂======CO₂")
        print("       Δ")
        print("2C+O₂======2CO")
    elif "硫单质" in name_list and "氧气" in name_list and name3==0:
        print("      Δ    ")
        print("S+O₂======SO₂")
    elif "钠单质" in name_list and "氧气" in name_list and name3==0:
        print("4Na+O₂======2Na₂O")
        print("        Δ    ")
        print("2Na+O₂======Na₂O₂")
    elif "钙单质" in name_list and "氧气" in name_list and name3==0:
        print("2Ca+O₂======2CaO")
        print("       Δ    ")
        print("Ca+O₂======CaO₂")
    #其他
    elif "氧化亚铁" in name_list and "氧气" in name_list and name3==0:
        print("         Δ")
        print("6FeO+O₂======2Fe₃O₄")
    #氯化反应
    elif "氧气" in name_list and "氯气" in name_list and name3==0:
        print("      点燃     ")
        print("H₂+Cl₂=====2HCl")
        print("      光照     ")
        print("H₂+Cl₂=====2HCl(爆炸)")
    elif "铜单质" in name_list and "氯气" in name_list and name3==0:
        print("        点燃")
        print("Cu+Cl₂======CuCl₂")
    elif "铁单质" in name_list and "氯气" in name_list and name3==0:
        print("         点燃")
        print("2Fe+3Cl₂======2FeCl₃")
    elif "钠单质" in name_list and "氯气" in name_list and name3==0:
        print("2Na+Cl₂======2NaCl")
    elif "钙单质" in name_list and "氯气" in name_list and name3==0:
        print("Ca+Cl₂======CaCl₂")
    #酸碱中和反应
    #铁
    elif "氢氧化铁" in name_list and "硫酸" in name_list and name3==0:
        print("2Fe(OH)₃+3H₂SO₄======Fe₂(SO₄)₃+6H₂O")
    elif "氢氧化铁" in name_list and "盐酸" in name_list and name3==0:
        print("Fe(OH)₃+3HCl======FeCl₃+3H₂O")
    #铜
    elif "氢氧化铜" in name_list and "硫酸" in name_list and name3==0:
        print("Cu(OH)₂+H₂SO₄======CuSO₄+H₂O")
    elif "氢氧化铜" in name_list and "盐酸" in name_list and name3==0:
        print("Cu(OH)₂+2HCl======CuCl₂+2H₂O")
    #钠
    elif "氢氧化钠" in name_list and "硫酸" in name_list and name3==0:
        print("2NaOH+H₂SO₄======Na₂SO₄+2H₂O")
    elif "氢氧化钠" in name_list and "盐酸" in name_list and name3==0:
        print("NaOH+HCl======NaCl+H₂O")
    #钙
    elif "氢氧化钙" in name_list and "硫酸" in name_list and name3==0:
        print("Ca(OH)₂+H₂SO₄======CaSO₄+2H₂O")
    elif "氢氧化钠" in name_list and "盐酸" in name_list and name3==0:
        print("Ca(OH)₂+HCl======CaCl₂+H₂O")
    #碱性氧化物和酸反应
    #铁和酸
    elif "氧化亚铁" in name_list and "硫酸" in name_list and name3==0:
        print("FeO+H₂SO₄======FeSO₄+H₂O")
    elif "氧化铁" in name_list and "硫酸" in name_list and name3==0:
        print("Fe₂O₃+3H₂SO₄======Fe₂(SO₄)₃+3H₂O")
    elif "四氧化三铁" in name_list and "硫酸" in name_list and name3==0:
        print("Fe₃O₄+4H₂SO₄======FeSO₄+Fe₂(SO₄)₃+4H₂O")
    elif "氧化亚铁" in name_list and "盐酸" in name_list and name3==0:
        print("FeO+2HCl======FeCl₂+H₂O")
    elif "氧化铁" in name_list and "盐酸" in name_list and name3==0:
        print("Fe₂O₃+6HCl======2FeCl₃+3H₂O")
    #铜和酸
    elif "氧化铜" in name_list and "硫酸" in name_list and name3==0:
        print("CuO+H₂SO₄======CuSO₄+H₂O")
    elif "氧化铜" in name_list and "盐酸" in name_list and name3==0:
        print("CuO+2HCl======CuCl₂+H₂O")
    #钠和酸
    elif "氧化钠" in name_list and "硫酸" in name_list and name3==0:
        print("Na₂O+H₂SO₄======Na₂SO₄+H₂O")
    elif "氧化钠" in name_list and "盐酸" in name_list and name3==0:
        print("Na₂O+2HCl======2NaCl+H₂O")
    elif "过氧化钠" in name_list and "硫酸" in name_list and name3==0:
        print("2Na₂O₂+2H₂SO₄======2Na₂SO₄+H₂O+O₂↑")
    elif "过氧化钠" in name_list and "盐酸" in name_list and name3==0:
        print("2Na₂O₂+4HCl======4NaCl+2H₂O+O₂↑")
    elif "硫酸氢钠" in name_list and "氢氧化钠" in name_list and name3==0:
        print("NaHSO₄+NaOH======Na₂SO₄+H₂O")
    #钙和酸
    elif "氧化钙" in name_list and "硫酸" in name_list and name3==0:
        print("CaO+H₂SO₄======CaSO₄+H₂O")
    elif "氧化钙" in name_list and "盐酸" in name_list and name3==0:
        print("CaO+2HCl======CaCl₂+H₂O")
    elif "过氧化钙" in name_list and "硫酸" in name_list and name3==0:
        print("2CaO₂+2H₂SO₄======2CaSO₄+2H₂O+O₂↑")
    elif "过氧化钙" in name_list and "盐酸" in name_list and name3==0:
        print("2CaO₂+4HCl======2NaCl+2H₂O+O₂↑")
    #亚硫酸盐和酸反应
    #钠
    elif "亚硫酸钠" in name_list and "硫酸" in name_list and name3==0:
        print("Na₂SO₃+H₂SO₄======Na₂SO₄+H₂O+SO₂↑")
        print("2Na₂SO₃+H₂SO₄======Na₂SO₄+2NaHSO₃")
    elif "亚硫酸钠" in name_list and "盐酸" in name_list and name3==0:
        print("Na₂SO₃+2HCl======2NaCl+H₂O+SO₂↑")
        print("Na₂SO₃+HCl======NaCl+NaHSO₃")
    #钙
    elif "亚硫酸钙" in name_list and "硫酸" in name_list and name3==0:
        print("CaSO₃+H₂SO₄======CaSO₄+H₂O+SO₂↑")
    elif "亚硫酸钠" in name_list and "盐酸" in name_list and name3==0:
        print("CaSO₃+2HCl======CaCl₂+H₂O+SO₂↑")
    #碳酸盐和酸反应
    #铜
    elif "碳酸铜" in name_list and "硫酸" in name_list and name3==0:
        print("CuCO₃+H₂SO₄======CuSO₄+H₂O+CO₂↑")
    elif "碳酸铜" in name_list and "盐酸" in name_list and name3==0:
        print("CuCO₃+2HCl======CuCl₂+H₂O+CO₂↑")
    #钠
    elif "碳酸钠" in name_list and "硫酸" in name_list and name3==0:
        print("Na₂CO₃+H₂SO₄======Na₂SO₄+H₂O+CO₂↑")
    elif "碳酸钠" in name_list and "盐酸" in name_list and name3==0:
        print("Na₂CO₃+2HCl======2NaCl+H₂O+CO₂↑")
    #钙
    elif "碳酸钙" in name_list and "硫酸" in name_list and name3==0:
        print("CaCO₃+H₂SO₄======CaSO₄+H₂O+CO₂↑")
    elif "碳酸钙" in name_list and "盐酸" in name_list and name3==0:
        print("CaCO₃+2HCl======CaCl₂+H₂O+CO₂↑")
    #碳酸氢盐和酸反应
    #钠
    elif "碳酸氢钠" in name_list and "硫酸" in name_list and name3==0:
        print("Ca(HCO₃)₂+H₂SO₄======CaSO₄+2H₂O+2CO₂↑")
    elif "碳酸氢钙" in name_list and "盐酸" in name_list and name3==0:
        print("Ca(HCO₃)₂+2HCl======CaCl₂+2H₂O+2CO₂↑")
    #钙
    elif "碳酸氢钠" in name_list and "硫酸" in name_list and name3==0:
        print("NaHCO₃+H₂SO₄======NaHSO₄+H₂O+CO₂↑")
        print("2NaHCO₃+H₂SO₄======Na₂SO₄+2H₂O+2CO₂↑")
    elif "碳酸氢钠" in name_list and "盐酸" in name_list and name3==0:
        print("NaHCO₃+HCl======2NaCl+H₂O+CO₂↑")
    #盐酸盐和硫酸反应
    elif "氯化铁" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name2==2):
        print("                   Δ")
        print("2FeCl₃+3H₂SO₄(浓)======2Fe₂(SO₄)₃+6HCl↑")
    elif "氯化铜" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name2==2):
        print("                       Δ")
        print("CuCl₂+H₂SO₄(浓)======CuSO₄+2HCl↑")
    elif "氯化钠" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name2==2):
        print("NaCl+H₂SO₄(浓)======NaHSO₄+HCl↑")
        print("                Δ")
        print("NaCl+H₂SO₄(浓)======Na₂SO₄+2HCl↑")
    elif "氯化钙" in name_list and "硫酸" in name_list and name3==0 and (name4==0 or name2==2):
        print("CaCl₂+H₂SO₄(浓)======CaSO₄+2HCl↑")
    #碱和酸性氧化物反应
    #钠
    elif "氢氧化钠" in name_list and "二氧化碳" in name_list and name3==0:
        print("2NaOH+CO₂======Na₂CO₃+H₂O")
        print("NaOH+CO₂======NaHCO₃+H₂O")
    elif "氢氧化钠" in name_list and "二氧化硫" in name_list and name3==0:
        print("2NaOH+SO₂======Na₂SO₃+H₂O")
        print("NaOH+SO₂======Na₂HSO₃")
    #钙
    elif "氢氧化钙" in name_list and "二氧化碳" in name_list and name3==0:
        print("Ca(OH)₂+CO₂======CaCO₃↓+H₂O")
        print("Ca(OH)₂+2CO₂======Ca(HCO₃)₂")
    elif "氢氧化钙" in name_list and "二氧化硫" in name_list and name3==0:
        print("Ca(OH)₂+SO₂======CaSO₃+H₂O")
        print("Ca(OH)₂+2SO₂======Ca(HSO₃)₂")
    #可溶性碱和硫酸盐反应
    #钠
    elif "氢氧化钠" in name_list and "硫酸铁" in name_list and name3==0:
        print("6NaOH+Fe₂(SO₄)₃======2Fe(OH)₃↓+Na₂SO₄")
    elif "氢氧化钠" in name_list and "硫酸亚铁" in name_list and name3==0:
        print("2NaOH+FeSO₄======Fe(OH)₂↓+Na₂SO₄")
    elif "氢氧化钠" in name_list and "硫酸铜" in name_list and name3==0:
        print("2NaOH+CuSO₄======Cu(OH)₂↓+Na₂SO₄")
    #钙
    elif "氢氧化钙" in name_list and "硫酸铁" in name_list and name3==0:
        print("3Ca(OH)₂+Fe₂(SO₄)₃======2Fe(OH)₃↓+3CaSO₄")
    elif "氢氧化钙" in name_list and "硫酸亚铁" in name_list and name3==0:
        print("Ca(OH)₂+FeSO₄======Fe(OH)₂↓+CaSO₄")
    elif "氢氧化钙" in name_list and "硫酸铜" in name_list and name3==0:
        print("Ca(OH)₂+CuSO₄======Cu(OH)₂↓+CaSO₄")
    #可溶性碱和盐酸盐反应
    elif "氢氧化钠" in name_list and "氯化铁" in name_list and name3==0:
        print("3NaOH+FeCl₃======Fe(OH)₃↓+NaCl")
    elif "氢氧化钠" in name_list and "氯化亚铁" in name_list and name3==0:
        print("2NaOH+FeCl₂======Fe(OH)₂↓+2NaCl")
    elif "氢氧化钠" in name_list and "氯化铜" in name_list and name3==0:
        print("2NaOH+CuCl₂======Cu(OH)₂↓+2NaCl")
    #钙
    elif "氢氧化钙" in name_list and "氯化铁" in name_list and name3==0:
        print("3Ca(OH)₂+2FeCl₃======2Fe(OH)₃↓+3CaCl₂")
    elif "氢氧化钙" in name_list and "氯化亚铁" in name_list and name3==0:
        print("Ca(OH)₂+FeCl₂======Fe(OH)₂↓+CaCl₂")
    elif "氢氧化钙" in name_list and "氯化铜" in name_list and name3==0:
        print("Ca(OH)₂+CuCl₂======Cu(OH)₂↓+CaCl₂")
    #盐和盐反应
    elif "氯化钙" in name_list and "碳酸钠" in name_list and name3==0:
        print("CaCl₂+Na₂CO₃======CaCO₃↓+2NaCl")
    #氢气还原反应
    elif "氧化铜" in name_list and "氢气" in name_list and name3==0:
        print("        Δ")
        print("H₂+CuO======Cu+H₂O")
    elif "氧化铁" in name_list and "氢气" in name_list and name3==0:
        print("          高温")
        print("3H₂+Fe₂O₃======2Fe+3H₂O")
    elif "四氧化三铁" in name_list and "氢气" in name_list and name3==0:
        print("           Δ")
        print("4H₂+Fe₃O₄======3Fe+3H₂O")
    #!去除 碱和过氧化氢反应
    # elif "氢氧化钠" in name_list and "过氧化氢" in name_list and name3==0:
    #     print("          高温")
    #     print("NaOH+H₂O₂======Na₂O₂+H₂O")
    # elif "氢氧化钙" in name_list and "过氧化氢" in name_list and name3==0:
    #     print("          高温")
    #     print("Ca(OH)₂+H₂O₂======CaO₂↓+2H₂O")
    #碳单质还原反应
    elif "碳单质" in name_list and "氧化铜" in name_list and name3==0:
        print("       高温")
        print("C+2CuO======2Cu+CO₂↑")
    elif "碳单质" in name_list and "氧化亚铁" in name_list and name3==0:
        print("      高温")
        print("C+FeO======Fe+CO↑")
    elif "碳单质" in name_list and "氧化铁" in name_list and name3==0:
        print("         高温")
        print("3C+2Fe₂O₃======4Fe+3CO₂↑")
    elif "碳单质" in name_list and "二氧化碳" in name_list and name3==0:
        print("       Δ")
        print("C+CO₂======2CO")
    elif "碳单质" in name_list and "过氧化钠" in name_list and name3==0:
        print("       Δ")
        print("C+2Na₂O₂======Na₂CO₃+Na₂O")
    #一氧化碳还原反应
    elif "一碳化碳" in name_list and "氧化铜" in name_list and name3==0:
        print("        Δ")
        print("CO+CuO======Cu+CO₂")
    elif "一氧化碳" in name_list and "氧化亚铁" in name_list and name3==0:
        print("          Δ")
        print("CO+FeO======Fe+CO₂")
    elif "一氧化碳" in name_list and "氧化铁" in name_list and name3==0:
        print("          Δ")
        print("3CO+Fe₂O₃======2Fe+3CO₂")
    elif "一氧化碳" in name_list and "四氧化三铁" in name_list and name3==0:
        print("          Δ")
        print("4CO+Fe₃O₄======3Fe+4CO₂")
    #氧化还原反应
    elif "一氧化碳" in name_list and "氧气" in name_list and name3==0:
        print("       点燃")
        print("2CO+O₂======2CO₂")
    #氯还原反应
    elif "硫化氢" in name_list and "氯气" in name_list and name3==0:
        print("Cl₂+H₂S=====2HCl+S↓")
    #氯化的氧化还原反应
    elif "氯化亚铁" in name_list and "氯气" in name_list and name3==0:
        print("2FeCl₂+Cl₂=====2FeCl₃")
    elif "氢氧亚铁" in name_list and "氯气" in name_list and name3==0:
        print("6Fe(OH)2+3Cl₂======4Fe(OH)₃+2FeCl₃")
    #含氯反应
    elif "氯气" in name_list and "水" in name_list and name3==0:
        print("Cl₂+H₂O=====HCl+HClO(可逆)")
    #亚氢氧化物和过氧化氢反应
    elif "氢氧化亚铁" in name_list and "过氧化氢" in name_list and name3==0:
        print("2Fe(OH)₂+H₂O₂======2Fe(OH)₃")
    #亚氢氧化物和氧气反应
    elif "氢氧化亚铁" in name_list and "氧气" in name_list and name3==0:
        print("4Fe(OH)₂+O₂======2Fe₂O₃+4H₂O")
    #含水反应
    #酸酐和水反应
    elif "二氧化碳" in name_list and "水" in name_list and name3==0:
        print("CO₂+H₂O======H₂CO₃")
    elif "二氧化硫" in name_list and "水" in name_list and name3==0:
        print("SO₂+H₂O======H₂SO₃")
    elif "三氧化硫" in name_list and "水" in name_list and name3==0:
        print("SO₃+H₂O======H₂SO₄")
    #单质和水反应
    elif "钠单质" in name_list and "水" in name_list and name3==0:
        print("2Na+2H₂O======2NaOH+H₂↑")
    elif "铁单质" in name_list and "水" in name_list and name3==0:
        print("              高温")
        print("3Fe+4H₂O(气态)======Fe₃O₄+4H₂↑")
    elif "氯气" in name_list and "水" in name_list and name3==0:
        print("Cl₂+H₂O======HClO+HCl(可逆)")
    elif "钙" in name_list and "水" in name_list and name3==0:
        print("Ca+2H₂O======Ca(OH)₂+H₂↑")
    #碱性氧化物和水反应
    #钠
    elif "氧化钠" in name_list and "水" in name_list and name3==0:
        print("Na₂O+2H₂O======2NaOH")
    elif "过氧化钠" in name_list and "水" in name_list and name3==0:
        print("2Na₂O₂+2H₂O======4NaOH+O₂↑")
    #钙
    elif "氧化钙" in name_list and "水" in name_list and name3==0:
        print("CaO+H₂O======Ca(OH)₂")
    elif "过氧化钠" in name_list and "水" in name_list and name3==0:
        print("2CaO₂+2H₂O======2Ca(OH)₂+O₂↑")
    #碱性氧化物和酸性氧化物反应
    #钠
    elif "氧化钠" in name_list and "二氧化碳" in name_list and name3==0:
        print("Na₂O+CO₂======Na₂CO₃")
    elif "过氧化钠" in name_list and "二氧化碳" in name_list and name3==0:
        print("2Na₂O₂+2CO₂======2Na₂CO₃+O₂↑")
    elif "氧化钠" in name_list and "二氧化硫" in name_list and name3==0:
        print("Na₂O+SO₂======Na₂SO₃")
    elif "过氧化钠" in name_list and "二氧化硫" in name_list and name3==0:
        print("Na₂O₂+SO₂======Na₂SO₄")
    #钙
    elif "氧化钙" in name_list and "二氧化碳" in name_list and name3==0:
        print("        高温")
        print("CaO+CO₂======CaCO₃")
    elif "过氧化钙" in name_list and "二氧化碳" in name_list and name3==0:
        print("2CaO₂+2CO₂======2CaCO₃+O₂↑")
    elif "氧化钠" in name_list and "二氧化硫" in name_list and name3==0:
        print("CaO+SO₂======CaSO₃")
    elif "过氧化钠" in name_list and "二氧化硫" in name_list and name3==0:
        print("CaO₂+SO₂======CaSO₄")
    #氯气和可溶性碱反应
    elif "氢氧化钠" in name_list and "氯气" in name_list and name3==0:
        print("2NaOH+Cl₂======NaCl+NaClO+H₂O")
        print("            Δ")
        print("6NaOH+3Cl₂======5NaCl+NaClO₃+3H₂O")
    #硫化反应
    elif "钠单质" in name_list and "硫单质" in name_list and name3==0:
        print("        Δ")
        print("2Na+S======Na₂S")
        print("      研磨")
        print("2Na+S======Na₂S(爆炸)")
    elif "钙单质" in name_list and "硫单质" in name_list and name3==0:
        print("        Δ")
        print("Ca+S======CaS(爆炸)")
        print("      研磨")
        print("Ca+S======CaS(爆炸)")
    elif "铁单质" in name_list and "硫单质" in name_list and name3==0:
        print("      Δ")
        print("Fe+S======Na₂S")
    elif "铜单质" in name_list and "硫单质" in name_list and name3==0:
        print("      Δ")
        print("Cu+S======Cu₂S")
    #取代反应
    #氯
    elif "氯气" in name_list and "氢氧化钠" in name_list and name3==0:
        print("Cl₂+2NaOH======NaCl+NaClO+H₂O")
    elif "氯气" in name_list and "氢氧化钙" in name_list and name3==0:
        print("2Cl₂+2Ca(OH)₂======CaCl₂+Ca(ClO)₂+2H₂O")
    #氢化反应
    elif "钠单质" in name_list and "氢单质" in name_list and name3==0:
        print("      Δ")
        print("2Na+H₂======2NaH")
    elif "钙单质" in name_list and "氢单质" in name_list and name3==0:
        print("      高温")
        print("Ca+H₂======CaH₂")
    #氢化物和水反应
    elif "氢化钠" in name_list and "水" in name_list and name3==0:
        print("NaH+H₂O======NaOH+H₂↑")
    elif "氢化钙" in name_list and "水" in name_list and name3==0:
        print("CaH₂+H₂O======Ca(OH)₂+2H₂↑")
    #其他反应
    elif "亚硫酸钠" in name_list and "次氯酸钠" in name_list and name3==0:
        print("NaClO+Na₂SO₃======NaCl+Na₂SO₄")
    else:
        print("error:Can not be proceed")
    print("\n\n反应结束\n\n")
    print("实验结束，自动退出反应器")
element_choic()
element_judge()
operation()