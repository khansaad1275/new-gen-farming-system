from transformers import AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch
import os


# Load the model and image processor
model_name = "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"
model = AutoModelForImageClassification.from_pretrained(model_name)
image_processor = AutoImageProcessor.from_pretrained(model_name)

# Define class labels for wheat and rice
class_labels = [
    "Healthy Wheat", "Wheat Rust - Leaf Rust", "Wheat Rust - Stem Rust", 
    "Wheat Rust - Stripe Rust", "Wheat Blight", "Wheat Powdery Mildew",
    "Wheat Yellow Rust", "Wheat Septoria Leaf Blotch", "Wheat Fusarium Head Blight",
    "Wheat Ergot", "Wheat Brown Rust", "Wheat Leaf Spot",
    "Healthy Rice", "Rice Blast", "Rice Brown Spot", "Rice Sheath Blight",
    "Rice Leaf Blast", "Rice Leaf Scald", "Rice Bacterial Blight",
    "Rice Stem Rot", "Rice Tungro Virus", "Rice Grain Discoloration"
]

def classify_image(img_path):
    try:
        # Load and preprocess the image
        img = Image.open(img_path)
        inputs = image_processor(images=img, return_tensors="pt")

        # Make predictions
        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        predicted_class = probabilities.argmax().item()

        # Check if predicted_class is within the range of class_labels
        if predicted_class < len(class_labels):
            predicted_label = class_labels[predicted_class]
        else:
            predicted_label = "No disease found"  # Handle out-of-range predictions
            print(f"{predicted_label}")

        return predicted_label, probabilities[0][predicted_class].item()

    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return "Error", 0.0

# Assuming classify_image and class_labels are defined earlier in your script
image_folder = 'images/'

for image_name in os.listdir(image_folder):
    if image_name.endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(image_folder, image_name)
        
        # Debugging: Print image path
        print(f"\nProcessing {img_path}...")
        
        predicted_label, confidence = classify_image(img_path)
        
        # Debugging: Print predicted label
        print(f"{image_name}: Predicted disease: {predicted_label}")
