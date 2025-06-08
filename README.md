# Plotly Formatter

A small Python utility for applying consistent styling to Plotly figures.  
Ideal for generating presentation-ready visuals with minimal effort.

## Features

- Automatically standardizes:
  - Title fonts
  - Axis labels and tick fonts
  - Legend appearance
  - Annotations
  - Grid visibility and layout
- Customizable with font sizes, colors, and more
- Easily extendable for team-specific styles or themes

## Installation

You can install directly from GitHub:

```bash
pip install git+https://github.com/Boerger22/plotly-formatter.git
```

## Usage Example

```python
from plotly_formatter import PlotlyFormatter
import plotly.graph_objects as go

# Create an instance (you can customize parameters if needed)
formatter = PlotlyFormatter()

# Create a Plotly figure
fig = go.Figure(data=go.Scatter(y=[1, 3, 2, 4]))

# Apply consistent styling
formatter.standardize(fig)

# Show the figure
fig.show()
```