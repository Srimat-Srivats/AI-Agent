import pandas as pd
from flask import Flask, request, render_template, make_response
from google.oauth2 import service_account
import gspread
import requests
import time
import openai

app = Flask(__name__)

def read_csv(file_path):
    return pd.read_csv(file_path)

def connect_to_google_sheets(sheet_id, range_name):
    credentials = service_account.Credentials.from_service_account_file('path_to_credentials.json')
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(sheet_id).worksheet(range_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    data = read_csv(file)
    columns = data.columns.tolist()
    return render_template('select_column.html', columns=columns, data_preview=data.head().to_html())

@app.route('/define_query', methods=['POST'])
def define_query():
    query_template = request.form['query']
    file = request.files['file']
    data = read_csv(file)
    search_column = request.form['search_column']
    queries = data[search_column]
    results = {}
    for entity in queries:
        search_results = web_search(query_template.format(entity=entity))
        parsed_result = extract_information(search_results, entity)
        results[entity] = parsed_result
    return render_template('results.html', results=results)

@app.route('/download_csv')
def download_csv():
    df = pd.DataFrame(results.items(), columns=['Entity', 'Extracted Information'])
    response = make_response(df.to_csv(index=False))
    response.headers['Content-Disposition'] = 'attachment; filename=results.csv'
    response.headers['Content-Type'] = 'text/csv'
    return response

def web_search(query):
    try:
        response = requests.get(f"https://api.serpapi.com/search?q={query}", params={'api_key': 'YOUR_API_KEY'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        time.sleep(60)  # wait for a minute before retrying
        return perform_search(query)

openai.api_key = 'YOUR_OPENAI_API_KEY'

def extract_information(search_results, entity):
    prompt = f"Extract the email address of {entity} from the following web results: {search_results}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
