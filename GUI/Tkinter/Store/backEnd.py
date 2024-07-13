import dataBase

class personnel:

    def __init__(self, Name="" ,lastName="", number=""):
        self.Name = Name
        self.lastName = lastName
        self.number = number

    def Add_new(self):
        dataBase.Add_new_personnel(self.Name, self.lastName, self.number)

    def Edit_personnel(self, id):
        dataBase.Edit_personnel(id, self.Name, self.lastName, self.number)
    

class object(personnel):
    def __init__(self, Name="" ,lastName="", number="", number_of_object=""):
        super().__init__(Name, lastName, number)
        self.number_of_object = number_of_object

    def Add_new_object(self):
        dataBase.Add_new_object(self.Name, self.lastName, self.number, self.number_of_object)

    def Edit_object(self, id):
        dataBase.Edit_object(id, self.Name, self.lastName, self.number, self.number_of_object)

        

def View_personnel():
    all_personnel = dataBase.View_all_personnel()
    allPersonnel = []
    for num in all_personnel:
        all_personnel = personnel(num[1], num[2], num[3])
        allPersonnel.append((num[0], all_personnel.Name, all_personnel.lastName, all_personnel.number))
    return allPersonnel


def View_object():
    all_object = dataBase.View_all_object()
    allObject = []
    for num in all_object:
        all_object = object(num[1], num[2], num[3], num[4])
        allObject.append((num[0], all_object.Name, all_object.lastName, all_object.number, all_object.number_of_object))
    return allObject


def serchPersonnel(Name="", lastName="", number=""):
    all_personnel = dataBase.Serch_personnel(Name, lastName, number)
    allPersonnel = []
    for num in all_personnel:
        all_personnel = personnel(num[1], num[2], num[3])
        allPersonnel.append((num[0], all_personnel.Name, all_personnel.lastName, all_personnel.number))
    return allPersonnel

def serchObject(Name="", lastName="", number="", number_of_object="" ):
    all_object = dataBase.Serch_object(Name, lastName, number, number_of_object)
    allObject = []
    for num in all_object:
        all_object = object(num[1], num[2], num[3], num[4])
        allObject.append((num[0], all_object.Name, all_object.lastName, all_object.number, all_object.number_of_object))
    return allObject

#==========================================================================================================


def delete(id):
    dataBase.Delete_personnel(id)

def deleteObject(id):
    dataBase.Delete_object(id)

