#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
    console.log('Missing size');
} else {
const m = number(process.argv[2]);
for (let i = 0; i < m; i++) {
    console.log('X'.repeat(m))
} 
}
}
