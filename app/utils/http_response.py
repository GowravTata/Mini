from flask import make_response, jsonify

class ApplicationResponse():
    @staticmethod
    def incomplete_param():
        response =  make_response(jsonify({'success':False, 'result':'Incomplete parameters'}), 400)
        response.headers['Access-Control-Allow-Credentials'] = True
        return response
    @staticmethod
    def success(data):
        response =  make_response(jsonify({'success':True, 'result':data}), 200)
        response.headers['Access-Control-Allow-Credentials'] = True
        return response
    @staticmethod
    def failed(data):
        response =  make_response(jsonify({'success':False, 'result':data}), 400)
        response.headers['Access-Control-Allow-Credentials'] = True
        return response