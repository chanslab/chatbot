# chatbot
 "Hey, 파이썬! 생성형 AI 활용 앱 만들어 줘" - 성안당, 김한호 외 2명 -   
 colab으로 개발한 내역을 로컬에 다시 작업


## 2024.4.26 
 가상환경을 venv로 설치할 경우 파이썬 특정 버전을 지정하는데 어려움이 있어서 (해당 파이썬 버전이 미리 설치되어 있어야 가능)    
 conda로 설치 문제는 경험상 conda는 호환되는 패키지 설치시 문제가 있음  
 일단, colab과 동일한 환경 구성(python 3.10.12) 을 위해서 anaconda를 설치하고 conda로 가상환경을 구성함

```shell
(base) ➜  chatbot git:(main) ✗ conda create -n .chatbot_conda python=3.10.12
(base) ➜  chatbot git:(main) ✗ conda activate .chatbot_conda
```

## gradio 설치 
```shell
pip install gradio
```

## OPENAI API 키
 colab에서는 민감정보 관리 화면에 등록하거나, colab 환경변수로 등록해서 사용 할 수 있음  
 
 로컬에서 사용할 경우 ~/.zshrc 에 등록하여 사용함  
 ```shell
 ehco OPENAI_API_KEY = '' >> ~/.zshrc
 ```
 또는
 ```python
 import os
 from getpass import getpass
 # getpass는 input과 동일하나, 입력값을 감추는 모듈
 os.environ['OPENAI_API_KEY']=getpass()
 ```
 불러올때는 
 ```python
 os.environ['OPENAI_API_KEY']
 # 또는 
 os.getenv('OPENAI_API_KEY')
 ```
 프로그램 내부에서 OPENAI API 키를 호출하는 메뉴가 없음에도 알아서 불러오고 있음  
 > 다른 책에서 OPENAI API 키를 관리하는 방법에 대해 경고하는 내용이 있음

- 
 
## 모델 선택 및 사용
model 안내 페이지에서 선택 
https://platform.openai.com/docs/models/overview
또는  
playground에서 선택할 수 있는 모델을 사용하면 됨


## OPENAI 호출
```python
# API 호출
completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
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
            "content": "안녕하세요!"
        }
    ]
)

# 결과 출력
print(completion.choices[0].message)
# 결과만 출력하고 싶을때
print(completion.choices[0].message.content)

```
### API 매개변수
|매개변수|내용|기본값      |
|----|:----|:----:|
|max_tokens|최대 답변 토큰 수|무한|
|temperature|창의적 정도<br>범위 0~2|1|
|top_p|토큰의 확률 분포 제한<br> 응답의 다양성 제어<br>일반적으로 건드리지 않음<br>범위 0~1|1|
|presense_penalty|이미 나온 내용 반복에 패널티 부여<br>값이 높을수록 이미 언급된 내용을 피하고 새로운 내용을 생성<br>범위 -2~2|0|
|frequency_penalty|자주 나타나는 단어나 구절을 반복하는 것에 대한 패널티 부여<br>값이 높을수록 흔한 단어나 구절을 피하고 독창적인 내용 생성<br>범위 -2~2|0|
|n|생성할 응답의 개수|1|
|stop|특정 문자열이나 문자열 목록을 만나면 응답을 중단<br>['.', 'END','end of text','\n'] 같은 값을 할당|null|

## graido 
사용해 보니, 기본적인 내용은 HTML수준의 화면 구성으로 쉬움   
streamlit은 계속 발전하고 있다는데, gradio는 어떤지 모르겠음

https://www.gradio.app/docs/gradio/chatinterface




