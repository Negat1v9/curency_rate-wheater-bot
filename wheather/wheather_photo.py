from .utilits import photourl


def get_photo_url(iconid: str) -> str:
    #url to get photo
    url = f"{photourl[0]}{iconid}{photourl[1]}"
    return url

    
    