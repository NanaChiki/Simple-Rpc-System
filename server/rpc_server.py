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