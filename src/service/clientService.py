from exceptions.clientAlreadyExists import ClientAlreadyExists
from repository.clientRepository import ClientRepository
from service.validations.clientCreate import validatePayload
from exceptions.clientNotFound import ClientNotFound


class ClientService:
  def __init__(self):
    self.repository = ClientRepository()

  async def create(self, data: dict):
    validatePayload(data)
    email = data['email']
    found_client = await self.repository.find_by_email(str(email))

    if found_client:
      raise ClientAlreadyExists('Client email already exists')

    return await self.repository.create(data)

  async def update_one(self, id, field, data):
    if not await self.repository.find_by_id(id):
      raise ClientNotFound('Client not found')
    data = {field: data}
    return await self.repository.update_one(id, data)


  async def get_by_id(self, id):
    found = await self.repository.find_by_id(id)
    found.pop('_id')
    return found