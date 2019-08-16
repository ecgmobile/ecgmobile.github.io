# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from .app import app, pages

def menu_pages():
    web_pages = [page for page in pages if page.meta['type'] == 'page' and not 'hidden' in page.meta]
    # Sort pages by date
    return sorted(web_pages, key=lambda page: page.meta['date'])

def sections(page):
    title = page.meta['title']
    sections = [page for page in pages if page.meta['type'] == 'section' and page.meta['page'] == title]
    return sorted(sections, key=lambda page: page.meta['id'])

@app.route('/')
def home():
    return redirect('/home/')

@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-page"
    page = pages.get_or_404(path)
    page_sections = sections(page)
    return render_template('page.html', page=page, pages=menu_pages(), sections=page_sections, enumerate=enumerate, len=len)
    