from collections.abc import Sequence
from typing import Any, Literal

import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.axes import Axes
from matplotlib.typing import ColorType

STYLE = "white"
CONTEXT = "talk"
RC = {
        "figure.facecolor": "white",
        "figure.dpi": 300,
        "figure.figsize": (4.5, 3),
        "figure.frameon": False,
        "axes.autolimit_mode": "round_numbers",
        "axes.labelsize": 12,
        "axes.labelweight": "bold",
        "axes.linewidth": 1.5,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "errorbar.capsize": 3,
        "font.sans-serif": ["Arial"],
        "font.size": 14,
        "font.weight": "bold",
        "legend.fontsize": 8,
        "legend.frameon": False,
        "legend.loc": "best",
        "lines.linewidth": 2,
        "lines.markeredgecolor": "black",
        "lines.markerfacecolor": "black",
        "mathtext.bf": "Arial:bold",
        "mathtext.bfit": "Arial:italic:bold",
        "mathtext.fontset": "custom",
        "mathtext.it": "Arial:italic",
        "mathtext.rm": "Arial",
        "mathtext.sf": "Arial",
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
        "xtick.labelsize": 10,
        "xtick.major.width": 1.5,
        "xtick.minor.width": 1.5,
        "xtick.bottom": True,
        "ytick.labelsize": 10,
        "ytick.major.width": 1.5,
        "ytick.minor.width": 1.5,
        "ytick.left": True,
        "patch.linewidth": 1.5,
        "pdf.fonttype": 42
}

def set_theme(
    context: dict[str, Any] | Literal['paper', 'notebook', 'talk', 'poster'] = CONTEXT,
    style: dict[str, Any] | Literal['white', 'dark', 'whitegrid', 'darkgrid', 'ticks'] = STYLE,
    palette: str | Sequence[ColorType] | None = "deep",
    font: str = "sans-serif",
    font_scale: float = 1,
    color_codes: bool = True,
    rc: dict[str, Any] = RC,
):
    sb.set_theme(
        context=context,
        style=style,
        palette=palette,
        font=font,
        font_scale=font_scale,
        color_codes=color_codes,
        rc=rc
    )

def barplot(*args, **kwargs) -> Axes:
    """
    Barplot + strip plot for categorical data
    """

    target_ax = kwargs.get("ax", plt.gca())
    patch_count = len(target_ax.patches)
    hue = kwargs.get("hue")
    fill_alpha = kwargs.get("alpha")
    if hue is None:
        kwargs.setdefault("color", "grey")
        kwargs.setdefault("edgecolor", "black")

    else:
        # Apply alpha after Seaborn chooses the hue colors so the edges can
        # remain fully opaque.
        fill_alpha = kwargs.pop("alpha", 0.5)

    ax = sb.barplot(*args, **kwargs)

    if hue is not None:
        for bar in ax.patches[patch_count:]:
            facecolor = bar.get_facecolor()
            # ignore the following lsp diagnostics because types in python don't behave properly
            # set_*color accepts a ColorType which can be RGBAColorType -> tuple[float, float, float, float]
            # # which is exactly what we pass below.
            bar.set_facecolor((*facecolor[:3], fill_alpha))  # pyright: ignore[reportArgumentType]
            bar.set_edgecolor("black")  # pyright: ignore[reportArgumentType]

    sb.stripplot(*args, **kwargs, edgecolor=RC["lines.markeredgecolor"], linewidth=RC["patch.linewidth"] / 2)
    sb.despine(ax=ax)
    plt.tight_layout()

    return ax
