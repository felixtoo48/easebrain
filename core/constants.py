from enum import Enum

class UserRoleEnum(Enum):
    ADMIN = "admin"
    USER = "user"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
    

class GenderEnum(Enum):
    MALE = "Male"
    FEMALE = "Female"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
    

class StatusEnum(Enum):
    SINGLE = "Single"
    MARRIED = "Married"
    DIVORCED = "Divorced"
    WIDOWED = "Widowed"
    SEPARATED = "Separated"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
    

class CategoryEnum(Enum):
    MR = "Mr"
    MRS = "Mrs"
    DR = "Dr"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)