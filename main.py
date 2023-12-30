import random

print("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)")
carsName = input().split(",")

cars = {carName: 0 for carName in carsName}

print("시도할 횟수는 몇회인가요?")
count = int(input())

print("\n실행결과")
for _ in range(count):
    for car in cars:
        if random.choice([0, 1]) == 1:
            cars[car] += 1
        print(car + " : " + "-" * cars[car])
    print()

maxStep = max(cars.values())

winners = list()
for car in cars:
    if cars.get(car) == maxStep:
        winners.append(car)

print(f"최종 우승자 : {', '.join(winners)}")