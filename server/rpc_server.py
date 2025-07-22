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