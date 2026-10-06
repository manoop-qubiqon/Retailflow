from pathlib import Path
import pandas as pd

REQUIRED = ["order_id", "order_date", "region", "product", "quantity", "unit_price"]


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    missing = set(REQUIRED) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.drop_duplicates(subset="order_id")
    df = df.dropna(subset=["quantity", "unit_price"])
    df = df[df["quantity"] > 0].copy()
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df.reset_index(drop=True)


def revenue_by_region(df: pd.DataFrame) -> pd.DataFrame:
    totals = df.groupby("region", as_index=False)["revenue"].sum()
    return totals.sort_values("revenue", ascending=False)


def main(input_path="data/raw/sales.csv", output_dir="output"):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    raw = pd.read_csv(input_path)
    clean = clean_sales(raw)
    clean.to_csv(out / "sales_clean.csv", index=False)
    revenue_by_region(clean).to_csv(out / "revenue_by_region.csv", index=False)
    print(f"Raw rows: {len(raw)} | Clean rows: {len(clean)}")


if __name__ == "__main__":
    main()
