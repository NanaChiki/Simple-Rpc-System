# Simple-rpc-system 🚀

A simple Remote Procedure Call (RPC) system built for learning purposes. This project demonstrates how different programming language can communicate and call functions on each other over a network.

## 🎯 What is RPC?

Think of RPC like this: imagine you have a friend in another room with a calculator. Instead of doing math yourself, you write a note saying "add 5 + 3", pass it through the door, and your friend writes back "8". That's essentially what RPC does - but with computers!

## 🏗️ Architecture

- **Server (Python)**: The "friend with the calculator" - does the actual work
- **Client (Node.js)**: You - sends requests for work to be done
- **Socket**: The "door" - how messages get passed between programs
- **JSON**: The "note format" - standardized way to write requests

## 🚀 Quick Start

### 1. Start the server
```bash
cd server
python rpc_server.py
```

### 2. Run the Client (in a new terminal)
```bash
cd client
node rpc_client.js
```

### 3. Run Comprehensive Tests
```bash
cd examples
node test_calls.js
```

## 📋 Available Functions
| Function              | Description                    | Example                                  |
|-----------------------|--------------------------------|------------------------------------------|
| floor(x)              |  Round down to nearest integer | floor(3.7) → 3                           |
| nroot(x, n)           |  Calculate nth root            | nroot(9,2) → 3.0                         |
| reverse(s)            |  Reverse a string              | reverse("hello") → "olleh"               |
| validAnagram(s1, s2)  |  Check if anagrams             | validAnagram("listen", "silent") -> true |
| sort(arr)             |  Sort string array             | sort(["c", "a", "b"]) → ["a", "b", "c"]  |

## 🧪 Testing

The project includes comprehensive tests in `examples/test_calls.js` that verify:

- All function calls work correctly
- Error handling works properly
- Edge cases are handled
- Performance is reasonable

## 🛠️ Technical Details
### Message Format

**Request:**
```JSON
{
    "method": "floor",
    "params": [3.7],
    "param_types": ["float"],
    "id": 1
}
```
**Response:**
```JSON
{
    "results": 3,
    "result_type": "int",
    "id": 1
}
```

### Socket Communication

- Uses Unix domain sockets (`AF_UNIX`) for local communication
- JSON serialization for cross-language compatibility
- Request/response ID matching for concurrent requests

## 🎓 Learning Objectives

After building this project, you'll understand:

1. **RPC Concepts**: How remote procedure calls work
2. **Socket Programming**: Network communication basics
3. **Protocol Design**: Creating communication protocols
4. **Cross-Language Integration**: Making different languages work together
5. **Error Handling**: Robust distributed system practices
6. **Testing**: Validating distributed systems

## 🔧 Extending the System

Want to add more features? Try:

- Add more mathematical functions
- Implement authentication
- Add request logging
- Support multiple simultaneous clients
- Add function discovery/introspection
- Implement different transport protocols (TCP, HTTP)

📁 Project Structure
```txt
simple-rpc-system/
├── server/
│   ├── rpc_server.py      # Python RPC server
│   └── requirements.txt   # Python dependencies
├── client/
│   ├── rpc_client.js      # Node.js RPC client
│   └── package.json       # Node.js dependencies
├── examples/
│   └── test_calls.js      # Comprehensive test suite
└── README.md              # This file
```

## 🧠 **Key Learning Points**

1. **RPC = Remote Function Calls**: Like calling a function that lives on another computer
2. **Sockets = Communication Channel**: How programs talk to each other
3. **JSON = Common Language**: Both Python and Node.js understand JSON
4. **ID Matching = Conversation Tracking**: Makes sure answers match questions
5. **Error Handling = Robust Systems**: Things go wrong, plan for it!