import streamlit as st
import pandas as pd

from drifts_algorithms import abrupt, gradual, incremental

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.DataFrame(columns=['dataset', 'starts'])

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')

st.title("Synthetic Dataframe Maker")

col1, col2, col3 = st.columns(3)

drift_type = col1.radio(
     "Drift type:",
     ('Abrupt', 'Gradual', 'Incremental'))

stream_size = col2.text_input('Stream Size', 10000)

samples = col3.text_input('Samples', 100)

st.markdown('---')

if drift_type == 'Abrupt':

    col1, col2 = st.columns(2)

    duration = col1.slider('% Maximum Duration', 0, 100, 10)
    ndiv = col2.text_input('Divisions - Amplitude', 5)
    dataset = []

    placeholder = st.empty()

    if st.button('Generate'):
        st.markdown('---')
        with st.spinner('Generating...'):
            for i in range(int(samples)):
                
                placeholder.write(f"{i+1}/{int(samples)}")

                data_stream = [0] * int(stream_size)
                data_stream, starts, ends, sucess = abrupt(data_stream,int(duration),int(ndiv))
                
                if not sucess:
                    st.stop()

                dataset.append(data_stream)

                df.at[i, 'dataset'] = data_stream
                df.at[i, 'starts'] = starts
                
                placeholder.empty()

            st.balloons()
            st.success(f"{int(samples)} samples generated!")
            print(df)

        st.markdown('---')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )

elif drift_type == 'Gradual':
    col1, col2 = st.columns(2)

    duration = col1.slider('% Initial Duration', 1, 30, 1)
    ndiv = col2.text_input('Divisions - Amplitude', 5)
    dataset = []
    placeholder = st.empty()

    if st.button('Generate'):
        st.markdown('---')
        with st.spinner('Generating...'):
            for i in range(int(samples)):
            
                placeholder.write(f"{i+1}/{int(samples)}")

                data_stream = [0] * int(stream_size)
                data_stream, starts, ends, sucess = gradual(data_stream,int(duration),int(ndiv))

                if not sucess:
                    st.stop()

                dataset.append(data_stream)

                df.at[i, 'dataset'] = data_stream
                df.at[i, 'starts'] = starts

                placeholder.empty()
                
            st.balloons()
            st.success(f"{int(samples)} samples generated!")
            print(df)

        st.markdown('---')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )

elif drift_type == 'Incremental':
    
    duration = st.slider('% Duration', 1, 30, 1)
    placeholder = st.empty()
    dataset = []

    if st.button('Generate'):
        st.markdown('---')
        with st.spinner('Generating...'):
            for i in range(int(samples)):
                placeholder.write(f"{i+1}/{int(samples)}")

                data_stream = [0] * int(stream_size)
                data_stream, starts, sucess = incremental(data_stream, duration)
                
                if not sucess:
                    st.stop()
                
                dataset.append(data_stream)

                df.at[i, 'dataset'] = data_stream
                df.at[i, 'starts'] = starts
            
            st.balloons()
            st.success(f"{int(samples)} samples generated!")

        st.markdown('---')
        
        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv',
        )