import json
import bottle
import ratings

@bottle.route('/')
def index():
  return bottle.static_file("index.html", root="")

@bottle.route('/<js_file>.js')
def javascript_file(js_file):
  print("Getting JavaScript file: " + js_file)
  code_js = bottle.static_file(js_file+".js", root="")
  return code_js

def json_series_data() :
  series_list = ratings.get_series()
  ret_val = json.dumps(series_list)
  return ret_val

@bottle.route('/series')
def get_series():
  ret_val = json_series_data()
  return ret_val

@bottle.post('/add_series')
def add_series():
  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  ratings.add_series(content)
  ret_val = json_series_data()
  return ret_val

@bottle.post('/rate_series')
def rate_series():
  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  ratings.rate_series(content)
  ret_val = json_series_data()
  return ret_val

bottle.run(host="0.0.0.0", port=8080, quiet=True)