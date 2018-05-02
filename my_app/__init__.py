from flask import Flask, request, json, make_response

# Define app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def sum_num(num1, num2):
    return num1 + num2

def subtract_num(num1, num2):
    return num1 - num2


'''
def multiply_num()


def divide_num()
'''

def prepare_response(message):
    # build response body to return back to Dialogflow
    request_response = {
        "speech": message,
        "displayText": message,
        "data": None,
        "contextOut": [],
        "source": "MY-CHATBOT-API"
    }
    request_response = json.dumps(request_response, indent=4)
    response = make_response(request_response)
    response.headers['Content-Type'] = 'application/json'
    print(message)
    return response

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = '' # going to store message for Chatbot to say

    # convert request from Dialogflow to JSON
    req = request.get_json(silent=True, force=True)
    # print out request JSON
    print(json.dumps(req, indent=4))
    # dissect the incoming message from dialogflow
    try:
        # if action is 'add_numbers' do addition
        if (req['result']['action'] == 'add_numbers'):
            # grab two numbers from dialogflow parameters
            num1 = int(req['result']['parameters']['num1'])
            num2 = int(req['result']['parameters']['num2'])
            # use sum_num() function to find sum of two numbers
            message = "The sum of {} and  {} is {}".format(num1, num2, sum_num(num1, num2))
            return prepare_response(message)
    except:
        message = "Oops there was an error, try again"
        return prepare_response(message)


if __name__ == '__main__':
    app.run() # kick off our API here

