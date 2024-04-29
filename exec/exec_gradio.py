import gradio as gr

# 20. Button
# with gr.Blocks() as app:
#     text1 = gr.Textbox(label="Name")
#     text2 = gr.Textbox(label="Output")
#     btn1 = gr.Button(value="Submit")
#     btn1.click(fn=lambda text : text, inputs=text1, outputs=text2)
#     gr.ClearButton([text1, text2])
    
# app.launch()


# 19. 드롭다운
# def display(dropmenu):
#     return dropmenu + "으로 이동합니다"

# app = gr.Interface(
#     display,
#     gr.Dropdown(['1층', '2층', '3층'], 
#                 label='이동 층', 
#                 info='이동할 층을 골라주세요'),
#     gr.Text()
# )
# app.launch()

# 18. 슬라이더
# def display(value):
#     return "구매 개수 : " + str(value)

# app = gr.Interface(
#     display,
#     gr.Slider(minimum=0, maximum=100, step=1),
#     "text"
# )
# app.launch()

# 17. 셀렉트 박스
# def display(cart):
#     text='장바구니 : '
#     for temp in cart:
#         text += temp
#         text += ' '
#     return text

# app = gr.Interface(
#     display,
#     gr.CheckboxGroup(["사과", "딸기", "바나나", "수박"]),
#     "text"
# )

# app.launch()

# 16. 체크 박스
# app = gr.Interface(lambda check : "VIP입니다" if check==True else "일반 고객입니다",
#                    gr.Checkbox(label="VIP 유무"),
#                    "text")
# app.launch()

# 15. 미디어 - 영상
# app = gr.Interface(lambda audio : audio, gr.Audio(), "audio")
# app.launch()

# 14. 미디어 - 영상
# app = gr.Interface(lambda video : video, gr.Video(), "video")
# app.launch()

# 13. 미디어 - input에 deafult 이미지 추가
# demo = gr.Interface(
#     lambda image : image.rotate(45),
#     gr.Image(type="pil", width=400, height=300, value="images/마릴.webp"),
#     gr.Image(type="pil", width=400, height=300),
#     examples=[
#         "images/마릴.webp",
#         "images/뮤.webp",
#         "images/빠모.webp",
#         "images/잠만보.jpeg"   
#     ]
# )
# demo.launch()

# 12. 미디어 - examples
# demo = gr.Interface(fn= lambda image : image.rotate(90),
#                     inputs=gr.Image(type='pil'),
#                     outputs="image")
# 다른 방식 fn, inputs, Image등의 매개변수 명을 넣지 않는 방식
# demo = gr.Interface(
#     lambda image : image.rotate(45),
#     gr.Image(type="pil", width=400, height=300),
#     gr.Image(type="pil", width=400, height=300),
#     examples=[
#         "images/마릴.webp",
#         "images/뮤.webp",
#         "images/빠모.webp",
#         "images/잠만보.jpeg"   
#     ]
# )
# demo.launch()

# 11. 데이터
# demo = gr.Interface(fn=lambda data : data, inputs=gr.DataFrame(), outputs="dataframe")
# demo.launch()

# 10. 텍스트
# def display(text):
#     return text
# lambda 이용
# app = gr.Interface(fn=lambda text : text, inputs=gr.Text(), outputs=gr.Textbox())
# app.launch()

# 9. Block - group
# with gr.Blocks() as app:
#     with gr.Group():
#         with gr.Row():
#             with gr.Tab("구매"):
#                 text3 = gr.Textbox()
#                 btn3 = gr.Button("구매하기")
#             with gr.Tab("환불"):
#                 text4 = gr.Textbox()
#                 btn4 = gr.Button("환불하기")
# app.launch()


# 8. Block - Tab
# with gr.Blocks() as app:
#     with gr.Row():
#         with gr.Tab("구매"):
#             text3 = gr.Textbox()
#             btn3 = gr.Button("구매하기")
#         with gr.Tab("환불"):
#             text4 = gr.Textbox()
#             btn4 = gr.Button("환불하기")
# app.launch()


# 7. Block - Column
# with gr.Blocks() as app:
#     with gr.Row():
#         with gr.Column(scale=9):
#             text1 = gr.Textbox()
#             text2 = gr.Textbox()
#         with gr.Column(scale=1):
#             btn1 = gr.Button("1층")
#             btn2 = gr.Button("2층")
            
# app.launch()


# 6. Block - Row
# with gr.Blocks() as app:
#     with gr.Row(equal_height=True):
#         text1 = gr.Textbox()
#         text2 = gr.Textbox()
#     with gr.Row():        
#         btn1 = gr.Button("입력")
#         btn2 = gr.Button("취소")
        
# app.launch()

# 5. chainterface
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

# 4. Blocks
# def display(text):
#     return text
# with gr.Blocks() as app:
#     text1 = gr.Textbox(label="Name")
#     text2 = gr.Textbox(label="Output ")
#     btn = gr.Button(value="Submit")
#     btn.click(fn=display, inputs=text1, outputs=text2)

# app.launch()

# 3. Tabbed Interface
# def display(text):
#     return text

# def display1(text):
#     return text

# app1 = gr.Interface(fn=display, inputs='text', outputs='text')
# app2 = gr.Interface(fn=display1, inputs='text', outputs='text')

# app = gr.TabbedInterface([app1, app2], ["입력1", "입력2"])

# app.launch()


# 2. Multiple Input Output
# def display(text1, text2, image):
#     return text1 + text2, image

# app = gr.Interface(fn=display,
#                    inputs=["text", "text", gr.Image(height=200, width=200)],
#                    outputs=["text", gr.Image(height=400, width=400)]
#                    )
# app.launch()

# 1. Single Input, Output
# def user_greeting(name):
#     return "안녕하세요" + name + " 고객님 근로복지공단에 오신것을 환영합니다."

# app=gr.Interface(
#         fn=user_greeting, 
#         inputs="text", 
#         outputs="text", 
#         title="근로복지공단"
#     )

# app.launch()

