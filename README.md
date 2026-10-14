# SzPlot

Plotting wrapper around Seaborn + Matploblib for lab figures

## Installation

```bash
uv add "szplot @ git+https://github.com/szablowskilab/szplot"
```

## Usage

The `set_theme` function initializes the Seaborn and Matplotlib RC parameters
with the configured style. You can pass any desired overrides for style, context, RC params, etc.

Call `set_theme` before any plotting functions to apply the theme

### Categorical plots

```python
from szplot import set_theme, bar

set_theme()
bar(data, x="categories", y="values", hue="categories")

```

