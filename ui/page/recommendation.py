from taipy.gui import Markdown
import pandas as pd
from db import SessionLocal

with SessionLocal() as session:
    df = pd.read_sql_table('job_info_clean', session.connection())

recommendations_md = Markdown("""
<|{df}|table|allow_all_rows=True|filter=True|>
""")
