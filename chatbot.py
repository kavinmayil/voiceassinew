import os
from embedchain import App

os.environ["OPENAI_API_KEY"]=""
elon_bot= App()

elon_bot.add("web_page","https://en.wikipedia.org/wiki/Elon_Musk")
elon_bot.add("web_page","https://tesla.com/elon-musk")
elon_bot.add("web_page","https://www.youtube.com/watch?v=MxZpaJK74Y4")

response = elone_bot.query("")
print(response)
