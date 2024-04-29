from click import clear
import gradio as gr

with gr.Blocks() as app:
    with gr.Row(equal_height=True):
        text1 = gr.Textbox()
        text2 = gr.Textbox()
    with gr.Row():        
        btn1 = gr.Button("입력")
        btn2 = gr.Button("취소")
        
app.launch()

# chainterface
# def display(message, history, additional_input_info):
#     return message

# app = gr.ChatInterface(
#     fn=display,
#     textbox=gr.Textbox(placeholder="대화를 입력해 주세요", scale=7),
#     title="근로복지공단 챗봇",
#     description="마트이용에 대한 모든 것을 알려드립니다",
#     theme="soft",
#     examples=[["세일 물품"], ["물건 위치"], ["xx 가격 알려 줘"]],
#     retry_btn="재전송",
#     undo_btn="이전 대화 삭제",
#     clear_btn="모든 대화 삭제",
#     additional_inputs=[
#         gr.Textbox("관리자 호출", label="긴급 시 사용하세요")
#     ]
# )

# app.launch()

# Blocks
# def display(text):
#     return text
# with gr.Blocks() as app:
#     text1 = gr.Textbox(label="Name")
#     text2 = gr.Textbox(label="Output ")
#     btn = gr.Button(value="Submit")
#     btn.click(fn=display, inputs=text1, outputs=text2)

# app.launch()

# Tabbed Interface
# def display(text):
#     return text

# def display1(text):
#     return text

# app1 = gr.Interface(fn=display, inputs='text', outputs='text')
# app2 = gr.Interface(fn=display1, inputs='text', outputs='text')

# app = gr.TabbedInterface([app1, app2], ["입력1", "입력2"])

# app.launch()


# Multiple Input Output
# def display(text1, text2, image):
#     return text1 + text2, image

# app = gr.Interface(fn=display,
#                    inputs=["text", "text", gr.Image(height=200, width=200)],
#                    outputs=["text", gr.Image(height=400, width=400)]
#                    )
# app.launch()

# Single Input, Output
# def user_greeting(name):
#     return "안녕하세요" + name + " 고객님 근로복지공단에 오신것을 환영합니다."

# app=gr.Interface(
#         fn=user_greeting, 
#         inputs="text", 
#         outputs="text", 
#         title="근로복지공단"
#     )

# app.launch()

