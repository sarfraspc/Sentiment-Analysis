
# Twitter US Airline Sentiment Analysis

A complete **Sentiment Analysis pipeline** using the **Twitter US Airline Sentiment Dataset**, built with  Python, and Streamlit! This project includes preprocessing, model training, and a web app for live predictions.

---

##  Project Structure

```

Sentiment Analysis/
├── data/                      # Raw & processed data
│   ├── Tweets.csv
│   └── cleaned\_tweets.csv
├── notebook/                  # EDA and prototyping
│   └── eda.ipynb
├── src/                       # Core modules
│   ├── preprocessing.ipynb
│   ├── vectorization.ipynb
│   ├── training.ipynb
│   └── evaluation.ipynb
├── app/                       # Streamlit app
│   └── streamlit\_app.py
├── README.md

````

---

##  Features

-  Cleaned tweet text using regex, stopwords & lemmatization
-  TF-IDF vectorization + One-Hot encoding for airline
-  Models trained: **Logistic Regression** & **MultinomialNB**
-  Evaluation metrics for comparison
-  Streamlit web app for real-time predictions

---

##  Tech Stack

- Python
- pandas, nltk, scikit-learn
- joblib
- Streamlit

---

##  Model Comparison

| Model                  | Accuracy |
|------------------------|----------|
| Logistic Regression    | Good   |
| Multinomial Naive Bayes| Decent |

---

## How to Run

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/sentiment-analysis.git
cd sentiment-analysis
````

2. **Install requirements**

```bash
pip install -r requirements.txt
```

3. **Run Streamlit app**

```bash
streamlit run app/streamlit_app.py
```

---

## Dataset

Dataset: [Twitter US Airline Sentiment (Kaggle)](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)

---

## Author

**Sarfras** –
[Linkedin](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
[Github](https://github.com/sarfraspc/Sentiment-Analysis.git)

---

Happy Predicting!
