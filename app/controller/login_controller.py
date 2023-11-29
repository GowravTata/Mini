from flask import Blueprint,request
from flask_restx import Resource, Api
from app.services.login_service import LoginService
from app.utils.http_response import ApplicationResponse as response

home_blueprint = Blueprint('api',__name__, url_prefix='/home')
api = Api(home_blueprint)


@api.route('/register')
class RegisterUser(Resource):

    def post(self):
        payload = request.json
        if 'username' in payload and 'password' in payload:
            loginService = LoginService()
            reason, success = loginService.register_user(payload=payload)
            if success:
                return response.success('SUCCESS')
            else:
                return response.failed(reason)        
        else:
            return response.incomplete_param()
        
    def get(self):
        username =request.args.get('username') 
        loginService= LoginService()
        reason, success =loginService.get_user(username)
        if success:
            return response.success('SUCCESS')
        else:
            return response.failed(reason)  
        
    def delete(self):
        username =request.args.get('username') 
        loginService= LoginService()
        reason, success =loginService.delete_user(username)
        if success:
            return response.success('SUCCESS')
        else:
            return response.failed(reason)  
        
api.add_resource(RegisterUser, '/')
