from config  import app
from flask import request,abort,jsonify
from api import convoapi
from models import getConvo,getTranslated

@app.route('/api/conversation',methods=['post'])
def getConversation():
    try:
        input=request.get_json()
        context=input['context']
        conversation=getConvo(context)
        print(conversation)
        return jsonify ({"conversation": conversation}) , 200
    except:
        abort ( {"status": "Server error"}, 500)


@app.route('/api/translated',methods=['post'])
def getTranslatedAPI():
    try:
        input=request.get_json()
        language=input['language']
        text=input['text']
        conversation=getTranslated(language,text)
        print(conversation)
        return jsonify ({"conversation": conversation}) , 200
    except:
        abort ( {"status": "Server error"}, 500)
