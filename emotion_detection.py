import requests 
import json

def emotion_detector(text_to_analyse): # URL del servicio de análisis de sentimientos 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Construyendo la carga útil de la solicitud en el formato esperado 
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Encabezado personalizado que especifica el ID del modelo para el servicio de análisis de sentimientos 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Enviando una solicitud POST a la API de análisis de sentimientos 
    response = requests.post(url, json=myobj, headers=header)

    # Si el código de estado de la respuesta es 200, extrae el label y el score de la respuesta 
    if response.status_code == 200: 
        # Analizando la respuesta JSON de la API 
        formatted_response = json.loads(response.text)
        
        # Acceder al diccionario de emociones
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Obtener la emoción con mayor valor
        max_emotion = max(emotions, key=emotions.get)

        jsonR = {  
         "anger": emotions['anger'], 
         "disgust": emotions['disgust'], 
         "fear": emotions['fear'], 
         "joy": emotions['joy'], 
         "sadness": emotions['sadness'], 
         "dominant_emotion":max_emotion,
         "code": response.status_code   
        }

    else: 
        jsonR = {  
         "anger": None, 
         "disgust": None, 
         "fear": None, 
         "joy": None, 
         "sadness": None, 
         "dominant_emotion":None,
         "code": response.status_code    
        }

        
    # Devolviendo un diccionario que contiene los resultados del análisis de sentimientos 
    return jsonR


#print(emotion_detector("i love you"))
#from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#import unittest


