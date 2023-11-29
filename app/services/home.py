from app.models.register import Register
from app.utils.pgsql import SqlDB
from sqlalchemy import insert



sql = SqlDB()

class Home:
    def __init__(self):
        pass
    
    def register_user(self,data):
       reason, success = '', False
       try:
           with sql.transaction() as session:
               insert_data = insert(Register).values(data)
               session.execute(insert_data)
               success = True
       except Exception as e:
            reason = str(e)
       finally:
           return reason, success
    # def register_user(self,data):
    #     # self.validate_register_payload(data)
    #     username = data['username']
    #     password = data['password']
    #     msg= {'message':''}
    #     try:
    #         with sql.transaction() as session:
    #             insert_data = insert(Register).values(username=username, password=password)
    #             session.execute(insert_data)
    #             msg['message'] = f'Added user {username}'
    #             return msg
    #     except IntegrityError:
    #             error_msg = f'User {username} already exists.'
    #             raise UserExistsException(error_msg)
    #     except Exception as e:
    #         raise Exception(e)
    
    # def validate_register_payload(self, data):
    #     try:
    #         file = open('app/json_schema/register_user.json')
    #         json_file = json.load(file)
    #         jsonschema.validate(data, json_file)
    #     except ValidationError as error:
    #         raise ValidationError(error.message)

         
         
