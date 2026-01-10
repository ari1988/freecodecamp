"""
Python gives you four handy built-in functions to dynamically work with object attributes.
They are getattr(), setattr(), hasattr(), and delattr().
"""

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
person = Person('John Doe', 38)

print(getattr(person,'name'))
print(dir(person))

##---------------

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30