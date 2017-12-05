DJ_ID = 'id'

# URLs
URL_NAME_SUBJECTS = 'subjects'
URL_NAME_SUBJECT = 'subject'
URL_NAME_ARTICLE = 'article'
URL_NAME_CONTACTS = 'contacts'
URL_NAME_FIND_CAT = 'find_cat'

APPLICATION_VERBOSE_NAME = 'Статьи'

# class Author
AUTHOR_VERBOSE_NAME = 'Автор'
AUTHOR_VERBOSE_NAME_PLURAL = 'Авторы'

# name
AUTHOR_NAME = 'name'
AUTHOR_KEY_NAME = 'Автор'
AUTHOR_KEY_NAME_HELP_TEXT = ''


# class Subject
SUBJECT_VERBOSE_NAME = 'Тема'
SUBJECT_VERBOSE_NAME_PLURAL = 'Темы'

# name
SUBJECT_NAME = 'name'
SUBJECT_KEY_NAME = SUBJECT_VERBOSE_NAME
SUBJECT_KEY_NAME_HELP_TEXT = 'Укажи тематику статьи'


# class Article
ARTICLE_VERBOSE_NAME = 'Статья'
ARTICLE_VERBOSE_NAME_PLURAL = APPLICATION_VERBOSE_NAME

# title
ARTICLE_TITLE = 'title'
ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE = '"{title}" имеет недопустимое значение.'
ARTICLE_KEY_TITLE = 'Название статьи'
ARTICLE_KEY_TITLE_HELP_TEXT = ''

# text
ARTICLE_TEXT = 'text'
ARTICLE_KEY_TEXT = 'Текст статьи'
ARTICLE_KEY_TEXT_HELP_TEXT = 'Используйте html теги: <p> <a> <img> для форматирования текста.'

# created
ARTICLE_CREATED = 'created'
ARTICLE_KEY_CREATED = 'Создано'
ARTICLE_KEY_CREATED_HELP_TEXT = ''

# updated
ARTICLE_UPDATED = 'updated'
ARTICLE_KEY_UPDATED = 'Обновлено'
ARTICLE_KEY_UPDATED_HELP_TEXT = ''

# show
ARTICLE_SHOW = 'show'
ARTICLE_KEY_SHOW = 'Показывать статью'
ARTICLE_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть. ' \
                           'Скрытые статьи доступны для персонала на сайте.'
# author
ARTICLE_AUTHOR = 'author'

# subject
ARTICLE_SUBJECT = 'subject'

# Article instances
ARTICLE_CONTACTS_ID = 1
ARTICLE_FIND_CAT_ID = 2

ARTICLES_DEFAULT = {
    ARTICLE_CONTACTS_ID: 'Контакты',
    ARTICLE_FIND_CAT_ID: 'Что делать я нашел кота',
}
