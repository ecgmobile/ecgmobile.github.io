# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from .app import app, pages

def menu_pages():
    web_pages = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    return sorted(web_pages, key=lambda page: page.meta['date'])

@app.route('/')
def home():
    return redirect('/home/')

@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-page"
    page = pages.get_or_404(path)
    return render_template('page.html', pages=menu_pages(), page=page)
