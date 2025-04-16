# Comparative Analysis of YOLOv10n and YOLOv11n for Brain Tumor Detection

This repository contains the project for comparing the performance of YOLOv10n and YOLOv11n models for detecting brain tumors using MRI images. The study evaluates both models based on standard metrics to determine detection accuracy and localization precision.

## Dataset

- **Description:**  
  The dataset comprises annotated MRI images featuring various brain tumor types.
  
- **Details:**  
  - **Training Set:** 878 images (including 15 background images)  
  - **Validation Set:** 223 images  
  - **Validation Breakdown:**  
    - All: 223 images, 241 instances  
    - Negative: 142 images, 154 instances  
    - Positive: 81 images, 87 instances  

## Models and Training

- **YOLOv10n:**  
  A lightweight model optimized for real-time performance.

- **YOLOv11n:**  
  An improved version featuring a fused architecture with 100 layers, 2,582,542 parameters, and 6.3 GFLOPs. It is designed for better convergence and higher detection accuracy.

- **Training Setup:**  
  Both models were trained for 50 epochs on Google Colab using a Tensor T4 GPU. Standard data augmentation techniques were applied to improve model robustness.

## Evaluation Metrics

The models were evaluated using the following metrics:

- **mAP@0.5:** Mean Average Precision at an IoU threshold of 0.5.
- **mAP@0.5–0.95:** Mean Average Precision averaged over IoU thresholds from 0.5 to 0.95 (in steps of 0.05).
- **Precision (All):** Ratio of correctly predicted objects (true positives) to all predicted objects.
- **Recall (All):** Ratio of correctly predicted objects to the total number of actual objects.

## Results

The performance metrics on the validation set are summarized in the table below:

| Model     | mAP@0.5 | mAP@0.5–95 | Precision (All) | Recall (All) |
|-----------|---------|------------|-----------------|--------------|
| YOLOv10n  | 0.443   | 0.324      | 0.425           | 0.859        |
| YOLOv11n  | 0.457   | 0.338      | 0.419           | 0.858        |

*Note: YOLOv11n shows a slight improvement in mAP metrics, indicating better overall detection quality.*

## Conclusion

This comparative analysis indicates that while both YOLOv10n and YOLOv11n achieve high recall, YOLOv11n demonstrates marginal improvements in mAP values. These results highlight the benefits of model enhancements for improving precision and localization in brain tumor detection using deep learning.

## Future Work

- Expand the dataset for better generalization.
- Optimize hyperparameters and experiment with advanced data augmentation techniques.
- Explore integration with clinical decision-support systems.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For further information or collaboration inquiries, please contact [Your Name] at [Your Email].
