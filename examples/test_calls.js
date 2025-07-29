const RPCClient = require('../client/rpc_client');

async function comprehensiveTest() {
  const client = new RPCClient();

  console.log('🧪 Comprehensive RPC Testing Suite\n');
  console.log('Make sure the Python server is running first!\n')

  const tests = [
    {
      name: 'Floor Function',
      test: () => client.floor(3.9),
      expected: 3
    },
    // {
    //   name: 'Floor with negative',
    //   test: () => client.floor(-2.7),
    //   expected: -3
    // },
    // {
    //   name: 'Square root (nroot)',
    //   test: () => client.nroot(2, 16),
    //   expected: 4
    // },
    // {
    //   name: 'Cube root (nroot)',
    //   test: () => client.nroot(3, 27),
    //   expected: 3
    // },
    // {
    //   name: 'Reverse string',
    //   test: () => client.reverse('JavaScript'),
    //   expected: 'tpircSavaJ'
    // },
    // {
    //   name: 'Valid anagram(true)',
    //   test: () => client.validAnagram('listen', 'silent'),
    //   expected: true
    // },
    // {
    //   name: 'Valid anagram (false)',
    //   test: () => client.validAnagram('hello', 'world'),
    //   expected: false
    // },
    // {
    //   name: 'Sort strings',
    //   test: () => client.sort(['zebra','apple','banana']),
    //   expected: ['apple','banana','zebra']
    // }
  ];

  let passed = 0;
  let failed = 0;

  for (const test of tests) {
    try {
      console.log(`🔍Testing: ${test.name}`);
      try {
        console.log('start');
        const result = await test.test();
        console.log(result);
      } catch (e) {
        console.error("error:", e);
      }
      // const result = await test.test();

      const success = JSON.stringify(result) === JSON.stringify(test.expected);
      if (success) {
        console.log(`   ✅PASS: Got ${JSON.stringify(result)}`);
        passed++;
      } else {
        console.log(`   ❌FAIL: Expected ${JSON.stringify(test.expected)}, got ${JSON.stringify(result)}`);
        failed++;
      }

    } catch (error) {
      console.log(`   ❌ Error: ${error.message}`);
      failed++;
    }

    console.log('');
  }

  console.log(`\n📊 Test Results: ${passed} passed, ${failed} failed`);
  if (failed == 0) {
    console.log('🎉 All tests passed! Your RPC system works perfectly!');
  }
}

// Error handling test
async function errorTest() {
  const client = new RPCClient();

  console.log('🚫 Testing error handling...\n');

  try {
    await client.callMethod('nonexistent', [], []);
  } catch (error) {
    console.log(`✅ Error handling works: ${error.message}\n`);
  }
}

async function runAllTests() {
  await comprehensiveTest();
  await errorTest();
}

runAllTests();