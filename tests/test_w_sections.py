import pandas as pd
import section_browser.w_sections as wsec


def test_load_aisc_w_sections():
    si_df = wsec.load_aisc_w_sections()
    assert si_df.iloc[0, 1] == "W1100X499"


def test_section_filter():
    test_df = pd.DataFrame(data = [
        ["X", "A", 200, 300], 
        ["X", "B", 250, 250], 
        ["Y", "C", 400, 600], 
        ["Y", "D", 500, 700]], 
        columns=["Type", "Section", "Ix", "Sy"]
    )
    selection = wsec.section_filter(test_df, 'ge', Ix=400)
    assert selection.iloc[0, 1] == "C"
    assert selection.iloc[1, 1] == "D"

    selection = wsec.section_filter(test_df, 'le', Sy=300)
    assert selection.iloc[0, 1] == "A"
    assert selection.iloc[1, 1] == "B"   


def test_sort_by_weight():
    test_df = pd.DataFrame(
        data=[
            ["X", "A", 200, 300],
            ["X", "B", 250, 250],
            ["Y", "C", 400, 600],
            ["Y", "D", 500, 700],
        ],
        columns=["Type", "Section", "Ix", "W"],
    )
    selection = wsec.sort_by_weight(test_df)
    assert selection.iloc[0, 1] == "B"
    assert selection.iloc[1, 1] == "A"
