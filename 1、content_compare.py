
import difflib
from bs4 import BeautifulSoup

# 用于比较两个文档的差异

file1 = 'file1_path'
file2 = 'file2_path'

with open(file1, 'r') as f:
    file1_content = f.read()

with open(file2, 'r') as f:
    file2_content = f.read()
    
diff_content = difflib.HtmlDiff().make_table(file1_content.splitlines(), file2_content.splitlines())

soup = BeautifulSoup(diff_content, 'html.parser')

# 查找html中的table
table = soup.find('table')

def table_to_list(table):
		# 将html表转为list
    rows = []
    for row in table.find_all('tr'):
        cols = [col.get_text(strip=True) for col in row.find_all(['td', 'th'])]
        rows.append(cols)
        
    return rows
    
table_list = table_to_list(table)
