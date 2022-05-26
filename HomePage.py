import pathlib
import sys

import streamlit as st
import streamlit.cli as stcli
from tensorflow import keras
from keras_preprocessing.sequence import pad_sequences
import pickle
import matplotlib.pyplot as plt
from Twitter.twitter_api import get_tweets

# Imporing Saved Model
def load_model():
    m = pathlib.Path(__file__).resolve().parent / "Latest.h5"
    model = keras.models.load_model(m)
    return model

#HomePage
def show_predict_page():
    model = load_model()
    st.title("User Depression Prediction")

    st.write("""### Enter Userid to predict his/her Mental health Status""")
    username = st.text_input("username")
    ok = st.button("Predict")
    if ok:
        tokenizer = pathlib.Path(__file__).resolve().parent / "tokenizer.pickle"
        with open(tokenizer, 'rb') as handle:
            tokens = pickle.load(handle)
            max_length = 32
            trunc_type = 'post'
            padding_type = 'post'
            #Getting Data from Twitter API
            tweets = get_tweets(username, 10)
            tweets = tokens.texts_to_sequences(tweets)
            tweets = pad_sequences(tweets, maxlen=max_length, truncating=trunc_type, padding=padding_type)
            result = model.predict(tweets)
            chances = [0, 0]
            for i in result:
                if i < 0.5:
                    chances[0] += 1
                if i > 0.5:
                    chances[1] += 1
            show_explore_page(username, chances)


# Creating Pie Chart and Giving result on the basis of the Total percentage
def show_explore_page(username, chances):
    labels = ["Depressed Percentage", "Non Depressed Percentage"]
    explode = [0, 0]
    if chances[0] > chances[1]:
        explode[0] = 0.2
    else:
        explode[1] = 0.2
    plt.style.use("default")
    fig1, ax1 = plt.subplots()
    ax1.pie(chances, labels=labels, autopct="%1.1f%%", shadow=True, startangle=180, explode=explode)
    ax1.axis("equal")
    st.write("""#### Predicting {0} Mental Health Status""".format(username))
    st.pyplot(fig1)
    depression = (chances[0]/sum(chances))*100
    if depression > 83.0:
        st.write("""#### Severe Chances of Getting Depressed.\n#### Needs Medication""")
    elif depression > 65.0:
        st.write("""#### high Chances of Getting Depressed.\n#### Needs Medical attention""")
    elif depression > 30.0:
        st.write("""#### Low Chances of Getting Depressed.\n#### Needs Medical """)
    else:
        st.write("""#### Happy Mind :) """)

if __name__ == '__main__':
    if st._is_running_with_streamlit:
        show_predict_page()
    else:
        sys.argv = ["streamlit", "run", "HomePage.py"]
        sys.exit(stcli.main())
