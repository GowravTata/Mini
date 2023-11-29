from flask import Blueprint,request
from flask_restx import Resource, Api
from app.services.home import Home
from app.utils.http_response import ApplicationResponse as response

api_blueprint = Blueprint('api',__name__, url_prefix='/home')
api = Api(api_blueprint)


@api.route('/register')
class RegisterUser(Resource):
    def post(self):
        data = request.json
        if 'username' in data and 'password' in data:
            home = Home()
            reason, success = home.register_user(data=data)
            if success:
                return response.success('SUCCESS')
            else:
                return response.failed(reason)        
        else:
            return response.incomplete_param()
        
api.add_resource(RegisterUser, '/')
