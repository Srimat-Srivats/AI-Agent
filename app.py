import pandas as pd
from flask import Flask, request, render_template, make_response
from google.oauth2 import service_account
import gspread
import requests
import time
import openai

app = Flask(__name__)

def read_csv(https://docs.google.com/spreadsheets/d/1kdoQjdIBMKlGX0WKosDrDP5zjy0DEHjnrKXeqGdcjoI/edit?usp=sharing):
    return pd.read_csv(https://docs.google.com/spreadsheets/d/1kdoQjdIBMKlGX0WKosDrDP5zjy0DEHjnrKXeqGdcjoI/edit?usp=sharing)

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

openai.api_key = {
  "type": "service_account",
  "project_id": "thermal-diorama-433913-p1",
  "private_key_id": "3af6c8a5e64e84ec0a056a831ad41de628c67f97",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDsMGter6e9Pznc\np5KeuDNiZMYAzyYAiM67wINT0zdmb4vWjUE8pMmyTigbr9mzLAMxuBLcmtHQn1xQ\ntcKRtZW913z5Px3W7XnBW8b0kdf6ZuSbImo5yXCS19PDVH+z8Og0OXfRo+y9IwqM\nHRg8KUqIyac8sfniCW/2QdZqKQIKhVLI7FRu+s9ssUmuqf1V56J/7F9045ZRWpIm\nwWrxeZ9iWv/ydSsefggM53DtLt9UBCMSxrH/MdpmFij0FNC82OBYIgLt/CdU0w/O\nsB6xgg9hTVCwt8b/2UNxZdXgsxOSgaDub77niGA/CIhSqzYY2xmzLjYbmCYPuLxT\nUupQrJB5AgMBAAECggEAXCDg6My0rc2JSOg2eWHZbUJot60VojS7CyJjN6HWZMcS\n8UwlC74tjLcOzwnvbYO39T9bYCClwe4/aJ4VeJevgp8Y+PIlNg5opUMi3og7Cknz\nVw38CHFqT2UPjYwayfoo4SIfei8qa3ZNKW055FGo6KVb7gFwOrq6qQByXfOD/8zU\nra5/MdBm2yoXR371HgqpBu3Nj66Kh0Gav5rWpXHgshP4iPK3ijeuGqDFpoU6xYHv\ngjFbR+YUV3J8sw9Av3wnyheHtb+Ijlr3dIxp71dL9LeCrporm8ic2P3wr4wClbuT\nKcfKHCHxbN5BbqWUGjZ88Sqn5dXu/XPLjbTmf44JHwKBgQD5V8ndvBsLzj01K/NF\ndLk9aVo1Vhs/PqKD7HPcWjqDbiCWLScKopxkomXyOEgGBaCpM04nbWMANCfW3Aju\nFDSGwEuozLt9VtXBvZA5F5/IPVsd9hKbjW7Rz7BBciyqNF4QG+bLND8V4h4Si9Z2\nMHNchAGR2tAWwfNtKlRobT9gswKBgQDyfrotHFam5bh32zuKoU6wsziTr5fQV9I3\nw87iRbR8MlmfHNKLujusanEmG36FrfpQ42H+kUDtdQ2orUopPfSyYJIAaMCJzq/S\nRS4cwI/NZY4SSB0GA5cvtOYWUnKzwaESGSGPhfYNHM15ydNBSM1Aj17c0ZwS5SI6\nBR0MgvBIIwKBgAFYygxakcLUkFwTKrM7WCzOvt/+4RLMYdBYnJ+aFSrUk3R8NfPG\nwRWCEw7l4u21ZhLD5i4sVxaPMY/ljF7M2SPJMh9tS633pBvxzC+iwwgv3KgixiL0\n9p5Hguo3laotsjxgCjUaySRzHjp3auckh9r+E4wYJHua/JegXOhbfrYlAoGAGA0B\noh/BaGQ4W4re6Oz+xP/BiMRNplhPfUBqcH7BW+ASi3lsWHdsG7mi50iqz89lmEg1\nG+6EJgkKBcTKKjT+5AI3+Npq3kAlqBE8dZWTrad4489LMaGBiTXD7ErZHYMC2qyr\na3S55qsIph+iWENEODcADZ6sgCNBtcd0Dh2ef0kCgYEAz86Kz0FzxUDTrvypqjRA\nmiKFtMn9iQbR2EKHmdUlgJ6S0F76n0L5FFoasVyJPZufS+1o8yI2BOX9Dwc0ibkM\nOjmHAztJ8l06asjMmzgHbM9Uy4aZB0Sk4R1oaUOMP2A1yL8dLaoJ4ft/uz4MQVm5\nvbSOoRyDN5/+MmH6a3u9WVM=\n-----END PRIVATE KEY-----\n",
  "client_email": "srimat@thermal-diorama-433913-p1.iam.gserviceaccount.com",
  "client_id": "117069911100238076982",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/srimat%40thermal-diorama-433913-p1.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


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
