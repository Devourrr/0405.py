'''
레스토랑 클래스
    속성
    - 카테고리
    - 음식메뉴
    - 가격
    - 재료

    기능
    - 주문 받기
    - 장보기
    - 요리하기
    - 결제하기
    - 음식 추천
'''
class Restaurant:
    #속성
    # name = '돈까스식당'
    # food = ['돈까스세트', '쫄면', '만두']
    # price = '7900'
    # money = '시재'
    # material = '음식'
    # hall = '홀'
    # customer = ['노인과 아동2명','성인 남성과 성인 여성','중년 남성','청소년 4명']
    customer = ['노인과 아동2명','성인 남성과 성인 여성','중년 남성','청소년 4명']
    menu = ['돈까스세트', '쫄면', '만두']
    


    #기능 생성자 메서드
    def __init__(self,name): # 오픈
        self.name= name
        print(f"{name}가 오픈했습니다")

    def customer1(self, customer): # 손님
        for c in customer:
            self.customer.append(c) 
        print(f"{self.name}에 {customer}가 입장했습니다")
    
    def food(self,menu): #메뉴
        print(f"{self.name}에서 제공하는 메뉴는 {self.menu}가 있습니다")

 

    def order(self,order): #주문
        self.order
        print(f"{self.customer[0]}이{self.menu[0],self.menu[1],self.menu[2] }를 주문합니다")
        print(f"{self.customer[1]}이 {self.menu[1],self.menu[2]}를 주문합니다")
        print(f"{self.customer[2]}이 {self.menu[2]}를 주문합니다")
        print(f"{self.customer[3]}이 {self.menu[0]}2인분 ,{self.menu[1]} 하나,{self.menu[2]} 하나를 주문합니다")

 
    def cook(self,cook): #요리
       self.cook
       print(f"주문하신{self.menu[0],self.menu[1],self.menu[2] }를 조리합니다 ")
       print(f"주문하신 {self.menu[1],self.menu[2]}를 조리합니다 ")
       print(f"주문하신{self.menu[2] }를 조리합니다 ")
       print(f"주문하신{self.menu[0]}2인분 ,{self.menu[1]} 하나,{self.menu[2]}를 조리합니다 ")

    def ser(self,serving): #서빙
        self.ser
        print(f"조리된 {self.menu[0],self.menu[1],self.menu[2] }을 서빙합니다 ")
        print(f"조리된 {self.menu[1],self.menu[2]}을 서빙합니다 ")
        print(f"조리된 {self.menu[2] }을 서빙합니다 ")
        print(f"조리된 {self.menu[0]}2인분 ,{self.menu[1]} 하나,{self.menu[2]}을 서빙합니다 ")

    
        
        
r1 = Restaurant('코돈블루')
r1.customer1(['노인과 아동2명','성인 남성과 성인 여성','중년 남성','청소년 4명'])
r1.food(['돈까스세트', '쫄면', '만두'])
r1.order(['돈까스세트', '쫄면', '만두'])
r1.cook('')
r1.ser