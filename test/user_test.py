from model.da.da import DataAccess
from model.entity.user import User

user = User (1 ,"Reza", "Rezaii","09121111111","tehran","mft")

user_da = DataAccess(User)
user_da.save(user)

print(user)
