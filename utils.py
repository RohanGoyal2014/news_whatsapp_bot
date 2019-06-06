import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "bootcampbot-idyulp"

from gnewsclient import gnewsclient
client = gnewsclient.NewsClient(max_results=3) 

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(msg, session_id):
    response = detect_intent_from_text(msg, session_id)
    if response.intent.display_name == 'get_news':
        news = get_news(dict(response.parameters))
        news_str = 'Here is your news:'
        # print(str(news))
        for row in news:
            news_str+= "\n\n{}\n\n{}\n\n".format(row['title'],row['link'])
        
        return news_str



        # return 'ok, i will show you news {}'.format(dict(response.parameters))
    else:
        return response.fulfillment_text

def get_news(parameters):
    client.topic = parameters.get('news type')
    client.language = parameters.get('language')
    client.location = parameters.get('geo-country')
    print(parameters)
    return client.get_news()
    # return '1'