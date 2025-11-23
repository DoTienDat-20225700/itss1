# ✅ **Yêu cầu trước khi chạy**

* Cài **Python 3.8+** và **pip**.
* Cài **Tesseract OCR** vào máy và ghi nhớ đường dẫn cài đặt (Windows mặc định đã được dùng trong code).

---

# ✅ **Cài đặt các thư viện Python**

pip install -r requirement.txt
---

# ✅ **Cấu hình Tesseract**

Trong project, đường dẫn Tesseract được đặt trong nhiều file.

Bạn cần kiểm tra và cập nhật nếu đường dẫn khác:

* `main.py`
* `test_ocr.py`
* `test_worker.py`

Các file này đặt:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


→ Nếu bạn cài Tesseract ở nơi khác, hãy đổi đường dẫn cho đúng.




Chạy file **main.py** trong môi trường venv




