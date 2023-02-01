# Synthetic Datastream Database Generator
This project is a Streamlit app that allows you to generate a synthetic datastream database. The app provides an interactive interface where you can select:

- **Drift Type**: Abrupt, Gradual or Incremental drift.
- **Stream size**: Number of bits at data stream
- **Samples**: Stream samples.
- **% Maximum Duration**: Max Drift duration based at stream size.
- **Division**: Aplitude. 

Also, it could be generated randomly, using the random tab at streamlit app.

The generated data can be exported in CSV format for further use.

## Getting Started
Prerequisites
To run this app, you need to have the following packages installed:

- Streamlit
- Pandas

You can install the packages using the following command:

Copy code
``pip install streamlit pandas``


Running the App
To run the app, navigate to the project directory and use the following command:

streamlit run /bin/main.py

## Using the App
The app has a simple and intuitive interface. You can select the all parameters that you want to generate, and select the types of drift to be generated for dataset. After making the selections, click the "Generate" button to generate the data. The generated data will be displayed in a table, and you can export it in CSV format by clicking the "Export to CSV" button.
