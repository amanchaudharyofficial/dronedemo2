import json

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
    except json.JSONDecodeError:
        print(f"Error: JSON decoding error - {filename}")
        return None
  
def populate_structure(json_data):
    """
    Populate a dictionary from JSON data.
    Assumes json_data is a dictionary with 'users' key containing a list of users.
    """
    if json_data is None or 'users' not in json_data:
        return {}  # Return empty dictionary if json_data is None or 'users' key is missing

    users_dict = {}
    for user in json_data['users']:
        # Use user 'id' as the key and the rest of the user details as the value
        users_dict[user['id']] = {
            'ip': user['ip'],
            'port': user['port']
        }
    return users_dict

# Example usage
read_data = read_json("data.json")
if read_data is not None:
    users_dict = populate_structure(read_data)
    for user_id, details in users_dict.items():
        print(f"MODULE NAME: {user_id}, IP: {details['ip']}, PORT: {details['port']}")
else:
    print("Failed to read JSON data from file.")
