

from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
app = Flask(__name__)

# Load the trained model
model = load_model(r'G:\project\MIni Project\pythonProject\Medicinal_Plant.h5')

# Class labels
class_labels = ["Aloevera", "Amla", "Amruta_Balli", "Arali", "Ashoka", "Ashwagandha", "Avocado", "Bamboo", "Basale",
                "Betel",
                "Betel_Nut", "Brahmi", "Castor", "Curry_Leaf", "Doddapatre", "Ekka", "Ganike", "Guava", "Geranium",
                "Henna",
                "Hibiscus", "Honge", "Insulin", "Jasmine", "Lemon", "Lemon_grass", "Mango", "Mint", "Nagadali", "Neem",
                "Nithyapushpa", "Nooni", "Pappaya", "Pepper", "Pomegranate", "Raktachandini", "Rose", "Sapota",
                "Tulasi", "Wood_sorel"]

# Define the path to the uploads directory
uploads_dir = os.path.join(app.root_path, 'static/uploads')

# Ensure the uploads directory exists
os.makedirs(uploads_dir, exist_ok=True)



methods_of_preparation = {
    "Aloevera": "Slit the leaf of an aloe plant lengthwise and remove the gel from the inside, or use a commercial preparation.",
    "Amla": "Eating raw amla and candies or taking amla powder with lukewarm water",
    "Amruta_Balli": "Make a decoction or powder from the stems of Giloy. It is known for its immunomodulatory properties.",
    "Arali": "Various parts like the root bark, leaves, and fruit are used for medicinal purposes. It can be consumed in different forms, including as a decoction. Different parts like the bark are used. It's often prepared as a decoction for menstrual and uterine health. The root is commonly used, and it can be consumed as a powder, capsule, or as a decoction. It is an adaptogen known for its stress-relieving properties. The fruit is consumed for its nutritional benefits, including healthy fats and vitamins.",
    "Ashoka": "Different parts like the bark are used. It's often prepared as a decoction for menstrual and uterine health.",
    "Ashwagandha": "The root is commonly used, and it can be consumed as a powder, capsule, or as a decoction. It is an adaptogen known for its stress-relieving properties.",
    "Avocado": "The fruit is consumed for its nutritional benefits, including healthy fats and vitamins.",
    "Bamboo": "Bamboo shoots are consumed, and some varieties are used in traditional medicine.",
    "Basale": "The leaves are consumed as a leafy vegetable. It's rich in vitamins and minerals.",
    "Betel": "Chewing betel leaves with areca nut is a common practice in some cultures. It's believed to have digestive and stimulant properties.",
    "Betel_Nut": "The nut is often chewed with betel leaves. However, excessive consumption is associated with health risks.",
    "Brahmi": "The leaves are used for enhancing cognitive function. It can be consumed as a powder, in capsules, or as a fresh juice.",
    "Castor": "Castor oil is extracted from the seeds and used for various medicinal and cosmetic purposes.",
    "Curry_Leaf": "Curry leaves are used in cooking for flavor, and they are also consumed for their potential health benefits.",
    "Doddapatre": "The leaves are used in traditional medicine, often as a poultice for skin conditions.",
    "Ekka": "Various parts may be used in traditional medicine. It's important to note that some species of Ekka may have toxic components, and proper identification is crucial.",
    "Ganike": "The leaves are used in traditional medicine, often as a remedy for respiratory issues.",
    "Guava": "Guava fruit is consumed for its high vitamin C content and other health benefits.",
    "Geranium": "Geranium oil is extracted from the leaves and stems and is used in aromatherapy and skincare.",
    "Henna": "Henna leaves are dried and powdered to make a paste used for hair coloring and as a natural dye.",
    "Hibiscus": "Hibiscus flowers are commonly used to make teas, infusions, or extracts. They are rich in antioxidants and can be beneficial for skin and hair health.",
    "Honge": "Various parts of the tree are used traditionally, including the bark and seeds. It's often used for its anti-inflammatory properties.",
    "Insulin": "The leaves are used for their potential blood sugar-lowering properties. They can be consumed fresh or as a tea.",
    "Jasmine": "Jasmine flowers are often used to make aromatic teas or essential oils, known for their calming effects.",
    "Lemon": "Lemon juice is a common remedy for digestive issues, and the fruit is rich in vitamin C. The peel can be used for its essential oil.",
    "Lemon_grass": "Lemon grass is used to make teas and infusions, known for its soothing and digestive properties.",
    "Mango": "Mango fruit is consumed fresh and is rich in vitamins and minerals. Some parts, like the leaves, are also used in traditional medicine.",
    "Mint": "Mint leaves are commonly used to make teas, infusions, or added to dishes for flavor. It's known for its digestive properties.",
    "Nagadali": "Different parts of the plant are used traditionally. It's often prepared as a decoction.",
    "Neem": "Various parts of the neem tree are used, including leaves, bark, and oil. It's known for its antibacterial and antifungal properties.",
    "Nithyapushpa": "The flowers are used in traditional medicine, often for their calming effects.",
    "Nooni": "Different parts of the tree are used traditionally. The oil extracted from the seeds is used for various purposes.",
    "Pappaya": " Consume fruit; leaves traditionally used for certain health benefits.",
    "Pepper": "Spice for flavor; potential digestive and antimicrobial properties.",
    "Pomegranate": "Eat seeds or drink juice for antioxidant benefits.",
    "Raktachandini": "Traditional uses; some parts may be toxic, use caution.",
    "Rose": " Make tea or use petals for calming and aromatic effects.",
    "Sapota": "Consume fruit for its sweet taste and nutritional content.",
    "Tulasi": "Make tea or use leaves for immune support.",
    "Wood_sorel": "Make tea or use leaves for immune support. Use leaves in salads; some varieties contain oxalic acid."
}



use_of_medicine={"Aloevera":"{improve skin and prevent wrinkles,wound healing}",
                 "Amla":"{controlling diabetes,hair amazing,losing weight,skin healthy}",
                 "Amruta_Balli":"{Immunomodulatory, fever.}",
                 "Arali":"{ parts for traditional healing.}",
                 "Ashoka":"{Uterine health, menstrual issue.}",
                 "Ashwagandha": "{Adaptogen, stress relief.}",
                 "Avocado":"{ Nutrient-rich, heart health.}",
                 "Bamboo":"{Shoots, traditional cuisine.}",
                 "Basale":"{Shoots, traditional cuisine.}",
                 "Betel":"{Digestive, chewed with areca nut.}",
                 "Betel_Nut":"{Chewing, traditional practices, caution.}",
                 "Brahmi":"{Cognitive enhancer, adaptogen}",
                 "Castor": "{ Oil for medicinal, cosmetic use}",
                 "Curry_Leaf":"{ Flavoring, potential traditional uses.}",
                 "Doddapatre":"{ Poultice, skin conditions.}",
                 "Ekka":"{Traditional uses, caution for toxicity.}",
                 "Ganike":"{Respiratory health, traditional medicine.}",
                 "Guava": "{ Vitamin C, digestive benefits}",
                 "Geranium":"{ Oil for aromatherapy, skincare.}",
                 "Henna": "{ Hair coloring, natural dye.}",
                 "Hibiscus":"{Tea for antioxidants, skin health.}",
                 "Honge":"{Anti-inflammatory, traditional use.}",
                 "Insulin":"{Potential blood sugar regulation, traditional use.}",
                 "Jasmine":"{Tea, relaxation, stress relief.}",
                 "Lemon":"{Digestive aid, rich in vitamin C.}",
                 "Lemon_grass":"{Tea, digestive, calming effects.}",
                 "Mango":"{Fruit, traditional uses for health.}",
                 "Mint": "{Tea, aids digestion, refreshing flavor.}",
                 "Nagadali":"{Traditional uses, potential medicinal purposes.}",
                 "Neem":"{ Antibacterial, antifungal, supports skin health.}",
                 "Nithyapushpa": "{Calming effects, traditional use.}",
                 "Nooni":"{ Oil from seeds, various traditional uses.}",
                 "Pappaya": "{ Fruit, leaves, traditional uses.}",
                 "Pepper":"{ Spice, potential digestive benefits.}",
                 "Pomegranate": "{Antioxidant-rich, heart health.}",
                 "Raktachandini":"{Traditional uses, caution for potential toxicity.}",
                 "Rose":"{Tea, calming, aromatic effects.}",
                 "Sapota":"{Sweet taste, nutritional content.}",
                 "Tulasi":"{Tea, immune support, respiratory health.}",
                 "Wood_sorel": "{Leaves in salads, some varieties may have medicinal uses.}"}


def predict_class(image_path):
    img = image.load_img(image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    return predicted_class_label


@app.route('/', methods=['GET', 'POST'])
def index():
    file_path = None
    filename = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file:
            file_path = os.path.join(uploads_dir, file.filename)
            file.save(file_path)
            predicted_class = predict_class(file_path)
            preparation= methods_of_preparation.get(predicted_class,"no information")
            uses=use_of_medicine.get(predicted_class,"no information")
            return render_template('index.html', prediction=predicted_class, preparation=preparation,uses=uses, file_path=file_path,filename=filename)

    return render_template('index.html', file_path=file_path,filename=filename)


@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

