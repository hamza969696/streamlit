import streamlit as st
import cleantext
from textblob import TextBlob 
import pandas as pd

st.title('Sentiment Analysis in Sports')

with st.expander('Analyze Text'):
    text = st.text_input('Text here:')
    if text:
        blob= TextBlob(text)
        st.write('subjectivity:',round(blob.sentiment.subjectivity,2))
    pre=st.text_input('clean text:')
    if pre:
        st.write(cleantext.clean(pre))


with st.expander('Analyze CSV'):
        def analyze(x):
            if x>=0.5:
                return 'Positive'
            else:
                return 'Negative'
        def score(x):
            blob1=TextBlob(x)
            return blob1.sentiment.polarity 

        uploaded_file = st.file_uploader('Upload CSV file:', type=['csv'])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)

            # Assuming 'text_column' is the name of the column you want to analyze
            text_column_name = st.text_input('Enter text column name:', value='text')
            if text_column_name in df.columns:
                df['score'] = df[text_column_name].apply(score)
                df['analysis'] = df['score'].apply(analyze)
                st.write(df.head())
            else:
                st.write(f"Error: '{text_column_name}' column not found in the uploaded CSV file.")

    
