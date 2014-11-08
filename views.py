from app import app
from stream_client import client
from flask import request, Response

@app.route('/api/subscription', methods=['POST', 'DELETE'])
def follow():
    session_id = 3 # TODO get from session
    my_feed = client.feed('flat:'+str(session_id))
    care_taker_id = request.form.get('care_taker_id')
    if not care_taker_id:
        return Response(status=400)
        
    if request.method == 'POST':    
        my_feed.follow('user:'+str(care_taker_id))
        return Response(status=201)
    else:
        my_feed.unfollow('user:'+str(care_taker_id))
        return Response(status=202)