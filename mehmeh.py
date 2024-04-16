import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Sample data
categories = ['Energy Saved']
values1 = [80]
values2 = [20]

fig, ax = plt.subplots(figsize=(1, 5))
ax.bar(categories, values1, label='Group 1', color ="Green")
ax.bar(categories, values2, bottom=values1, label='Group 2', color ="#F2F3F5")

# Customizing

ax.set_xlabel('Fuel Energy Bar')
ax.set_ylabel('Percentage %')
# ax.title('Vertical Stack Graph')
# plt.legend()

# Displaying the graph



st.pyplot(fig)