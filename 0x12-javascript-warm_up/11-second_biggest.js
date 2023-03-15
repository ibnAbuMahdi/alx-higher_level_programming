#!/usr/bin/node

const args = process.argv;
let f = Number.NEGATIVE_INFINITY; let s = Number.NEGATIVE_INFINITY;

for (let i = 0; i < args.length; i++) {
  const num = Number(args[i]);

  if (num > f) {
    s = f;
    f = num;
  } else if (num > s && num < f) {
    s = num;
  }
}

if (s === Number.NEGATIVE_INFINITY) {
  console.log(0);
} else {
  console.log(s);
}
