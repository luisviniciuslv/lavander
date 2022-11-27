import os

from flask import Flask

from constants import config

class Lavander(Flask):
  def __init__(self):
    super(Lavander, self).__init__("Lavander")
    for i in os.listdir('./src/controllers'):
        if str(i).endswith('.py'):
          i = str(i).replace('.py', '')
          self.register_blueprint(__import__('controllers.' + i, fromlist=[i]).__dict__[i])
          print("loaded ", i)

client = Lavander()
client.run(port=config["PORT"])
