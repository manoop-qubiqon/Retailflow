# Lab 4 solution - standardise region names

Add to clean_sales() right after the dropna line:

    df["region"] = df["region"].str.strip().str.title()

Add to tests/test_clean_sales.py:

    def test_region_names_are_standardised():
        df = sample()
        df["region"] = [" south", "SOUTH", "north", "North "]
        out = clean_sales(df)
        assert set(out["region"]) == {"South", "North"}
