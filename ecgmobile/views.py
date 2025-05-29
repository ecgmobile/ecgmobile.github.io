# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from .app import app, pages, freezer

DEFAULT_LANG='en'

def menu_pages(lang):
    web_pages = [page for page in pages if page.meta['type'] == 'page' and not 'hidden' in page.meta and not 'root' in page.meta and 'lang' in page.meta and page.meta['lang'] == lang ]
    print(lang)
    return sorted(web_pages, key=lambda page: page.meta['date'])

def sections(page):
    title = page.meta['title']
    sections = [page for page in pages if page.meta['type'] == 'section' and page.meta['page'] == title]
    return sorted(sections, key=lambda page: page.meta['id'])

def create_page(path, lang):
    page = pages.get_or_404(path)
    page_sections = sections(page)
    return render_template('page.html', page=page, pages=menu_pages(lang), sections=page_sections, lang=lang, enumerate=enumerate, len=len)

@app.route('/')
def main():
    return redirect('/{}/'.format(DEFAULT_LANG))

@app.route('/<lang>/')
def main_localized(lang):
    return create_page('main_{}'.format(lang), lang)

@app.route('/<lang>/<path:path>/')
def page(lang, path):
    if path == 'main':
        redirect('/')
    return create_page('{}_{}'.format(path, lang), lang)

@app.route('/support/')
def support():
    return redirect('/ru/support/')

@app.route('/privacy-policy/')
def privacy_policy():
    return redirect('/ru/privacy-policy/')

@freezer.register_generator
def main_localized():
    yield {'lang': 'en'}

@freezer.register_generator
def page():
    yield {'lang': 'ru', 'path': 'main'}
    yield {'lang': 'en', 'path': 'main'}
    yield {'lang': 'ru', 'path': 'support'}
    yield {'lang': 'en', 'path': 'support'}
    yield {'lang': 'ru', 'path': 'privacy-policy'}
    yield {'lang': 'en', 'path': 'privacy-policy'}
    yield {'lang': 'ru', 'path': 'ecg-mob-privacy-policy'}
    yield {'lang': 'en', 'path': 'ecg-mob-privacy-policy'}

@freezer.register_generator
def support():
    yield '/support/'

@freezer.register_generator
def privacy_policy():
    yield '/privacy-policy/'
    