import requests
import json

def emotion_detector(text_to_analyse):
   url = 'http://localhost:8080/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"accept": "application/json",
              "content-type": "application/json",
                "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)
   formatted_response = json.loads(response.text)
   j = 0
   k = 0
   s = ""
   finalJSON={}
   
   if response.status_code == 200:
      try:
        for i in formatted_response['emotionPredictions']:
          for w in i.items():
            
            for attribute, value in w[1].items():
                finalJSON[attribute]=value
                k=value
                if j == 0:
                  j=value
                  s=attribute
                elif k>j:
                  j=k
                  s=attribute
            finalJSON["dominant_emotion"]= s
            return finalJSON

      except:
          return "error on loop"
      
   elif response.status_code == 400:
      BlankJSON = {
    "anger": None, 
    "disgust": None, 
    "fear": None, 
    "joy": None, 
    "sadness": None, 
    "dominant_emotion":None
    }
      return BlankJSON
