from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formattedText = "For the given statement, the system response is "
    countValue = []    

    if response["dominant_emotion"]==None:
        return "Invalid text! Please try again!"
        
    for attribute, value in response.items():
        countValue.append(str(attribute))
        countValue.append(str(value))
    i=0
    k = 0


    while(i<len(countValue)):
         print(i)
         if countValue[i]=="dominant_emotion":
            formattedText += " The dominant emotion is "+countValue[i+1]
            break
         elif i+4 == len(countValue):
            formattedText += " and "+str(countValue[i])+" : "+str(countValue[i+1])+"."
            i+=1
         else:
            if i%2==0:
                formattedText+="'"+countValue[i]+"'"+" : "
            else:
                 formattedText+=countValue[i]+","
         i+=1
    return formattedText

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
