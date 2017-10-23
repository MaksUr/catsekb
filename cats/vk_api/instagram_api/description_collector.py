# https://api.instagram.com/oauth/authorize/?client_id=69bf1df965de4745a3a587d03c725979&redirect_uri=http://127.0.0.1:8000/&response_type=code

# token = http://127.0.0.1:8000/?code=e78abce18de74188ae8d56fa644e3e17

from requests import get

from cats.vk_api.helper_functions import save_json

API_KEY = "f5208a30388245c1890b0e27991c9642"


def get_data_from_tag(tag_name):
    data = get(
        # r"https://api.instagram.com/v1/tags/{tag_name}/media/recent?access_token={token}".format(
        "https://api.instagram.com/v1/users/self/media/recent/?access_token={token}".format(
            # tag_name=tag_name,
            token=API_KEY
        )
    ).json()
    return data


def main():
    tag = 'пристроен_catsekb'
    d = get_data_from_tag(tag_name=tag)
    save_json('result', d)


if __name__ == '__main__':
    main()
