#음료수 클래스
class Beberage:
	def __init__(self,name,price,quantity):
		self.name=name
		self.price=price
		self.quantity=quantity
 
#자판기(돈) 클래스
class Bending:
	def __init__(self,money1000,money500,money100):
		self.money1000=money1000 #1000원 짜리 갯수
		self.money500=money500 #500원 짜리 갯수
		self.money100=money100 #100원 짜리 갯수
		self.total_money=money1000*1000+money500*500+money100*100 #가지고 있는 동전의 갯수로 총 보유금 계산
		self.item = [Beberage("coke",700,20),Beberage("sprite",600,20),Beberage("암바사",600,20),
		Beberage("조이",500,20),Beberage("파워에이드",1000,20),Beberage("코코팜",700,20),
		Beberage("순수",500,20),Beberage("트레타",1300,20),Beberage("옥수수 수염차",1000,20),
		Beberage("선키스트",1000,20),Beberage("미닛메이드",1000,20),Beberage("식혜",600,20),
		Beberage("조지아",500,20),Beberage("맥스",700,20),Beberage("유자",600,20),
		Beberage("닥터페퍼",1000,0)] #가지고 있는 음료수 배열
 
#과금 클래스
class Calculate:
	def menu():
		while True:
			print("==============")
			number=int(input("시작:1, 종료:0\n"))
			if(not number):break; #0이면 종료
 
			#사용자 입력
			print("금액을 입력하세요.")
			money1000=int(input("1000원(개):"))
			money500=int(input("500원(개):"))
			money100=int(input("100원(개):"))
			total_money = money1000*1000+money500*500+money100*100 #사용자가 넣은 총 금액 계산
			print("총 금액:",total_money)
			print();

			#음료 이름, 가격, 재고 출력
			for i in range(0,16):
				print(i)
				print(japanki.item[i].name)
				print(japanki.item[i].price,"원")
				print(japanki.item[i].quantity,"개")
				print("----------------------")
 
			select=int(input("음료를 선택하세요."))
 
			total_change = total_money-japanki.item[select].price #거스름돈 총액
			change1000 = total_change//1000 #거슬러 줘야하는 1000원 짜리 갯수
			change500 = (total_change-change1000*1000)//500 #거슬러 줘야하는 500원 짜리 갯수
			change100 = total_change%500//100 #거슬러 줘야하는 100원 짜리 갯수
 
			print("선택한 음료수:",japanki.item[select].name,", 가격:",japanki.item[select].price,)
 
			if total_money>=japanki.item[select].price: #넣은 돈이 음료를 뽑는 데 충분한지 판별
				if japanki.item[select].quantity>0: #재고가 있는지 판별
					#자판기가 충분한 거스름돈을 가지고 있는지 판별
					if japanki.money1000>=change1000 and japanki.money500>=change500 and japanki.money100>=change100: 
						japanki.money1000+=money1000
						japanki.money500+=money500
						japanki.money100+=money100
						japanki.total_money=japanki.money1000*1000+japanki.money500*500+japanki.money100*100
 
 						#해당 음료의 갯수를 빼고 돈 계산
						japanki.item[select].quantity-=1
						japanki.money1000-=change1000
						japanki.money500-=change500
						japanki.money100-=change100
						japanki.total_money=japanki.money1000*1000+japanki.money500*500+japanki.money100*100
						total_change=change1000*1000+change500*500+change100*100
						
						print("거스름돈: ",total_change)
					else:
						print("거스름돈이 부족합니다.");
				else:
					print("해당 음료가 모두 소진되었습니다.")
			else:
				print("금액이 부족합니다.")
 
			print("")
			print("1000원 수: ",japanki.money1000)
			print("500원 수: ",japanki.money500)
			print("100원 수: ",japanki.money100)
			print("자판기 보유금:",japanki.total_money)
 
japanki=Bending(100,100,100) #금액 초기화 및 생성
calculate.menu();