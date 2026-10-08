import pandas as pd

def pareto_flags(df, score="f1_macro", cost="fit_median_s"):
    flags=[]
    for _, row in df.iterrows():
        dominated = ((df[score] >= row[score]) & (df[cost] <= row[cost]) & 
                     ((df[score] > row[score]) | (df[cost] < row[cost]))).any()
        flags.append(not bool(dominated))
    return flags

def test_pareto_marks_dominated_rows():
    df = pd.DataFrame({"f1_macro": [.90, .90, .88], "fit_median_s": [2., 1., 3.]})
    assert pareto_flags(df) == [False, True, False]

def test_single_model_is_pareto():
    df = pd.DataFrame({"f1_macro": [.8], "fit_median_s": [1.]})
    assert pareto_flags(df) == [True]