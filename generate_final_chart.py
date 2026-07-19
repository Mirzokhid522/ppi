import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Load the dataset
file_path = 'Final_Demand_Data.csv'
df = pd.read_csv(file_path)

# Create subplots with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# 1. 'quarter (% change)' bars (Dark Blue)
fig.add_trace(
    go.Bar(
        x=df['Quarter'], y=df['quarter (% change)'], 
        name="quarter (% change)", 
        marker_color='#003366'
    ),
    secondary_y=False,
)

# 2. 'annual (% change)' bars (Orange)
fig.add_trace(
    go.Bar(
        x=df['Quarter'], y=df['annual (% change)'], 
        name="annual (% change)", 
        marker_color='#E67E22'
    ),
    secondary_y=False,
)

# 3. 'index no.' line (Light Blue)
fig.add_trace(
    go.Scatter(
        x=df['Quarter'], y=df['index no.'], 
        name="index no.", 
        line=dict(color='#3498DB', width=2),
        mode='lines'
    ),
    secondary_y=True,
)

# Layout adjustments for dark theme
fig.update_layout(
    title_text="Final Demand Data",
    title_font=dict(color='white'),
    plot_bgcolor='black',
    paper_bgcolor='black',
    xaxis=dict(
        showgrid=False,
        tickfont=dict(color='white'),
        title_font=dict(color='white')
    ),
    yaxis=dict(
        showgrid=True, 
        gridcolor='#333333', 
        title='%',
        tickfont=dict(color='white'),
        title_font=dict(color='white')
    ),
    yaxis2=dict(
        showgrid=False, 
        title='index number',
        tickfont=dict(color='white'),
        title_font=dict(color='white')
    ),
    legend=dict(
        orientation="h", 
        yanchor="top", y=-0.15, 
        xanchor="center", x=0.5,
        font=dict(color='white')
    ),
    barmode='group'
)

# Ensure the directory exists and save the file
if not os.path.exists('public'):
    os.makedirs('public')

fig.write_html("public/index.html")
print("Interactive chart saved as public/index.html")