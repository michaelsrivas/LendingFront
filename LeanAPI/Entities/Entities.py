class Login:
  def __init__(self, email, password):
    self.email = email
    self.password = password

class Owner:
    def __init__(self, socialSecurityNumber, name, address, city, state, postalCode, email, password, taxId, bussinessName, bussinessAddress, bussinessCity, bussinessState, bussinessPostalCode, amount):        
        self.socialSecurityNumber = socialSecurityNumber
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.email = email 
        self.password = password
        self.taxId = taxId
        self.bussinessName = bussinessName
        self.bussinessAddress = bussinessAddress
        self.bussinessCity = bussinessCity
        self.bussinessState = bussinessState
        self.bussinessPostalCode = bussinessPostalCode
        self.amount = amount

class Bussiness:
    def __init__(self, ownerEmail, taxId, name, address, city, state, postalCode, amount):
        self.ownerEmail = ownerEmail
        self.taxId = taxId
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.amount = amount

   
