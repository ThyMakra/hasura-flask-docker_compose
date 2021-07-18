# from registerUserTypes import registerUserArgs, UserOutput
import requests

from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route('/')
def index():
    return '200'

@app.route('/getAccountInvoice')
def getAccountInvoice():
  resp = requests.get('http://graphql-engine:8080/api/rest/getAccountInvoice')
  excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
  headers = [(name, value) for (name, value) in 
    resp.raw.headers.items() if name.lower() not in excluded_headers]
  response = Response(resp.content, resp.status_code, headers)
  return response
  # return '200'


# @app.route('/registerUser', methods=['POST'])
# def registerUserHandler():
#   args = registerUserArgs.from_request(request.get_json())
#   print(args)
#   # business logic here
#   return UserOutput(id="1").to_json()




if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')