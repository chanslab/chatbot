# OPENAI LLMs 연결
# 기존의 langchain.llms 는 Deprecated (며칠사이에 갑자기 Deprecated)
# To use it run `pip install -U langchain-openai` and import as `from langchain_openai import OpenAI`.
# https://python.langchain.com/docs/integrations/platforms/openai/
# from langchain_openai import OpenAI
from langchain_openai.llms import OpenAI

# OpenAI 공식문서에서 사용하고 있는 모델과 동일한 모델 선택
# https://platform.openai.com/docs/guides/text-generation/completions-api
gpt = OpenAI(model_name="gpt-3.5-turbo", temperature=0)
gpt.predict('파이썬을 만든 사람은?')

