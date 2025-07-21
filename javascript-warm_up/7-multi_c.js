#!/usr/bin/node
#!/usr/bin/env node
const x = process.argv[2];
const num = parseInt(x);

if (isNaN(num) || x === undefined) {
  console.log("Missing number of occurrences");
} else if (num > 0) {
  for (let i = 0; i < num; i++) {
    console.log("C is fun");
  }
}
