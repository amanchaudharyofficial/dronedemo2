import json

# def write_json(data, filename):
#   """
#   Writes a dictionary to a JSON file.
#   """
#   with open(filename, "w") as f:
#     json.dump(data, f, indent=4)  # Indent for readability

def read_json(filename):
  """
  Reads a JSON file and returns the data as a dictionary.
  """
  try:
    with open(filename, "r") as f:
      data = json.load(f)
      return data
  except FileNotFoundError:
    print(f"Error: File not found - {filename}")
    return None
  
def populate_structure(json_data):
    """ Populate a dictionary from JSON data """
    users_dict = {}
    for user in json_data['users']:
        # Use user 'id' as the key and the rest of the user details as the value
        users_dict[user['id']] = {
            'ip': user['ip'],
            'port': user['port']
        }
    return users_dict

# Example usage (assuming data is a dictionary)
# data = {"message": "This is a test message"}
# write_json(data, "data.json")
# Read the data back
read_data = read_json("data.json")
users_dict= populate_structure(read_data)
for user_id, details in users_dict.items():
        print(f"MODULE NAME: {user_id}, IP: {details['ip']}, PORT: {details['port']}")
        
