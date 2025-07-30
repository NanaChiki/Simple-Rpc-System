// Importing Node.js's built-in net module and assigning it to the variable net
const { rejects } = require('assert');
const net = require('net');

class RPCClient {
  constructor(socketPath = "/tmp/rpc_socket") {
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

      client.on('connect', () => {
        console.log(`📞 Connected to server (${this.socketPath})`);
        console.log(`📤 Sending: ${JSON.stringify(request)}`);

        // Send the request
        client.write(JSON.stringify(request));
      });

      client.on('data', (data) => {
        console.log(`📥 Received: ${data.toString()}`);
        
        try {
          const response = JSON.parse(data);

          // Check if there was an error
          if (response.error) {
            reject(new Error(response.error));
          } else {
            resolve(response.results);
          }
        } catch (error) {
          reject(new Error(`Failed to parse response: ${error.message}`));
        }

        client.end();
      });

      client.on('error', (error) => {
        console.error(`❌ Connection error: ${error.message}`);
        reject(error);
      });

      client.on('close', () => {
        console.log('👋 Connection closed');
      });
    });
  }

  /**
   * Helper methods for each RPC function - makes it easier to use
   */
  async floor(x) {
    return await this.callMethod('floor', [x], ['float']);
  }

  async nroot(x, n) {
    return await this.callMethod('nroot', [x, n], ['int', 'int']);
  }

  async reverse(s) {
    return await this.callMethod('reverse', [s], ['str']);
  }

  async validAnagram(s1, s2) {
    return await this.callMethod('validAnagram', [s1, s2], ['str', 'str']);
  }

  async sort(strArr) {
    return await this.callMethod('sort', [strArr], ['list']);
  }
}

module.exports = RPCClient;

// If this file run directly, show some examples
if (require.main === module) {
  async function runExamples() {
    const client = new RPCClient();

    console.log('🧪 Testing RPC Client...\n');

    try {
      // Test floor
      console.log('1️⃣ Testing floor(3.7):')
      const floorResult = await client.floor(3.7);
      console.log(`  Result: ${floorResult}\n`);

      // Test reverse
      console.log('2️⃣ Testing reverse("hello"):')
      const reverseResult = await client.reverse("hello");
      console.log(`  Result: ${reverseResult}\n`);

      // Test sort
      console.log('3️⃣ Testing sort(["banana", "apple", "cherry"])');
      const sortResult = await client.sort(["banana", "apple", "cherry"]);
      console.log(`  Result: ${sortResult}\n`);

      // Test valid anagram
      console.log('4️⃣ Testing validAnagram("listen", "silent")');
      const anagramResult = await client.validAnagram("listen", "silent");
      console.log(`  Result: ${anagramResult}\n`);

      // Test nroot
      console.log('5️⃣ Testing nroot(2, 9) (square root of 9):');
      const nrootResult = await client.nroot(2, 9);
      console.log(`  Result: ${nrootResult}\n`);
    } catch (error) {
      console.error(`❌ Error: ${error.message}`);
    }
  }

  runExamples();
}