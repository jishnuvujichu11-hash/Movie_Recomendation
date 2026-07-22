import streamlit as st
import pandas as pd
import requests
import pickle


with open (open('model.pkl','rb')) as file:
    movies,consine_sim = pickle.load(file)