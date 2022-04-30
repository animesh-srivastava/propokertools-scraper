import requests
from bs4 import BeautifulSoup
import time
import os
from PIL import Image


headers = {
    "Host": "www.propokertools.com",
    "Connection": "keep-alive",
    "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "X-Prototype-Version": "1.6.0.3",
    "DNT": "1",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://www.propokertools.com",
    "Referer": "http://www.propokertools.com/pql",
    "Accept-Encoding": "gzip, deflate",
}

url = "http://www.propokertools.com/pql"
query_url = "http://www.propokertools.com/pql/execute_query"
timeout = 10


def _open_image(image_path) -> bool:
    """
    Open image from command line
    """
    img = Image.open(image_path)
    img.show()
    return True


def _check_connection() -> bool or Exception:
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        if resp.status_code == 200:
            return True
        else:
            return Exception("Error in connecting to the server. Status code: {}".format(resp.status_code))
    except:
        raise Exception("No connection to server. Check your internet")


def _make_request(query: str) -> bytes or int:
    """
    Make a request to the server
    """
    resp = requests.post(
        query_url,
        data={
            "query": query,
            "_": ""
        },
        headers=headers,
        timeout=timeout
    )
    if resp.status_code == 200:
        return resp.content
    return resp.status_code


def _save_image_from_url(url: str, filepath: str) -> bool:
    """
    Download and save image to a filepath from a url
    """
    try:
        resp = requests.get(url, stream=True, timeout=timeout)
        if resp.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in resp:
                    f.write(chunk)
            return True
        else:
            return False
    except:
        return False


def _parse_response(content: bytes) -> dict:
    """
    Parse the response from the server
    """
    soup = BeautifulSoup(content, 'html.parser')
    errors = soup.find("div", {"class": "error"})
    if errors is not None:
        return {"error": "".join(errors)}
    table = soup.find("table")
    keys = []
    for i, row in enumerate(table.findAll("th")):
        keys.append(row.text)
    ret_dict = {}
    for i, row in enumerate(table.findAll("td")):
        if row.text.strip():
            ret_dict[keys[i]] = row.text.strip()
        elif len(row.find_all('img')):
            if not os.path.isdir("images"):
                os.mkdir("images")
            for img in row.find_all('img'):
                # Save the image to a file and return the filepath to the saved image
                ret_dict[keys[i]] = \
                    "images/{}-{:0.5f}.png".format(keys[i], time.time())
                saved = _save_image_from_url(
                    img['src'], ret_dict[keys[i]])
                if not saved:
                    # If image is not saved, show None
                    ret_dict[keys[i]] = None
                    print("Error in saving image")
                else:
                    # Open image in image viewer
                    _open_image(ret_dict[keys[i]])
    return ret_dict
