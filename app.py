from openai import OpenAI
import gradio as gr

client=OpenAI()

# 상담봇 - 채팅 및 답변
def counseling_bot_chat(message, chat_history):
    if message == "":
        return "", chat_history
    else:
        completion=client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"당신은 근로복지공단의 부정수급 신고센터 상담원입니다. 부정수급신고와 관련되지 않은 질문에는 정중히 거절하세요"},
                {"role":"user", "content":message}
            ]
        )
        chat_history.append([message, completion.choices[0].message.content])
        return "", chat_history

# 상담봇 - 되돌리기
def counseling_bot_undo(chat_history):
    if len(chat_history) > 1:
        chat_history.pop()
    return chat_history

# 상담봇 - 초기화
def counseling_bot_reset(chat_history):
    chat_history=[[None, "안녕하세요, 헤이마트입니다. 상담을 도와드리겠습니다"]]
    return chat_history


# 번역봇 -
def translate_bot(output_conditions, output_language, input_text):
    if input_text =="":
        return ""
    else:
        if output_conditions == "":
            output_conditions = ""
        else:
            output_conditions="번역할 때의 조건은 다음과 같습니다" + output_conditions

        completion=client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role":"system", "content":"당신은 번역가입니다. 입력한 언어를 다른 설명 없이 곧바로 {0}로 번역해서 알려 주세요. 번역이 불가능한 언어라면 번역이 불가능하다고 말한 후 그 이유를 설명해 주세요. {1}".format(output_language, output_conditions)},
                    {"role":"user", "content": input_text}
                ]
            )
        return completion.choices[0].message.content


# 소설봇
def novel_bot(model, temperature, detail):
    completion=client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role":"system", "content":"당신은 소설가 입니다. 요청하는 조건에 맞춰 소설을 작성해 주세요."},
            {"role":"user", "content":detail}
        ]
    )
    return completion.choices[0].message.content

# 레이아웃 begin ----------------------------------------------------------------
with gr.Blocks(theme=gr.themes.Default()) as app:
    with gr.Tab("상담봇"):
        # 1 상단 타이틀
        gr.Markdown(
            value="""
            # <center>상담봇</center>
            <center>근로복지공단 부정수급 신고센터 상담봇입니다. 산업재해보상보험 부정수급 신고와 관련된 질문에 답변드립니다</center>
            """
        )
        # 2 채팅 화면
        cb_chatbot=gr.Chatbot(
            value=[[None, "안녕하세요, 산업재해보상보험 부정수급 신고의 상담을 도와드리겠습니다"]],
            show_label=False # 레이아웃 좌측 상단의 작은 Chatbot 라벨을 제거
        )
        with gr.Row():
            # 3 채팅 입력 창
            cb_user_input=gr.Text(
                lines=1,
                placeholder="입력 창",
                container=False,
                scale=9
            )
            # 4 채팅 보내기
            cb_send_btn=gr.Button(
                value="보내기",
                scale=1,
                variant="primary"
                # primary,secondary, neutral, stop
            )
        with gr.Row():
            # 5 마지막 채팅 되돌리기
            gr.Button(
                value="되돌리기"
            ).click(fn=counseling_bot_undo, inputs=cb_chatbot, outputs=cb_chatbot)
            # 6 채팅 초기화
            gr.Button(
                value="초기화"
            ).click(fn=counseling_bot_reset, inputs=cb_chatbot, outputs=cb_chatbot)
            # 보내기 버튼 클릭시
            cb_send_btn.click(fn=counseling_bot_chat, inputs=[cb_user_input, cb_chatbot], outputs=[cb_user_input, cb_chatbot])
            # 채팅 입력후 Enter시
            cb_user_input.submit(fn=counseling_bot_chat, inputs=[cb_user_input, cb_chatbot], outputs=[cb_user_input, cb_chatbot])
    with gr.Tab("번역봇"):
        # 1
        gr.Markdown(
            value="""
            # <center>번역봇</center>
            <center>다국어 번역봇입니다</center>
            """
        )
        with gr.Row():
            # 2
            tb_output_conditions=gr.Text(
                label="번역 조건",
                placeholder="예시: 자연스럽게",
                lines=1,
                max_lines=3
            )
            # 3
            tb_output_language=gr.Dropdown(
                label="출력 언어",
                choices=["한국어", "영어", "일본어", "중국어"],
                value="한국어",
                allow_custom_value=False,
                interactive=True
            )
        # 4
        tb_submit=gr.Button(
            value="번역하기",
            variant="primary"
        )
        with gr.Row():
            # 5
            tb_input_text=gr.Text(
                placeholder="번역할 내용을 적어 주세요",
                lines=10,
                max_lines=20,
                show_copy_button=True,
                label=""
            )
            # 6
            tb_output_text=gr.Text(
                lines=10,
                max_lines=20,
                show_copy_button=True,
                label="",
                interactive=False
            )
        # 번역봇 - 내용 보내기
        tb_submit.click(
            fn=translate_bot,
            inputs=[tb_output_conditions,
                    tb_output_language,
                    tb_input_text],
            outputs=tb_output_text
        )
    with gr.Tab("소설봇"):
        # 1
        gr.Markdown(
            value="""
            # <center>소설봇</center>
            <center>소설을 생성해 주는 봇입니다</center>
            """
        )
        with gr.Accordion(label="사용자 설정"):
            with gr.Row():
                with gr.Column(scale=1):
                    # 2
                    nb_model=gr.Dropdown(
                        label="모델 선택",
                        choices=["gpt-3.5-turbo","gpt-3.5-turbo-16k","gpt-4","gpt-4-32k","gpt-4-1106-preview"],
                        value="gpt-4-1106-preview",
                        interactive=True
                    )
                    # 3
                    nb_temperature=gr.Slider(
                        label="창의성",
                        info="숫자가 높을 수록 창의적",
                        minimum=0,
                        maximum=2,
                        step=0.1,
                        value=1,
                        interactive=True
                    )
                # 4
                nb_detail=gr.Text(
                    container=False,
                    placeholder="소설의 세부적인 설정을 작성합니다.",
                    lines=8,
                    scale=4
                )
        # 5
        nb_submit=gr.Button(
            value="생성하기",
            variant="primary"
        )
        # 6
        nb_output=gr.Text(
            label="",
            placeholder="이곳에 소설의 내용이 출력됩니다",
            lines=10,
            max_lines=200,
            show_copy_button=True
        )

        # 보내기
        nb_submit.click(
            fn=novel_bot,
            inputs=[nb_model, nb_temperature, nb_detail],
            outputs=nb_output
        )

# 레이아웃 end ----------------------------------------------------------------

# 실행
app.launch(debug=True)  # debug=True일 경우 프로그램에 오류가 발생했을때 확인이 용이함