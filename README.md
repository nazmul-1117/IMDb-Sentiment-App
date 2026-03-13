# IMDb-Sentiment-App 🎬

**IMDb-Sentiment-App** is a Streamlit web application that predicts the sentiment of movie reviews as **Positive** or **Negative** using a pre-trained Naive Bayes model with TF-IDF vectorization. This app allows users to input or paste movie reviews and instantly get a sentiment prediction along with a confidence score.  

---

## Features

- Clean and interactive web interface built with **Streamlit**.
- Predict sentiment of movie reviews as **Positive** or **Negative**.
- Displays **prediction confidence score**.
- Includes **sample reviews** for testing.
- Sidebar instructions for ease of use.
- Author dedication and GitHub link included in the footer.

---

## Demo

![Demo Screenshot](screenshot.png)  
*Replace with your actual app screenshot.*

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/IMDb-Sentiment-App.git
cd IMDb-Sentiment-App
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure the model is in place:

```
model/naive_bayes_model_pipeline.joblib
```

---

## Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```

* Enter a movie review in the text box.
* Click **Predict Sentiment**.
* Optionally, check **Use a Sample Review** to test instantly.
* View the predicted sentiment and confidence score.

---

## Project Structure

```
IMDb-Sentiment-App/
│
├─ app.py                     # Main Streamlit app
├─ model/
│   └─ naive_bayes_model_pipeline.joblib  # Pre-trained pipeline
├─ requirements.txt           # Python dependencies
└─ README.md
```

---

## Requirements

* Python 3.12
* Streamlit
* scikit-learn 1.6.1
* pandas
* numpy
* joblib

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Deployment

You can deploy this app online using **Render**, **Streamlit Cloud**, or **Heroku**.

### Render Deployment

1. Push your repository to GitHub.
2. Create a new **Web Service** on Render and connect your GitHub repo.
3. Set the **Start Command**:

```bash
streamlit run app.py --server.port $PORT
```

4. Deploy and access your app online.

---

## Author

Developed with ❤️ by **Md. Nazmul Hossain**
Dedicated to all movie lovers 🎥

GitHub: [https://github.com/nazmul-1117/IMDb-Sentiment-App](https://github.com/nazmul-1117/IMDb-Sentiment-App)

---

## License

This project is open-source and available under the MIT License.