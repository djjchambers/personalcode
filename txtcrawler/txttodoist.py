# txttodoist

from todoist.api import TodoistAPI
api_token = "1101a52a2c2afdf97fb557c5aeec4d0c8584b603"
result = TodoistAPI(api_token)
result.sync()
print(result.state['projects'])