# Dự án Astar & Xử lý ảnh

## Tổng quan
Dự án này chứa hai phần chính: thuật toán tìm đường A* và xử lý ảnh. Thư mục báo cáo chứa tài liệu kết quả, mã nguồn nằm trong thư mục `ChuongTrinh`.

## Cấu trúc thư mục
- BaoCao/: chứa báo cáo, biểu đồ, hoặc tài liệu liên quan.
- ChuongTrinh/: mã nguồn chính
  - `Astar.py`: triển khai thuật toán A* để tìm đường ngắn nhất.
  - `Image_Processing.py`: các hàm xử lý ảnh (tiền xử lý, lọc, v.v.).
  - `Main.py`: điểm chạy chính (entry point) để chạy/kiểm tra các chức năng.

## Yêu cầu
- Python 3.8 hoặc mới hơn
- Các thư viện Python thông dụng (nếu cần): `numpy`, `opencv-python`, `matplotlib`.

Bạn có thể cài nhanh các phụ thuộc bằng cách tạo file `requirements.txt` (nếu chưa có) rồi chạy:

```bash
python -m pip install -r requirements.txt
```

Nếu không có `requirements.txt`, cài thủ công ví dụ:

```bash
python -m pip install numpy opencv-python matplotlib
```

## Cách chạy
1. Mở terminal ở thư mục gốc của dự án.
2. Chạy ứng dụng chính (Windows):

```powershell
python ChuongTrinh\\Main.py
```

Hoặc (POSIX):

```bash
python ChuongTrinh/Main.py
```

`Main.py` có thể chứa các ví dụ chạy A* hoặc các pipeline xử lý ảnh. Mở file để xem các tham số đầu vào và cách cấu hình.

## Ghi chú cho Windows
- Dùng `python` hoặc `py` tùy theo thiết lập hệ thống.
- Đường dẫn tới file trong Windows có thể dùng dấu `\\` như ví dụ trên.

## Đóng góp
- Mở issue nếu gặp lỗi hoặc muốn đề xuất tính năng.
- Gửi pull request kèm mô tả và ví dụ tái hiện lỗi (nếu có).

## License
Chưa có license cụ thể trong repository — nếu bạn muốn, hãy thêm file `LICENSE` (ví dụ MIT).

---
Nếu bạn muốn, tôi có thể: tạo `requirements.txt` tự động, kiểm tra/ chỉnh `Main.py` để thêm hướng dẫn chạy, hoặc commit & push file này lên remote. Tôi sẽ tiếp tục commit và push ngay nếu bạn cho phép.
