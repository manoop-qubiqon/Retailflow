# RetailFlow - Azure DevOps practical for data engineers

Cleans daily sales CSV files and delivers them to Azure Blob Storage via Azure DevOps.

## Run locally
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python -m pytest -v              # 4 passed
    python -m src.clean_sales        # Raw rows: 8 | Clean rows: 5

## Files
- data/raw/sales.csv              sample input (1 duplicate, 2 rows with missing values)
- src/clean_sales.py              the pipeline
- tests/test_clean_sales.py       unit tests
- azure-pipelines.yml             Lab 3 CI pipeline
- solutions/azure-pipelines-full.yml   Lab 5 CI + CD pipeline
- solutions/lab4_region_change.md      Lab 4 change and test
