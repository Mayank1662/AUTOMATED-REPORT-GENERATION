import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Step 1: Load data
df = pd.read_csv("data/sales_data.csv")
summary = df.describe().to_html(classes='summary-table')

# Step 2: Load template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('report_template.html')

# Step 3: Render HTML with data
html_out = template.render(title="Weekly Sales Report", summary_table=summary)

# Step 4: Export to PDF
HTML(string=html_out).write_pdf("output/sample_report.pdf")

print("✅ Report generated successfully!")
