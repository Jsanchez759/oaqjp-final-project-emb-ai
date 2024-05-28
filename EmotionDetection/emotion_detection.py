import requests
import json
from transformers import AutoTokenizer, AutoModelWithLMHead

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    data = { "raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, headers = headers, json = data)
    if response.status_code == 400:
        predictions = {
        'anger': None,
        'disgust': None, 
        'fear': None, 
        'joy': None, 
        'sadness': None, 
        'dominant_emotion': None}
    elif response.status_code == 200:
        predictions_dict = json.loads(response.text)
        predictions = predictions_dict['emotionPredictions'][0]['emotion']

        greatest_score = 0
        for label, score in predictions.items():
            if score > greatest_score:
                greatest_score = score
                dominant_emotion = label

        predictions['dominant_emotion'] = dominant_emotion
        
    return predictions

# if __name__ == "__main__":
#     response = emotion_detector('hi')
#     print(response)