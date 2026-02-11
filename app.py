import joblib
import gradio as gr
import numpy as np

model = joblib.load("predictive_maintenance_model.pkl")

def predict(air, process, rpm, torque, tool):
    X = np.array([[air, process, rpm, torque, tool]])
    preds = model.predict(X)[0]
    labels = ["TWF","HDF","PWF","OSF","RNF"]
    return dict(zip(labels, preds))

gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Air Temperature"),
        gr.Number(label="Process Temperature"),
        gr.Number(label="Rotational Speed"),
        gr.Number(label="Torque"),
        gr.Number(label="Tool Wear")
    ],
    outputs="label",
    title="Industrial Failure Prediction System"
).launch()
