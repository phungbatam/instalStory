from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

def download_chapters(chapter_urls, output_dir):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy trình duyệt ở chế độ headless
    service = Service('C:\\webdrivers\\chromedriver.exe')  # Thay đổi đường dẫn đến chromedriver

    driver = webdriver.Chrome(service=service, options=chrome_options)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for index, url in enumerate(chapter_urls, start=1):
        try:
            driver.get(url)
            # Đợi cho nội dung được tải hoàn tất
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))  # Chờ cho phần tử body xuất hiện
            )

            # Lấy toàn bộ HTML của trang
            html = driver.page_source

            # Lưu nội dung vào file
            file_name = os.path.join(output_dir, f"chap{index}.html")
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(html)
            print(f"Đã lưu {file_name}")
        except Exception as e:
            print(f"Lỗi khi xử lý {url}: {e}")

    driver.quit()

# Danh sách các liên kết của các chương
chapter_urls = [
    'https://dtruyen.com/em-la-tieu-tien-nu-cua-anh/chuong-1_1701005.html',
    'https://dtruyen.com/em-la-tieu-tien-nu-cua-anh/chuong-2_1701006.html',
    'https://dtruyen.com/em-la-tieu-tien-nu-cua-anh/chuong-3_1701007.html',
]

output_dir = 'chapters'
download_chapters(chapter_urls, output_dir)
