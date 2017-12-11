from os.path import join, isdir, isfile, basename

from os import listdir

from articles.article_constants import ARTICLE_TITLE, ARTICLE_TEXT, ARTICLE_SUBJECT
from articles.models import Subject, Article
from catsekb.constants import NAME
from catsekb.settings import BASE_DIR

ARTICLES_DIR = join(BASE_DIR, 'articles', 'articles_list')


def create_article(art_fn, subject):
    if isfile(art_fn) and art_fn.endswith('.txt'):
        title = basename(art_fn).replace('.txt', '')
        text = open(art_fn, 'r', encoding='UTF-8').read()
        Article.objects.get_or_create(
            title=title,
            defaults={
                ARTICLE_TITLE: title,
                ARTICLE_TEXT: text,
                ARTICLE_SUBJECT: subject
            }
        )


def create_articles_by_subj(subject, subj_dir):
    for a in listdir(subj_dir):
        create_article(join(subj_dir, a), subject)


def update_articles():
    subjects = listdir(ARTICLES_DIR)
    for subj in subjects:
        curr_dir = join(ARTICLES_DIR, subj)
        if isdir(curr_dir):
            subject, updated = Subject.objects.get_or_create(name=subj, defaults={NAME: subj})
            create_articles_by_subj(subject, curr_dir)

