import requests
from bs4 import BeautifulSoup
import pypandoc

# 获取文章内容
url = 'https://www.example.com/article'
response = requests.get(url)
html = response.text

# 解析网页内容
soup = BeautifulSoup(html, 'html.parser')
article = soup.find('div', {'class': 'article-content'})

# 转换为 Markdown 格式
markdown = pypandoc.convert_text(str(article), 'markdown', format='html')

# 输出 Markdown 文本
print(markdown)
