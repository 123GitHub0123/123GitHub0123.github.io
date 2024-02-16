import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/cinema/later/china"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
# 3.获取并分析元素
all_movies = soup.find('div', id="showing-soon")
# 4.展示有用信息
for each_movie in all_movies.find_all('div', class_="item"):
    # print(each_movie)
    all_a_tag = each_movie.find_all('a')
    all_li_tag = each_movie.find_all('li')
    all_span_tag = each_movie.find_all('li', class_="dt last")
    movie_name = all_a_tag[1].text
    movie_href = all_a_tag[1]['href']
    movie_date = all_li_tag[0].text
    movie_type = all_li_tag[1].text
    movie_area = all_li_tag[2].text
    movie_lovers = all_span_tag[0].text
    print('电影名：{},电影链接：{},放映日期：{},电影类型：{},首映地区：{},想看的人数：{}'.format(
        movie_name, movie_href, movie_date, movie_type, movie_area, movie_lovers))
# 5.将获取的有用信息保存到一个html文件
# python里面三个"围起来的字符会被看做是一整个字符串，避免了换行符的麻烦。
# .format()这个方法的用法是把字符串里面的{}字符，按次序一一替换成 format() 接受的所有参数。
file_obj = open('index.html', 'w', encoding="utf-8")
file_obj.write("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>近期电影即将上映影片信息</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<h2 class="text-center">近期即将上映影片信息</h2>
<table class="table table-striped table-hover mx-auto text-center">
    <thead>
        <tr>
            <th>电影名(点击了解影片)</th>
            <th>放映日期</th>
            <th>电影类型</th>
            <th>首映地区</th>
            <th>关注者数量</th>
        </tr>
    </thead>
    <tbody>
""")
for each_movie in all_movies.find_all('div', class_="item"):
    # print(each_movie)
    all_a_tag = each_movie.find_all('a')
    all_li_tag = each_movie.find_all('li')
    all_span_tag = each_movie.find_all('li', class_="dt last")
    movie_name = all_a_tag[1].text
    movie_href = all_a_tag[1]['href']
    movie_date = all_li_tag[0].text
    movie_type = all_li_tag[1].text
    movie_area = all_li_tag[2].text
    movie_lovers = all_span_tag[0].text
    # print('电影名：{},电影链接：{},放映日期：{},电影类型：{},上映地区：{},想看的人数：{}'.format(
    #    movie_name,movie_href,movie_date,movie_type,movie_area,movie_lovers))
    file_obj.write("""
        <tr>
            <td><a onclick="window.open('{}', '_blank')">{}</a></td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
    """.format(movie_href, movie_name, movie_date, movie_type, movie_area, movie_lovers))
file_obj.write("""
     </tbody>
</table>
	  <script>
    // 获取所有的链接元素
    const links = document.getElementsByTagName('a');

    // 定义可用的颜色列表
    const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'];

    // 为每个链接设置随机颜色
    for (let i = 0; i < links.length; i++) {
      const randomColor = colors[Math.floor(Math.random() * colors.length)];
      links[i].style.color = randomColor;
    }
  </script>
<a href="https://beian.miit.gov.cn/" target="_blank">蜀ICP备2022005602号</a>
</body>
</html>
    """)
file_obj.close()
print("finshed")
