#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
 print() {
 for (let i = 0; i < this.width; i++) {
     console.log('X'.repeat(this.height));
}
module.exports = Rectangle;
