import gradio as gr
from ultralytics import YOLO
from PIL import Image
import torch

yolo10n = YOLO(r"C:\Users\Dhruv\Downloads\yolov10n-results (2)\content\runs\detect\train\weights\best.pt")  
yolo11n = YOLO(r"c:\Users\Dhruv\Downloads\yolo11nResults\content\runs\detect\train\weights\best.pt")  


def detect_tumor(image, model_choice):
    model = yolo10n if model_choice == "YOLOv10n" else yolo11n
    results = model(image)
    rendered_image = results[0].plot()
    print(results)
    return Image.fromarray(rendered_image)

iface = gr.Interface(
    fn=detect_tumor,
    inputs=[
        gr.Image(type="pil", label="Upload Brain MRI Image"),
        gr.Radio(["YOLOv10n", "YOLOv11n"], label="Select Model", value="YOLOv11n")
    ],
    outputs=gr.Image(type="pil", label="Detected Tumor Output"),
    title="Brain Tumor Detection using YOLO",
    description="Upload a brain MRI image and choose between YOLOv10n or YOLOv11n to detect brain tumors."
)

iface.launch()