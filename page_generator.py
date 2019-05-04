# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body, about):
	page = f"""<html>
    {head}
    {body}
	{about}
    </html>"""
	return page

def generate_about_block(url = "about.html"):
	block = "<hr><a href={0}>О реализации</a>".format(url)
	return block
	

def generate_head(title):
	head = "<meta charset='utf-8'>" + "<title>" + title + "</title>"
	return "<head>" + head + "</head>"

def generate_body(header, paragraphs):
	body = "<h1>" + header + "</h1>"
	i = 0
	while i < len(paragraphs):
		body = body + "<p>" + paragraphs[i] + "</p>"
		i = i + 1
	return "<body>" + body + "</body>"

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, 'w')
	today = dt.now().date()
	header += ' ' + str(today)
	page = generate_page(head=generate_head(title), body=generate_body(header=header, paragraphs=paragraphs), about = generate_about_block())
	print(page, file = fp)
	fp.close()


paragraphs = generate_prophecies(total_num = 3, num_sentences = 4)
title = 'Предсказания, гороскоп, трулала'
header = 'Ваши предсказания на '
save_page(title = title, header = header, paragraphs = paragraphs)