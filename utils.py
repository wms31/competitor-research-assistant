from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from bs4 import BeautifulSoup

import io
import markdown
import requests
# from weasyprint import HTML

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

RESULTS_PER_QUESTION = 3
ddg_search = DuckDuckGoSearchAPIWrapper()

def scrape_text(url):
  try:
    response = requests.get(url)
    
    if response.status_code == 200:
      # Parse the content of the page using BeautifulSoup
      soup = BeautifulSoup(response.text, 'html.parser')
        
      # Extract all text from the webpage
      text = soup.get_text(separator=' ', strip=True)

      return text
    else:
      return f"Failed to scrape the webpage. Status code: {response.status_code}"
  except Exception as e:
    print(f"An error occurred: {e}")
    return f"Failed to scrape the webpage. Error: {e}"

def flatten_list_of_list(list_of_list):
  content = []
  for sublist in list_of_list:
    content.append("\n\n".join(sublist))
  return "\n\n".join(content)

def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
  results = ddg_search.results(query, num_results)
  return [r["link"] for r in results]

# Create a sample stylesheet and modify existing styles if needed.
styles = getSampleStyleSheet()
styles['Heading1'].alignment = TA_LEFT
styles['Heading2'].alignment = TA_LEFT
styles['Heading3'].alignment = TA_LEFT

# Correctly add a new style using the add() method.
bullet_list_style = ParagraphStyle(
    name='BulletList',
    parent=styles['Normal'],
    leftIndent=24,
    bulletFontName='Symbol',
    bulletFontSize=10
)
styles.add(bullet_list_style)

numbered_list_style = ParagraphStyle(
    name='NumberedList',
    parent=styles['Normal'],
    leftIndent=24
)
styles.add(numbered_list_style)

# Continue with the rest of your PDF generation code.
# def download_as_pdf(results):
#     pdf_file = io.BytesIO()
#     doc = SimpleDocTemplate(pdf_file, pagesize=letter)
#     story = []

#     # Convert markdown to HTML and then parse with BeautifulSoup
#     import markdown
#     from bs4 import BeautifulSoup

#     html = markdown.markdown(results)
#     soup = BeautifulSoup(html, 'html.parser')

#     for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol']):
#         if element.name == 'h1':
#             p = Paragraph(element.text, styles['Heading1'])
#         elif element.name == 'h2':
#             p = Paragraph(element.text, styles['Heading2'])
#         elif element.name == 'h3':
#             p = Paragraph(element.text, styles['Heading3'])
#         elif element.name == 'p':
#             p = Paragraph(element.text, styles['Normal'])
#         elif element.name == 'ul':
#             list_items = [Paragraph(li.text, styles['BulletList']) for li in element.find_all('li')]
#             p = ListFlowable(list_items, bulletType='bullet')
#         elif element.name == 'ol':
#             list_items = [Paragraph(li.text, styles['NumberedList']) for li in element.find_all('li')]
#             p = ListFlowable(list_items, bulletType='1')
#         else:
#             p = Paragraph(element.text, styles['Normal'])

#         story.append(p)
#         story.append(Spacer(1, 6))

#     doc.build(story)
#     pdf_file.seek(0)
#     return pdf_file.getvalue()