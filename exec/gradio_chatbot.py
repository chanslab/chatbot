import gradio as gr


# 레이아웃 begin

with gr.Blocks(theme=gr.themes.Default()) as app:
    with gr.Tab("상담"):
        # 1 타이틀 및 설명
        gr.Markdown(
            value="""
            # <center> 산재보험 부정수급신고 상담 </center>
            ## <center> 근로복지공단의 산재보험 부정수급신고 상담봇입니다. 부정수급신고와 관련된 질문에 답변드립니다.</center>
            """
        )
        # 2 chatbot 화면
        gr.Chatbot(
            value=[[None, "안녕하세요, 근로복지공단 부정수급신고의 상담을 도와드리겠습니다"]],
            show_label=False
        )
        # 채팅 입력 화면
        with gr.Row():
            # 3
            gr.Text(
                lines=1,
                placeholder="입력 창",
                container=False,
                
            )
            # 4
            gr.Button()
        with gr.Row():
            # 5
            gr.Button()
            # 6
            gr.Button()
    with gr.Tab("번역"):
        pass
    with gr.Tab("소설"):
        pass


# 레이아웃 end
app.launch()