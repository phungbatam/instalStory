import requests
from bs4 import BeautifulSoup
import os

def download_chapter(url, chapter_number, output_folder):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tìm phần tử chứa nội dung chương
        content = soup.find('div', class_='content')  # Thay đổi phần tử và class nếu cần
        
        if content:
            chapter_text = content.get_text()
            file_path = os.path.join(output_folder, f'chuong_{chapter_number}.txt')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(chapter_text)
            print(f'Đã tải chương {chapter_number} và lưu vào {file_path}')
        else:
            print(f'Không tìm thấy nội dung cho chương {chapter_number}')
    else:
        print(f"Không thể tải chương {chapter_number}, mã lỗi: {response.status_code}")

def main():
    base_url = 'https://sstruyen.vn/em-la-tieu-tien-nu-cua-anh/chuong-'  # URL mẫu của các chương
    output_folder = 'chapters'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    start_chapter = 1
    end_chapter = 75  # Bạn có thể thay đổi phạm vi này theo số lượng chương bạn muốn tải
    
    for chapter_number in range(start_chapter, end_chapter + 1):
        chapter_url = f'{base_url}{chapter_number}/reading/'
        download_chapter(chapter_url, chapter_number, output_folder)

if __name__ == '__main__':
    main()
