# services/inference_service.py
import torch
import torchvision.transforms as T
from PIL import Image
import asyncio

# Load model once at import
MODEL_PATH = "./models/resnet18.pth"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# For demo, use pretrained resnet18
model = torch.hub.load("pytorch/vision", "resnet18", pretrained=True)
model.eval()
model.to(DEVICE)

transform = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Dummy labels for ImageNet
LABELS = ["label_{}".format(i) for i in range(1000)]

async def run_inference(image_path: str):
    # Simulate async I/O
    await asyncio.sleep(0)
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(input_tensor)
    probs = torch.nn.functional.softmax(outputs[0], dim=0)
    top5 = torch.topk(probs, 5)
    results = []
    for idx, score in zip(top5.indices, top5.values):
        results.append({"label": LABELS[idx], "confidence": float(score)})
    return results
