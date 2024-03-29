def calculate_change(item_price, payment):
    # 잔돈 계산
    change = payment - item_price

    # 동전의 갯수 계산
    num_1000 = change // 1000
    change %= 1000

    num_500 = change // 500
    change %= 500

    num_100 = change // 100
    change %= 100

    num_50 = change // 50
    change %= 50

    num_10 = change // 10

    return num_1000, num_500, num_100, num_50, num_10

item_price, payment = map(int, input("물건 가격과 지불 가격을 입력하세요: ").split())

    num_1000, num_500, num_100, num_50, num_10 = calculate_change(item_price, payment)

    print("1000원 동전의 개수:", num_1000)
    print("500원 동전의 개수:", num_500)
    print("100원 동전의 개수:", num_100)
    print("50원 동전의 개수:", num_50)
    print("10원 동전의 개수:", num_10)
