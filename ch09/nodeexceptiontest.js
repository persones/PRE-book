b = null;
b.do(); 

const fs = require('fs');
try {
  console.log(a[2])
} catch (error) {
  console.log('error', error)
}

const https = require('https');

b = null;
try {
  b.do(); 
} catch (error) {
  console.log('error', error) 
  // recover
}


//https.get('https://a1pi.nasa.gov/planetary/apod?api_key=DEMO_KEY', (resp) => {
https.get(3, (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(JSON.parse(data).explanation);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});

setInterval(() => {
  console.log('tick')
}, 1000);

