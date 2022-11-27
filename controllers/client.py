import json
from flask import Blueprint, jsonify, request
from exceptions.clientAlreadyExists import ClientAlreadyExists
from exceptions.clientNotFound import ClientNotFound
from exceptions.invalidPayloadException import InvalidPayloadException
from service.clientService import ClientService
client = Blueprint('client', __name__, url_prefix='/client')

@client.route('/',methods=['POST'])
async def create():
  data = request.get_json()
  try:
    client = ClientService()
    await client.create(data)
    return jsonify({'message': 'Client created'}), 201
  
  except InvalidPayloadException as e:
    return jsonify({'message': e.message}), 400
  
  except ClientAlreadyExists as e:
    return jsonify({'message': e.message}), 400

@client.route('/<id>', methods=['POST'])
async def update(id):
  req = request.get_json()
  field = req["field"]
  data = req["data"]
  
  try:
    client = ClientService()
    await client.update_one(id, field, data)
    return jsonify({'message': 'Updated'}), 204
  
  except ClientNotFound as e:
    return jsonify({'message': e.message})

@client.route('/<id>', methods=['GET'])
async def get(id):
  try:
    client = ClientService()
    foundClient = await client.get_by_id(id)
    print(foundClient)
    return jsonify(foundClient), 200

  except ClientNotFound as e:
    return jsonify({'message': e.message}), 404

@client.route('/', methods=["DELETE"])
async def delete():
  data = request.get_json()
  id = data["id"]

  try:
    client = ClientService()
    await client.delete_by_id(id)
    return jsonify({'message': 'sucess'}), 200
  except ClientNotFound as e:
    return jsonify({'message': e}), 404