import requests
from bs4 import BeautifulSoup

newsurl = input ('请输入新闻网址：')
def getNewDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    #找到文章标题
    result['文章标题：'] = soup.select('#artibodyTitle')[0].text

    #找到新闻来源
    result['新闻来源：'] = soup.select('.time-source span a')[0].text
    
    #找到发布时间
    result['发布时间：'] = soup.select('.time-source')[0].contents[0].strip()
    
    #找到正文内容
    result['正文内容：'] = soup.select('#artibody')[0].text
    
    #找到责任编辑
    result['责任编辑：'] = soup.select('.article-editor')[0].text
    
    #找到评论总数
    result['总评论数：'] = getCommentCounts(newsurl)
    return result

def getCommentCounts(newsurl):
    m = re.search('doc-i(.+).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']

print (getNewDetail(newsurl))