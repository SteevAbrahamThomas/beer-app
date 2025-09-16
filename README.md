# 🍺 Alcohol Consumption Predictor  

A simple **Streamlit web app** that predicts the **total litres of pure alcohol consumed per person per year** based on beer, spirit, and wine servings.  

This project uses:  
- **Python 3.8+**  
- **scikit-learn** (Linear Regression model)  
- **Streamlit** (for UI)  
- **pandas**  

---

## 📂 Project Structure
```
beer-app/
│── app.py                # Streamlit web app
│── train_model.py        # Script to train and save the ML model
│── beer-servings.csv     # Dataset (global alcohol consumption data)
│── model.pkl             # Trained regression model
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## 🚀 Features
- Interactive **web UI** built with Streamlit.  
- Accepts **Beer servings, Spirit servings, Wine servings** as user input.  
- Predicts **total litres of pure alcohol** consumed.  
- Deployable on **Streamlit Cloud** with one click.  

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/beer-app.git
cd beer-app
```

### 2. Create a virtual environment
#### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model (creates `model.pkl`)
```bash
python train_model.py
```

### 5. Run the Streamlit app
```bash
streamlit run app.py
```

Now open 👉 [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deployment on Streamlit Cloud
1. Push this repo to **GitHub**.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in with GitHub.  
3. Create a **New app**, select your repo and `app.py` as the entry point.  
4. Deploy 🚀.  
5. Share your public app URL (e.g. `https://your-username-beer-app.streamlit.app`).  

---

## 📊 Dataset
The dataset used (`beer-servings.csv`) contains:  
- **beer_servings** 🍺  
- **spirit_servings** 🥃  
- **wine_servings** 🍷  
- **total_litres_of_pure_alcohol** 🍶  
- Country & continent data  
---

## 👨‍💻 Author
Made with ❤️ using **Python + Streamlit**  
