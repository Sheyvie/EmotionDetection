"""Watson NPLemotion detection"""
import requests
import json


def emotion_detector(text_to_analyze):
    """watson NLP API endpoint and headers"""
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=headers)
    status_code = response.status_code
    #return response.text
    res= json.loads(response.text)
    if status_code == 400:
        formatted_response = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }
    else:
        res = json.loads(response.text)
        formatted_response = res ['emotionPredictions'][0]['emotion']
        dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
        formatted_response['dominant_dictionary'] = dominant_emotion

    return formatted_response


