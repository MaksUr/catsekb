from os.path import join

from catsekb.constants import URL_NAME_CONTACTS, URL_NAME_FIND_CAT, CAPTION, URL, SHOW, CREATED, CREATED_KEY, UPDATED, \
    UPDATED_KEY, SUBJECT, AUTHOR, NAME, TEXT, TITLE, FOLDER, Y_POS, KEY_Y_POS, KEY_Y_POS_HELP_TEXT, USE_BACKGROUND, \
    KEY_USE_BACKGROUND, KEY_USE_BACKGROUND_HELP_TEXT, URL_NAME_ABOUT

FEED_PAGINATE_BY = 10


APPLICATION_VERBOSE_NAME = 'Статьи'

# class Author
AUTHOR_VERBOSE_NAME = 'Автор'
AUTHOR_VERBOSE_NAME_PLURAL = 'Авторы'

# name
AUTHOR_NAME = NAME
AUTHOR_KEY_NAME = 'Автор'
AUTHOR_KEY_NAME_HELP_TEXT = ''


# class Subject
SUBJECT_VERBOSE_NAME = 'Тема'
SUBJECT_VERBOSE_NAME_PLURAL = 'Темы'

# name
SUBJECT_NAME = NAME
SUBJECT_KEY_NAME = SUBJECT_VERBOSE_NAME
SUBJECT_KEY_NAME_HELP_TEXT = 'Укажи тематику статьи'

# show
SUBJECT_SHOW = SHOW
SUBJECT_KEY_SHOW = 'Показывать тему статей'
SUBJECT_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть. ' \
                           'Скрытые темы статей доступны для персонала на сайте.'


# class Article
ARTICLE_VERBOSE_NAME = 'Статья'
ARTICLE_VERBOSE_NAME_PLURAL = APPLICATION_VERBOSE_NAME

# title
ARTICLE_TITLE = TITLE
ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE = '"{title}" имеет недопустимое значение.'
ARTICLE_KEY_TITLE = 'Название статьи'
ARTICLE_KEY_TITLE_HELP_TEXT = ''

# text
ARTICLE_TEXT = 'text'
ARTICLE_KEY_TEXT = 'Текст статьи'
ARTICLE_KEY_TEXT_HELP_TEXT = 'Используйте html теги: <p> <a> <img> для форматирования текста.'

# created
ARTICLE_CREATED = CREATED
ARTICLE_KEY_CREATED = CREATED_KEY
ARTICLE_KEY_CREATED_HELP_TEXT = ''

# updated
ARTICLE_UPDATED = UPDATED
ARTICLE_KEY_UPDATED = UPDATED_KEY
ARTICLE_KEY_UPDATED_HELP_TEXT = ''

# show
ARTICLE_SHOW = SHOW
ARTICLE_KEY_SHOW = 'Показывать статью'
ARTICLE_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть. ' \
                           'Скрытые статьи доступны для персонала на сайте.'

# y_pos
ARTICLE_Y_POS = Y_POS
ARTICLE_KEY_Y_POS = KEY_Y_POS
ARTICLE_KEY_Y_POS_HELP_TEXT = KEY_Y_POS_HELP_TEXT

# use_background
ARTICLE_USE_BACKGROUND = USE_BACKGROUND
ARTICLE_KEY_USE_BACKGROUND = KEY_USE_BACKGROUND
ARTICLE_KEY_USE_BACKGROUND_HELP_TEXT = KEY_USE_BACKGROUND_HELP_TEXT

# author
ARTICLE_AUTHOR = AUTHOR

# subject
ARTICLE_SUBJECT = SUBJECT

# Article instances
ARTICLE_CONTACTS_ID = 1
ARTICLE_FIND_CAT_ID = 2
ARTICLE_ABOUT_ID = 3

ARTICLES_DEFAULT_MAPPING = {
    ARTICLE_CONTACTS_ID: {
        CAPTION: 'Контакты',
        URL: URL_NAME_CONTACTS,
        FOLDER: join('articles', 'articles_list', 'contacts.txt'),
    },
    ARTICLE_FIND_CAT_ID: {
        CAPTION: 'Что делать я нашел кота',
        URL: URL_NAME_FIND_CAT,
        FOLDER: join('articles', 'articles_list', 'find_cat.txt'),
    },
    ARTICLE_ABOUT_ID: {
        CAPTION: 'О проекте',
        URL: URL_NAME_ABOUT,
        FOLDER: join('articles', 'articles_list', 'about.txt'),
    },
}


ARTICLES_DEFAULT_CAPTIONS = tuple((ARTICLES_DEFAULT_MAPPING[i][CAPTION] for i in ARTICLES_DEFAULT_MAPPING))


# class News
NEWS_VERBOSE_NAME = 'Новость'
NEWS_VERBOSE_NAME_PLURAL = 'Новости'

# title
NEWS_TITLE = TITLE
NEWS_KEY_TITLE = 'Заголовок новости'
NEWS_KEY_TITLE_HELP_TEXT = ''

# text
NEWS_TEXT = TEXT
NEWS_KEY_TEXT = 'Текст новости'
NEWS_KEY_TEXT_HELP_TEXT = ARTICLE_KEY_TEXT_HELP_TEXT

# created
NEWS_CREATED = CREATED
NEWS_KEY_CREATED = CREATED_KEY
NEWS_KEY_CREATED_HELP_TEXT = ''

# updated
NEWS_UPDATED = UPDATED
NEWS_KEY_UPDATED = UPDATED_KEY
NEWS_KEY_UPDATED_HELP_TEXT = ''

# show
NEWS_SHOW = SHOW
NEWS_KEY_SHOW = 'Показывать новость'
NEWS_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть. ' \
                           'Скрытые статьи доступны для персонала на сайте.'

# important
NEWS_IMPORTANT = 'important'
NEWS_KEY_IMPORTANT = 'Важная новость'
NEWS_KEY_IMPORTANT_HELP_TEXT = 'Последняя новость закрепляется на главной. ' \
                               'В ленте новостей новость занимает все ширину. ' \
                               'Внимательно проследите и настройте позицию по вертикали ' \
                               'для корректного отображения новости.'
# y_pos
NEWS_Y_POS = Y_POS
NEWS_KEY_Y_POS = KEY_Y_POS
NEWS_KEY_Y_POS_HELP_TEXT = KEY_Y_POS_HELP_TEXT

# use_background
NEWS_USE_BACKGROUND = USE_BACKGROUND
NEWS_KEY_USE_BACKGROUND = KEY_USE_BACKGROUND
NEWS_KEY_USE_BACKGROUND_HELP_TEXT = KEY_USE_BACKGROUND_HELP_TEXT

# author
NEWS_AUTHOR = AUTHOR
NEWS_KEY_AUTHOR_HELP_TEXT = 'Выберите автора'
