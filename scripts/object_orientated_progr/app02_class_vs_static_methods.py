


# When to use class methods and when to use static methods? 

class Item_example: 
    @staticmethod
    def is_integer(num): 
        pass
        '''
        This should do something that has a relationship with the 
        class, but not something that must be unique per instance!
        alternative it could be defined separately out of the class
        '''

    @classmethod
    def instatiate_from_yaml_file(cls):
        pass 
        '''
        This should also do something that has a relatiohship with the class 
        but usually those are used to manipulate different structures of data,
        to instatiate objecs like we have doe with CSV. 
        '''

        ''' 
        MAIN DIFFERENCE: 
        staticmethod does NOT pass the object or class as the first argument
        '''


# commonly static and class methods are  called from the class level 
Item_example.is_integer(5)
Item_example.instatiate_from_yaml_file()

# it is possible to call a static and a class method from the instace level 
# but NOT common
item1 = Item_example()
item1.is_integer(5)