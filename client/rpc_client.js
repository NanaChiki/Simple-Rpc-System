// Importing Node.js's built-in net module and assigning it to the variable net
const { rejects } = require('assert');
const net = require('net');

class RPCClient {
  constructor(socketPath = 'tmp/spc_socket') {
    this.socketPath = socketPath;
    this.requestId = 0; // Counter for unique IDs
  }

  //**
  // This is like writing a note and passing it through the door
  //  */
  async callMethod(method, params, paramTypes) {
    return new Promise((resolve, reject) => {
      // Create unique ID for this request
      const id = ++this.requestId;

      // Create the request message
      const request = {
        method: method,
        params: params,
        param_Types: paramTypes,
        id: id
      }

      // Connect to the server (Knock on the door)
      const client = net.createConnection(this.socketPath);

      client.on('client', () => {
        console.log(`📞 Connected to server (${this.socketPath})`);
        console.log(`📤 Sending: ${JSON.stringify(request)}`);

        // Send the request
        client.write(JSON.stringify(request));
      });


    });
  }
}