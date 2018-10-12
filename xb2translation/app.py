from .translation import Translation
from flask import Flask, jsonify, request, render_template, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/<language>/<query_string>')
def query(language, query_string):
  args = request.args

  # select language
  if language == 'cn' or language[0] == '简':
    query_language = 'cn'
  elif language == 'fr' or language[0] == '法':
    query_language = 'fr'
  elif language == 'gb' or language == 'en' or language[0] == '英':
    query_language = 'gb'
  elif language == 'ge' or language[0] == '德':
    query_language = 'ge'
  elif language == 'it' or language[0] == '意':
    query_language = 'it'
  elif language == 'jp' or language[0] == '日':
    query_language = 'jp'
  elif language == 'sp' or language[0] == '西':
    query_language = 'sp'
  elif language == 'tw' or language[0] == '繁' or language[0] == '台':
    query_language = 'tw'
  else:
    return '请提交正确的语言'

  # parse tablename
  table = ''
  if 'table' in args.keys():
    table = args['table']

  # parse limit
  limit = 100
  if 'limit' in args.keys():
    limit = int(args['limit'])

  # query db
  t = Translation()
  result = t.query(query_language, query_string, table, limit)
  
  # output format
  format = ''
  if 'format' in args.keys():
    format = args['format']

  if format == 'json':
    data_model = ("table", "id", "cn", "fr", "gb", "ge", "it", "jp", "sp", "tw")
    output = []
    for row in result:
      output.append(dict(zip(data_model, row)))
    return jsonify(output)
  else:
    return render_template('result_table.html', data=result)
