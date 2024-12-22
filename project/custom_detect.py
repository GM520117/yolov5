import torch
from pathlib import Path

# 設定模型權重的路徑
model_path = r'C:/Users/owner/Downloads/Yolov5/yolov5/runs/train/exp2\weights\best.pt'

# 檢查權重檔案是否存在
if not Path(model_path).exists():
    raise FileNotFoundError(f"模型權重檔案未找到：{model_path}")

# 載入 YOLOv5 模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

# 設定來源與結果的路徑
source_folder = r'C:/Users/owner/Downloads/Yolov5/yolov5/project/images'
output_folder = r'C:/Users/owner/Downloads/Yolov5/yolov5/project/results'

# 執行檢測
results = model(source_folder)

# 保存結果
results.save(save_dir=output_folder)

print(f"影像辨識完成！結果已儲存至：{output_folder}")
