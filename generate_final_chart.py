import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

# Layout adjustments for styling
fig.update_layout(
    title_text="Final Demand Data",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='lightgray', title='%'),
    yaxis2=dict(showgrid=False, title='index number'),
    legend=dict(
        orientation="h", 
        yanchor="top", y=-0.15, 
        xanchor="center", x=0.5
    ),
    plot_bgcolor='white',
    barmode='group'
)

# Save the interactive file
fig.write_html("final_demand_chart.html")
print("Interactive chart saved as final_demand_chart.html")