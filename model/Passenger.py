class Passenger:
    def __init__(self, id, survived, passenger_class, name, gender, age, sibling_spouse, parent_children, ticket_number
               , fare):
        self.id = id
        self.survived = survived
        self.passenger_class = passenger_class
        self.name = name
        self.gender = gender
        self.age = age
        self.sibling_spouse = sibling_spouse
        self.parent_children = parent_children
        self.ticket_number = ticket_number
        self.fare = fare