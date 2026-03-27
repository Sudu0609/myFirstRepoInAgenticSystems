# Import libraries
import pandas as pd
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))
loss = [0.9, 0.75, 0.6, 0.5, 0.45, 0.42, 0.4, 0.39, 0.38, 0.38]

# Step 2: Create DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Training Loss": loss
})

# Step 3: Create line chart
fig = px.line(
    df,
    x="Epoch",
    y="Training Loss",
    title="Training Loss Over Epochs",
    markers=True
)

# Step 4: Add annotation (where loss stabilizes)
fig.add_annotation(
    x=8,
    y=0.39,
    text="Loss stabilizes here",
    showarrow=True,
    arrowhead=2
)

# Step 5: Update axis labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

# Step 6: Show chart
fig.show()