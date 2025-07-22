import sys
import os
import logging
import time
import datetime
from src.data.model.unsplash_data import UnsplashPhoto
from src.utils.json_helper import parse_json
from src.data.remote.api_requests import *
from src.utils.log_helper import Log
from collections import defaultdict, Counter, deque
import heapq
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import DEBUG, API_URL, API_PHOTOS

# print(f"sys.path: {sys.path}")
print(f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")

filename = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
# logger = logging.getLogger('test')
# logger.setLevel(logging.DEBUG)
# logging.Formatter.default_msec_format = '%s.%03d'

# # file log
# file_handler = logging.FileHandler(f'{filename}.log', mode='w')
# formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s | [%(funcName)s() - %(lineno)d]: %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# # console log
# console_handler = logging.StreamHandler()
# console_formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s |[%(funcName)s() - %(lineno)d]: %(message)s') # Include filename and name
# console_handler.setFormatter(console_formatter)
# logger.addHandler(console_handler)

class MyClass:
    def my_method(self):
        Log.d(__name__, 'This is a debug message.')
        Log.i(__name__,'This is an info message.')
        Log.w(__name__,'This is a warning message.')
        Log.e(__name__,'This is an error message.')
        Log.c(__name__, 'This is a critical message.')

def main(*args):
    print("Debug mode:", DEBUG)
    print("API URL:", API_URL)
    print("API PHOTOS:", API_PHOTOS)
    return
    Log.initialize(logging.DEBUG)
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("SDET interview questions")
    search_box.send_keys(Keys.RETURN)

    assert "SDET" in driver.title
    input("Press Enter to close the browser and exit...")
    # driver.quit()
    try:
        photos = get_photos(per_page=10)
        print(f"1th photo: {photos[0]}")

        # 記錄日誌訊息
        Log.d(__name__, 'This is a debug message.')
        Log.i(__name__,'This is an info message.')
        Log.w(__name__,'This is a warning message.')
        Log.e(__name__,'This is an error message.')
        Log.c(__name__, 'This is a critical message.')
        my_object = MyClass()
        my_object.my_method()

    except (TypeError, ValueError) as e:
        print(f"Error parsing JSON: {e}")

    # test = "python3 test"
    # print(f'{test}')
    # charIndex = [-1] * 128
    # print(f"charIndex: {charIndex}")
    # s = "abc"
    # s = '#'.join(s)
    # print(f's: {s}')
    # dp = [0 for _ in range(len(s))]
    # print(f"dp: {dp}")

if __name__ == "__main__":
    print(f"{__name__}")
    main()
