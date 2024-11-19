# SCT_ML_4  

## Project Title:  
**Hand Gesture Recognition with CNNs**

---

## Project Description:  
This project implements a Convolutional Neural Network (CNN) to classify hand gestures into 11 categories using the LeapGestRecog dataset. The objective was to preprocess the dataset, train a CNN model, and evaluate its performance while identifying potential areas for improvement.

---

## Dataset:  
The dataset used for this project is the **LeapGestRecog** dataset, which contains over 20,000 images of hand gestures in grayscale.  
You can download the dataset here: [LeapGestRecog Dataset](https://www.kaggle.com/kmader/leapgestrecog).  

---

## Requirements:  
The following libraries and tools are required to run this project:  
- Python 3.7 or above  
- TensorFlow  
- NumPy  
- OpenCV  
- matplotlib  

To install the dependencies, use:  
```bash
pip install -r requirements.txt
```

---

## Steps to Reproduce:  
Follow these steps to run the project locally:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/RajeevRayagada/SCT_ML_4.git
   cd SCT_ML_4
   ```

2. Install the required Python libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset:  
   - Visit [LeapGestRecog Dataset](https://www.kaggle.com/kmader/leapgestrecog).  
   - Download the dataset and extract it to a folder (e.g., `data/`).

4. Update the dataset path in the `Hand_Gesture_Recognition.ipynb` file:  
   Modify the `data_path` variable to point to your dataset folder.  

5. Run the Jupyter Notebook:  
   ```bash
   jupyter notebook Hand_Gesture_Recognition.ipynb
   ```

6. Follow the steps in the notebook to preprocess the dataset, train the CNN model, and evaluate its performance.

---

## Results:  

### **Key Metrics**:  
- **Training Accuracy**: 85%  
- **Validation Accuracy**: ~10%  

The low validation accuracy indicates overfitting and highlights the need for further optimization.

### **Training vs. Validation Accuracy Plot**:  
![Accuracy Plot](https://github.com/RajeevRayagada/SCT_ML_4/blob/main/Training%20and%20Validation%20accuracy.png)

---

## Conclusion:  
This project demonstrates the challenges of training a CNN model on complex datasets and the importance of regularization, data augmentation, and architecture optimization. Future iterations will address these challenges with advanced techniques like dropout, learning rate scheduling, and fine-tuning.
