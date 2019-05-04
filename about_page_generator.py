# coding: utf-8
from horoscope import times, advices

def generate_page(title, body):
    page = f"""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>{title}</title>
            </head>
            <body>
                {body}   
            </body>
        </html>"""
 
    return page


def generate_ul(title, lst):
    li_text = ""
    for li in lst:
        li_text += "<li>{0}</li>".format(li)

    ul = """<h2>{title}</h2>
            <ul>{li}</ul>
            <hr>""".format(title = title, li = li_text)

    return ul  

def generate_footer():
    return """<footer><a href = "index.html">На главную</a></footer>"""

def save_page(title, output = 'about.html'):
    ###### генерим списки
    body = ""
    body += generate_ul(title = "Времена дня:", lst = times)
    body += generate_ul(title = "Глаголы:", lst = advices)
    body += generate_footer()

    fa = open(output, 'w')
    page = generate_page(title = title, body = body)
    print(page, file = fa)

save_page('О чём всё это')