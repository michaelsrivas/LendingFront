from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
from Entities import Entities
users = [] 
owners = [] 
bussinesss = [] 

class BaseHandler(RequestHandler):
    
     def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                    'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
        
class SignIn(BaseHandler):  
  def post(self):
    credentials = (json.loads(self.request.body))
    loginEmail = credentials["email"]
    loginPassword = credentials["password"]    
    
    exist = any(o for o in owners if o.email == loginEmail and o.password == loginPassword)
    #if exist == 0:
    #    login = Entities.Login(loginEmail, loginPassword)
    #    users.append(login)    
    self.write({'message': exist})  

class SignUp(BaseHandler):
  def post(self):
    owner = (json.loads(self.request.body))
    email = owner["email"]     
    password = owner["password"] 
    socialSecurityNumber = owner["ssNumber"]
    name = owner["name"]
    address = owner["address"]
    city = owner["city"]
    state = owner["state"]
    postalCode = owner["postalCode"]  
    taxId = owner["taxId"]  
    bussinessName = owner["bussinessName"]
    bussinessAddress = owner["address"]
    bussinessCity = owner["city"]
    bussinessState = owner["state"]
    bussinessPostalCode = owner["postalCode"]    
    amount = int(owner["amount"])

    exist = any(o for o in owners if o.email == email)
    if exist == 0:
        ownerEntity = Entities.Owner(
            socialSecurityNumber, 
            name, 
            address, 
            city, 
            state, 
            postalCode, 
            email,
            password,
            taxId,
            bussinessName,
            bussinessAddress,            
            bussinessCity,
            bussinessState,
            bussinessPostalCode,
            amount)
        owners.append(ownerEntity) 
    
    exist = any(o for o in owners if o.password == password and o.password == password)
    message = ""
    if amount > 50000:
        message = "Declined"
    elif amount == 50000:
        message = "Undecided"
    else:
        message = "Approved"

    self.write({'message': message})
    #self.write({'message': json.loads(json.dumps(ownerEntity.__dict__))})

class SignUpBussiness(BaseHandler):
  def post(self):
    bussiness = (json.loads(self.request.body))
    email = bussiness["email"]     
    taxId = bussiness["taxId"]
    name = bussiness["name"]
    address = bussiness["address"]
    city = bussiness["city"]
    state = bussiness["state"]
    postalCode = bussiness["postalCode"]    
    amount = int(bussiness["amount"])

    exist = any(b for b in bussinesss if b.ownerEmail == email)
    if exist == 0:
        bussinessEntity = Entities.Bussiness(email, taxId, name, address, city, state, postalCode, amount)
        bussinesss.append(bussinessEntity) 

    message = ""
    if amount > 50000:
        message = "Declined"
    elif amount == 50000:
        message = "Undecided"
    else:
        message = "Approved"

    self.write({'message': message})

def make_app():
  urls = [      
      ("/api/users/authenticate/", SignIn),
      ("/api/users/register/", SignUp),      
      ]
  return Application(urls, debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8881)
    print("Listening port 8881")
    IOLoop.instance().start()
    
