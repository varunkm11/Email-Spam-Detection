# 📧 Email Spam Detection App

A **machine learning web app** built with **Streamlit** that classifies text messages as **Spam** or **Not Spam** using a **Naive Bayes classifier** trained on SMS data. It uses the **Bag of Words model** for text vectorization with `CountVectorizer`.

---

## 🔗 Live Demo

🌐 [Try it on Streamlit](https://email-spam-detection-jlwpvvfqympjvniulugcku.streamlit.app/)  

---

## 🖼️ App Preview

Enter a message and click **Validate** to classify it as Spam or Not Spam.

---

## 📁 Files in the Repository
spam-detection-app/
├── app.py               # Main Streamlit app code
├── spam.csv             # Dataset (SMS messages and labels)
├── requirements.txt     # All required Python packages
└── README.md            # Project documentation

---

## 📊 Dataset

The dataset used is a collection of SMS messages labeled as either:
- `ham` → renamed to `Not Spam`
- `spam` → renamed to `Spam`

> Make sure your `spam.csv` file includes at least two columns: `Category`, and `Message`.

---

## ⚙️ How It Works

- **Data Cleaning**: Removes duplicates
- **Feature Extraction**: Uses `CountVectorizer` to convert text into numerical features
- **Model**: Trains a `Multinomial Naive Bayes` classifier
- **Evaluation**: Displays test accuracy
- **Prediction**: Takes user input and classifies it in real-time

---

## 💻 Installation & Usage

### 🔸 1. Clone the repository

```bash
git clone https://github.com/your-username/spam-detection-app.git
cd spam-detection-app
```
### 🔸 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 🔸 3. Run the Streamlit app in VS Code
```bash
streamlit run app.py
```
### 🙌 Contributions
Feel free to contribute to improve the model, UI, or data. Pull requests are welcome!
### 🔗 Author
👤 [varunkm11](https://github.com/varunkm11)

