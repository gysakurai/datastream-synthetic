import streamlit as st
import pandas as pd
import random

from drifts_algorithms import abrupt, gradual, incremental

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.DataFrame(columns=['dataset', 'starts'])

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')

st.title("Synthetic Dataframe Maker - Random Parameters")

col1, col2, col3 = st.columns(3)

drift_type = col1.radio(
     "Drift type:",
     ('Abrupt', 'Gradual', 'Incremental'))

samples = 100

st.markdown('---')

if drift_type == 'Abrupt':

    placeholder = st.empty()
    i = 1

    if st.button('Generate'):
        with st.spinner('Generating...'):
            while i <= samples:
                
                placeholder.write(f"{i+1}/{int(samples)}")

                stream_size = random.randint(1000, 100000)
                duration = random.randint(1,100)
                ndiv = random.randint(1,5)
        
                data_stream = [0] * int(stream_size)

                data_stream, starts, ends, sucess = abrupt(data_stream,int(duration),int(ndiv))
                
                if not sucess:
                    print(f"{stream_size}|{duration}|{ndiv}")
                    continue

                df.at[i, 'dataset'] = data_stream
                df.at[i, 'starts'] = starts
                i = i + 1
                
                placeholder.empty()

            st.balloons()
            st.success(f"{int(samples)} samples generated!")
            print(df)

        st.markdown('---')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='abrupt.csv',
            mime='text/csv',
        )

elif drift_type == 'Gradual':
    i = 1
    placeholder = st.empty()
    if st.button('Generate'):
        with st.spinner('Generating...'):
            while i <= samples:
                placeholder.write(f"{i+1}/{int(samples)}")
                
                stream_size = random.randint(1000, 100000)
                duration = random.randint(1,30)
                ndiv = random.randint(1,5)
            
                data_stream = [0] * int(stream_size)
                data_stream, starts, ends, sucess = gradual(data_stream,int(duration),int(ndiv))
            
                if not sucess:
                    print(f"{stream_size}|{duration}|{ndiv}")
                    continue

                df.at[i, 'dataset'] = data_stream
                df.at[i, 'starts'] = starts
                i = i + 1

                placeholder.empty()
                
            st.balloons()
            st.success(f"{int(samples)} samples generated!")
            print(df)

        st.markdown('---')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='gradual.csv',
            mime='text/csv',
        )

elif drift_type == 'Incremental':
    placeholder = st.empty()
    i = 1

    if st.button('Generate'):
        with st.spinner('Generating...'):
            while i <= samples:
                placeholder.write(f"{i+1}/{int(samples)}")

                stream_size = random.randint(1000, 100000)
                duration = random.randint(1,30)

                data_stream = [0] * int(stream_size)
                data_stream, starts, sucess = incremental(data_stream, duration)
                
                if not sucess:
                    print(f"{stream_size}|{duration}")
                    continue
                
                df.at[i, 'dataset'] = data_stream
                df.at[i, 'starts'] = starts
                i = i + 1
            
            st.balloons()
            st.success(f"{int(samples)} samples generated!")

        st.markdown('---')
        
        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='incremental.csv',
            mime='text/csv',
        )