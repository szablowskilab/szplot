import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import seaborn as sb
    import os

    from szplot import barplot, set_theme
    data_dir = os.path.join("notebooks", "plots")
    return barplot, data_dir, os, plt, set_theme


@app.cell
def _(set_theme):
    set_theme()

    data = {
        "categories": [
            "A", "A", "A",
            "B", "B", "B",
            "C", "C", "C"
        ],
        "values": [
            1.2, 1.5, 1.1,
            2.4, 2.6, 2.2,
            3.4, 3.6, 3.1
        ]
    }
    return (data,)


@app.cell
def _(barplot, data, data_dir, os, plt):
    barplot(data, x="categories", y="values", width=0.2)

    plt.savefig(os.path.join(data_dir, "barplot.svg"))
    plt.gca()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
