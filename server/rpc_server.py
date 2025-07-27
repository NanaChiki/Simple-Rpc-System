import socket
import json
import os 
import math
from typing import Dict, Any, List, Callable

class RPCServer:
  def __init__(self, socket_path: str = "/tmp/rpc_socket"):
    self.socket_path = socket_path
    self.socket = None
    # This is our "function phonebook" - maps names to actual functions
    self.methods: Dict[str, Callable] = {
      "floor": self._floor,
      "nroot": self._nroot,
      "reverse": self._reverse,
      "validAnagram": self._validAnagram,
      "sort": self._sort
    }

  def _floor(self, x: float) -> int:
    """Like cutting off the decimal part: 3.7 -> 3"""
    return int(math.floor(x))
  
  def _nroot(self, x: int, n: int) -> float:
    """Find what number times itself n times equals x"""
    if n == 0:
      raise ValueError("Cannot calculate 0th root")
    if x < 0 and n % 2 == 0:
      raise ValueError("Cannot calculate even root of negative number")
    return x ** (1.0/n)

  def _reverse(self, s: str) -> str:
    """Turn 'hello' into 'olleh'"""
    return s[::-1]
  
  def _valid_anagram(self, s1: str, s2: str) -> bool:
    """check if two words use the same letters: 'listen' and 'silten'"""
    return sorted(s1.lower()) == sorted(s2.lower())
  
  def _sort(self, str_arr: List[int]) -> List[int]:
    """Put words in alphabetical order: ['cat', 'dog', 'apple'] -> ['apple', 'cat', 'dog']"""
    return sorted(str_arr)
  
  def _valid_params(self, method: str, params: List[Any], param_types: List[str]) -> List[Any]:
    """Check if the parameters are the right type"""
    if len(params) != len(param_types):
      raise ValueError(f"Expected {len(param_types)} parameters, got {len(params)}")
    
    converted_params = []
    for param, param_type in zip(params, param_types):
      if param_type == "int":
        converted_params.append(int(param))
      elif param_type == "float":
        converted_params.append(float(param))
      elif param_type == "str":
        converted_params.append(str(param))
      elif param_type == "list":
        if not isinstance(param, list):
          raise ValueError(f"Expected list, got {type(param)}")
        converted_params.append(param)
      else:
        converted_params.append(param)

    return converted_params.append(param)
  
  def _process_request(self, request_data: str) -> str:
    """This is like reading a note and doing what it asks"""
    try:
      request = json.loads(request_data)
      # Extract info from the request
      method = request.get("method")
      params = request.get("params", [])
      param_types = request.get("param_Types", [])
      request_id = request.get("id", None)
      
      # Check if we know this function
      if method not in self.methods:
        raise ValueError(f"Unknown method: {method}")
      
      # Convert params to right types
      validated_params = self._valid_params(method, params, param_types)

      # Call the function
      result = self.methods[method](*validated_params)

      # Figure out what type the result is
      if isinstance(result, int):
        result_type = "int"
      elif isinstance(result, float):
        result_type = "float"
      elif isinstance(result, str):
        result_type = "str"
      elif isinstance(result, list):
        result_type = "list"
      elif isinstance(result, bool):
        result_type = "bool"
      else:
        result_type = "unknown"
      
      # Send back the answer
      response = {
        "results": result,
        "result_type": result_type,
        "id": request_id
      }

    except Exception as e:
      # If something went wrong, send back an error
      response = {
        "error": str(e),
        "id": request.get("id") if 'request' in locals() else None
      }

    return json.dumps(response)
  
  def start_server(self):
    """Start Listening for requests"""
    # Remove old socket file it it exists
    if os.path.exists(self.socket_path):
      os.unlink(self.socket_path)
    
    # Create a socket like opening a door
    self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    self.socket.bind(self.socket_path)
    self.socket.listen(1)

    print(f"🚀 RPC server started! Listening on {self.socket_path}")
    print(f"Available methods: floor, nroot, reverse, valid_anagram, sort")
    print("Press Ctrl + C to stop")

    try:
      while True:
        # Wait for someone to knock on the door
        connection, client_address = self.socket.accept()
        print(f"📞 Client address: {client_address} \n🔌Socket: {connection}!")
        
        try:
          # Read the message
          data = connection.recv(4096).decode('utf-8')
          if data:
            print(f"📥 Received message: {data}")

            # Process the message and respond
            response = self._process_request(data)
            connection.send(response.encode('utf-8'))
            print(f"📫 Sent response: {response}")
        except Exception as e:
          print(f"❌ Error occurred: {e}")

        finally:
          connection.close()
          print(f"👋 Client disconnected")
    except KeyboardInterrupt:
      print("\\n📴 Server stopping...")
    
    finally:
      if self.socket:
        self.socket.close()
      if os.path.exists(self.socket_path):
        os.unlink(self.socket_path)
    
def main():
  server = RPCServer()
  server.start_server

if __name__ == "__main__":
  main()

