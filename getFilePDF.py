from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def text_to_pdf(txt_folder, output_pdf):
    # Tạo một đối tượng canvas để ghi PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    y = height - 1.5 * inch  # Vị trí y bắt đầu từ trên cùng của trang

    # Đăng ký font hỗ trợ Unicode
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'Dejavu\\DejaVuSans.ttf'))

    # Sử dụng font mới
    c.setFont('DejaVuSans', 12)
    
    # Lấy danh sách các file .txt và sắp xếp theo thứ tự
    txt_files = sorted([f for f in os.listdir(txt_folder) if f.endswith('.txt')])
    
    for txt_file in txt_files:
        file_path = os.path.join(txt_folder, txt_file)

        # Đọc nội dung từ file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Thêm tiêu đề cho từng file
        title = txt_file.replace('.txt', '').replace('_', ' ').title()
        c.setFont('DejaVuSans', 14)
        c.drawString(1 * inch, y, title)
        y -= 0.5 * inch
        
        # Thêm nội dung file vào PDF
        c.setFont('DejaVuSans', 12)
        for line in lines:
            words = line.strip().split()
            line_width = 0
            current_line = []
            
            for word in words:
                word_width = c.stringWidth(word + ' ', 'DejaVuSans', 12)
                if line_width + word_width > width - 2 * inch:
                    c.drawString(1 * inch, y, ' '.join(current_line))
                    y -= 0.25 * inch
                    if y < 1 * inch:  # Nếu không còn đủ chỗ trên trang, thêm trang mới
                        c.showPage()
                        c.setFont('DejaVuSans', 12)
                        y = height - 1.5 * inch
                    current_line = []
                    line_width = 0
                current_line.append(word)
                line_width += word_width

            if current_line:
                c.drawString(1 * inch, y, ' '.join(current_line))
                y -= 0.25 * inch
        
        # Đảm bảo không bỏ sót bất kỳ trang nào
        if y < 1 * inch:
            c.showPage()
            y = height - 1.5 * inch
    
    # Lưu PDF
    c.save()
    print(f'File PDF đã được lưu vào {output_pdf}')

if __name__ == '__main__':
    txt_folder = 'chapters'  # Thư mục chứa các file .txt
    output_pdf = 'cuon_truyen.pdf'  # Tên file PDF đầu ra
    text_to_pdf(txt_folder, output_pdf)
