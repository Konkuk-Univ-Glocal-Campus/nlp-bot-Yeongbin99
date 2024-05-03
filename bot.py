import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["꽤 흥미롭습니다. 더 알려주세요.",
                    "알겠어요. 계속하세요.",
                    "왜 그런 말을 하나요?",
                    "정말 웃긴 날씨지?",
                    "우리 주제를 바꿔 보자.",
                    "어젯밤에 경기 보셨나요?"]

print("안녕하세요 심플로봇 마빈 입니다.")
print("언제든지 '안녕'이라고 입력하시면 이 대화를 종료하실 수 있습니다.")
print("각 답을 입력한 후 'Enter'를 누르세요.")
print("오늘은 어때요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "안녕":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("얘기해서 즐거웠어요, 안녕!")
