from os.path import join, isdir, isfile, basename

from os import listdir

import re

from articles.article_constants import ARTICLE_TITLE, ARTICLE_TEXT, ARTICLE_SUBJECT
from articles.models import Subject, Article
from catsekb.constants import NAME, IMAGE
from catsekb.settings import BASE_DIR
from catsekb.view_functions import create_or_update_default_articles

ARTICLES_DIR = join(BASE_DIR, 'articles', 'articles_list')

PATTERN_URL = re.compile(r"((https?://)?([-\w\.]+)\.([\w]{2,6}\.?)(/[-\w\.]*)*/?)", re.S)
PATTERN_IMG_URL = re.compile(
    r"""(?:\b[a-z\d.-]+://[^<>\s]+|\b(?:(?:(?:[^\s!@#$%^&*()_=+[\]{}\|;:'",.<>/?]+)\.)+(?:ac|ad|aero|ae|af|ag|ai|al|am|an|ao|aq|arpa|ar|asia|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|biz|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|cat|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|coop|com|co|cr|cu|cv|cx|cy|cz|de|dj|dk|dm|do|dz|ec|edu|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gov|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|info|int|in|io|iq|ir|is|it|je|jm|jobs|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mil|mk|ml|mm|mn|mobi|mo|mp|mq|mr|ms|mt|museum|mu|mv|mw|mx|my|mz|name|na|nc|net|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|org|pa|pe|pf|pg|ph|pk|pl|pm|pn|pro|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tel|tf|tg|th|tj|tk|tl|tm|tn|to|tp|travel|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|xn--0zwm56d|xn--11b5bs3a9aj6g|xn--80akhbyknj4f|xn--9t4b11yi5a|xn--deba0ad|xn--g6w251d|xn--hgbk6aj7f53bba|xn--hlcj6aya9esc7a|xn--jxalpdlp|xn--kgbechtv|xn--zckzah|ye|yt|yu|za|zm|zw)|(?:(?:[0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]))(?:[;/][^#?<>\s]*)?(?:\?[^#<>\s]*)?(?:#[^<>\s]*)?(?!\w))\.jpe?g""",
    re.S
)

TEMPLATE_TAG_PARAGRAPH = '\n<p>{text}</p>'
TEMPLATE_TAG_IMG = '\n<img src="{src}">'


class ArticleText:
    def __init__(self, text):
        self.text = text
        url = PATTERN_IMG_URL.search(self.text)
        if url:
            self.url = url.group()
        else:
            self.url = "http://127.0.0.1:8000/media/sad_cat.png"

    @staticmethod
    def combine_url_with_text(urls, lines):
        res = list()
        for i, l in enumerate(lines):
            paragraph = PATTERN_URL.sub(r'\n<a \1">Ссылка</a>', l)
            if paragraph:
                res.append(TEMPLATE_TAG_PARAGRAPH.format(text=paragraph))
            else:
                res.append('')
            try:
                res.append(TEMPLATE_TAG_IMG.format(src=urls[i]))
            except IndexError:
                pass
        return res

    def get_text_without_urls(self):
        return PATTERN_IMG_URL.split(self.text)

    def get_urls_from_text(self):
        return PATTERN_IMG_URL.findall(self.text)

    def get_text(self):
        # TODO: разделитель строки
        # TODO: оформление ссылок
        # TODO: оформление сылок на изображения
        text_without_urls = self.get_text_without_urls()
        img_urls = self.get_urls_from_text()
        res_list = self.combine_url_with_text(img_urls, text_without_urls)
        res_text = ''.join(res_list)
        return res_text


def create_article(art_fn, subject):
    if isfile(art_fn) and art_fn.endswith('.txt'):
        fn = basename(art_fn)
        title = fn[fn.index('-')+1:].replace('.txt', '')
        t = open(art_fn, 'r', encoding='UTF-8').read()
        at = ArticleText(t)
        text = at.get_text()
        article, created = Article.objects.get_or_create(
            title=title,
            defaults={
                ARTICLE_TITLE: title,
                ARTICLE_TEXT: text,
                ARTICLE_SUBJECT: subject,
                IMAGE: at.url,
            }
        )
        if created is False:
            article.__setattr__(ARTICLE_TITLE, title)
            article.__setattr__(ARTICLE_TEXT, text)
            article.__setattr__(ARTICLE_SUBJECT, subject)
            article.__setattr__(IMAGE, at.url)
            article.save()


def create_articles_by_subj(subject, subj_dir):
    l = listdir(subj_dir)
    l.sort(key=lambda s: int(s.split('-')[0]))
    for a in l:
        create_article(join(subj_dir, a), subject)


def update_articles():
    print('update articles')
    create_or_update_default_articles()
    subjects = [i for i in listdir(ARTICLES_DIR) if isdir(join(ARTICLES_DIR, i))]
    subjects.sort(key=lambda s: int(s.split('-')[0]))
    for subj in subjects:
        curr_dir = join(ARTICLES_DIR, subj)
        subject, updated = Subject.objects.get_or_create(
            name=subj[subj.index('-')+1:], defaults={NAME: subj[subj.index('-')+1:]}
        )
        create_articles_by_subj(subject, curr_dir)
    print('update articles is finished')

