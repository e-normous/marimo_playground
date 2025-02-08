import marimo

__generated_with = "0.10.19"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    # kaggle dataset from here: https://www.kaggle.com/datasets/joebeachcapital/nintendo-games
    dataset_path = "NintendoGames.csv"
    return (dataset_path,)


@app.cell
def _(dataset_path, pd):
    df_raw = pd.read_csv(dataset_path)
    return (df_raw,)


@app.cell
def _(df_raw):
    # in marimo, we can simply name the df and get an interactive table with shape information at the bottom
    df_raw
    return


@app.cell
def _():
    # there seem to be many values that do not indicate a meta_score. We will remove them later as we'll focus on that column later on.
    return


@app.cell
def _(df_raw):
    # show the different datatypes of each columns
    print(df_raw.dtypes)
    return


@app.cell
def _(df_raw):
    df = df_raw.dropna(subset=["meta_score"])
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.describe()
    return


if __name__ == "__main__":
    app.run()
