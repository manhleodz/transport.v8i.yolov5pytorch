import os

# Đường dẫn tới thư mục chứa labels
labels_dir = "test/labels"

# Quét qua tất cả các file trong thư mục labels
for filename in os.listdir(labels_dir):
    file_path = os.path.join(labels_dir, filename)
    
    # Kiểm tra nếu file là .txt
    if filename.endswith(".txt"):
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Tăng ID của từng class lên 1
        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 0:
                # Tăng ID (phần tử đầu tiên trong mỗi dòng) lên 1
                parts[0] = str(int(parts[0]) + 1)
                updated_lines.append(" ".join(parts))
        
        # Ghi lại nội dung vào file
        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines))
