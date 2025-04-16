Comparative Analysis of YOLOv10n and YOLOv11n for Brain Tumor Detection
This project presents a comparative study of YOLOv10n and YOLOv11n models in detecting brain tumors using MRI images. The objective is to evaluate and contrast the performance of these two models on a brain tumor dataset.​

Dataset
The dataset comprises annotated MRI images of brain tumors, including various tumor types. It is sourced from publicly available datasets such as Br35H and Roboflow.​
PMC
+1
ScienceDirect
+1

Models and Training
YOLOv10n: A lightweight version of the YOLOv10 model.

YOLOv11n: An enhanced version with improved accuracy and efficiency.​
Nano NTP

Both models were trained for 50 epochs using Google Colab with a T4 GPU. The training process involved standard data augmentation techniques and utilized the default hyperparameters provided by the respective YOLO versions.​
ResearchGate

Evaluation Metrics
The models were evaluated using the following metrics:​

mAP@0.5: Mean Average Precision at an IoU threshold of 0.5.

mAP@0.5–0.95: Mean Average Precision averaged over IoU thresholds from 0.5 to 0.95 in steps of 0.05.

Precision: The ratio of true positive detections to the total number of positive predictions.

Recall: The ratio of true positive detections to the total number of actual positives in the dataset.​

Results
The performance metrics for both models are as follows:​


Model	mAP@0.5	mAP@0.5–0.95	Precision	Recall
YOLOv10n	0.443	0.324	0.425	0.859
YOLOv11n	0.457	0.338	0.419	0.858
The results indicate that YOLOv11n slightly outperforms YOLOv10n in terms of mAP metrics, suggesting better overall detection quality.​

Conclusion
The comparative analysis demonstrates that YOLOv11n offers marginal improvements over YOLOv10n in detecting brain tumors from MRI images. These findings can inform future research and development of more accurate and efficient models for medical image analysis.
