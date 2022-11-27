from exceptions.invalidPayloadException  import InvalidPayloadException

REQUIRED_FIELDS = ['name', 'email', 'usage_time', 'price_per_hour']

def validatePayload(payload: dict):
  for field in REQUIRED_FIELDS:
    if field not in payload:
      raise InvalidPayloadException(f'Missing field: {field}')

  return True