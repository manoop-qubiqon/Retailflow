import pandas as pd
import pytest
from src.clean_sales import clean_sales, revenue_by_region


def sample():
    return pd.DataFrame({
        "order_id":   [1, 1, 2, 3],
        "order_date": ["2026-10-01"] * 4,
        "region":     ["South", "South", "North", "North"],
        "product":    ["A", "A", "B", "C"],
        "quantity":   [2, 2, None, 4],
        "unit_price": [10.0, 10.0, 5.0, 2.5],
    })


def test_removes_duplicates_and_missing():
    assert len(clean_sales(sample())) == 2


def test_revenue_is_quantity_times_price():
    out = clean_sales(sample())
    assert out.loc[out.order_id == 1, "revenue"].item() == 20.0


def test_revenue_by_region():
    result = revenue_by_region(clean_sales(sample()))
    assert result.iloc[0]["region"] == "South"


def test_missing_column_raises():
    with pytest.raises(ValueError):
        clean_sales(sample().drop(columns=["region"]))
