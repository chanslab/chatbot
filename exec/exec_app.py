import os
from openai import OpenAI
client=OpenAI()

# OPENAI_API_KEY 불러오기
#print(os.getenv('OPENAI_API_KEY'))

# API 호출
completion=client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    # messages에 값을 할 당 할때는 반드시 딕셔너리를 담은 리스트를 작성해야 함
    # 딕셔너리는 role, content로 이루어진 2개의 키가 포함되어 있어야 함
    # role의 값 "system", "user", "assistant", "tool"
    # content에는 role에 들어간 규칙에 맞는 지침 또는 메시지 작성
    messages=[
        {
            "role":"system",
            "content":"당신은 근로복지공단의 상담원입니다."
        },
        {
            "role": "user",
            "content": "저녁으로 무엇을 먹을까요? 짧게 설명해주세요"
        }
    ],
    temperature=1.8,
    max_tokens=100,
    top_p=1,
    presence_penalty=0,
    frequency_penalty=0,
    n=2,
    stop=None
)

# 결과 출력
# print(completion.choices[0].message)
# print(completion.choices[0].message.content)
for choice in completion.choices:
    print(choice.index, choice.message.content)
