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
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="js/bootstrap.min.js"></script>
    <style>
        /* 自定义样式，使链接看起来像普通文本 */
        .info-link {
            color: inherit; /* 继承父元素的文本颜色 */
            text-decoration: none; /* 去除下划线 */
        }

        .info-link:hover, .info-link:focus {
            color: inherit; /* 鼠标悬停或聚焦时颜色保持不变 */
            text-decoration: none; /* 鼠标悬停或聚焦时去除下划线 */
        }
    </style>
    <title>近期电影即将上映影片信息</title>

</head>
<body>
<h2 class="text-center">近期即将上映影片信息</h2>
<div class="table-responsive">
    <table class="table table-striped table-hover mx-auto text-center">
        <thead>
        <tr>
            <th scope="col">电影名(点击了解影片)</th>
            <th scope="col">放映日期</th>
            <th scope="col">电影类型</th>
            <th scope="col">首映地区</th>
            <th scope="col">关注者数量</th>
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
</div>
<script>
    // 获取所有的链接元素
    const links = document.getElementsByTagName('a');

    // 定义可用的颜色列表
    const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'];

    // 为每个链接设置随机颜色
    for (let i = 0; i < links.length; i++) {
        links[i].style.color = colors[Math.floor(Math.random() * colors.length)];
    }
</script>
<div class="bg-light p-3">
    <p><a class="info-link" href="https://beian.miit.gov.cn/" target="_blank"><span>蜀ICP备2022005602号</span></a>
    </p>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>
</html>""")
file_obj.close()
print("finshed")
