from app.models.register import Register
from app.utils.pgsql import SqlDB
from sqlalchemy import insert, delete


sql = SqlDB()

class LoginService:
    def __init__(self):
        pass
    
    def register_user(self,payload):
       reason, success = '', False
       try:
           with sql.transaction() as session:
               statement = insert(Register).values(payload)
               session.execute(statement)
               success = True
       except Exception as e:
            reason = str(e)
       finally:
           return reason, success
    
    def get_user(self, username):
        reason, success = '', False
        with sql.transaction() as session:
            user_exists = session.query(Register).filter(Register.username==username).all()
            if user_exists:
                reason = user_exists
                success = True
            else:
                reason = f'User {username} not found.☹'
                success= False
        return reason, success      
         
    def delete_user(self, username):
        reason, success = '', False
        try:
            reason, success =self.get_user(username)
            if success:
                with sql.transaction() as session:
                    statement = delete(Register).where(Register.username==username)
                    session.execute(statement)
        except Exception as e:
            reason = str(e)
            success = False
        finally:
           return reason, success
         
