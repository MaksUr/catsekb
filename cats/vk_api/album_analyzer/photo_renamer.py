from os import listdir, rename

from os.path import join, isfile

ALBUMS_PTH = join('media', 'images', 'cats', 'albums')


def rename_photo(p):
    if not isfile(p):
        print('ERROR! photo ' + p + ' not exist')
    elif not p.endswith('.jpg'):
        rename(p, p+'.jpg')
        print('rename', p, '[.jpg]')
    else:
        print('Уже переименован:', p)


def get_photos(alb_pth):
    current_path = join(ALBUMS_PTH, alb_pth, 'photos')
    res = [join(current_path, file_pth) for file_pth in listdir(current_path)]
    return res


def main():
    albums = listdir(ALBUMS_PTH)
    i = 0
    for alb in albums:
        photos = get_photos(alb)
        for photo in photos:
            rename_photo(photo)
            i += 1
    print('rename', i, 'photos')

if __name__ == '__main__':
    main()





