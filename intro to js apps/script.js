var choice = prompt("Welcome to Area Calculator. \n Please Enter your Choice. \n1.Area of Rectangle. \n2.Area of Triangle. \n3.Area of Circle. \n4.Area of Parallelogram\n5.Area of square.");
if (choice=='1'){
var l = prompt('enter the length')
var b = prompt('enter breadth')
var result = Number(1) * Number(b)
alert ('The Area is '+ result)
}
if (choice == '2') {
var h = prompt('enter the height')
var b = prompt('enter base')
var result = Number(h) * Number(b)/2
alert('The Area is ' + result)
}
if (choice == '3') {
var r = prompt('enter the radius')
var result = 3.14*Number(r)*Number(r)
alert('The Area is ' + result)
}
if (choice == '4') {
var h = prompt('Enter the height')
var cb = prompt('Enter the corresponding base')
var result = Number(h) * Number(cb)
alert('The Area is ' + result)
}
if (choice == '5') {
var l = prompt('enter the length')
var b = prompt('enter breadth')
var result = Number(l) * Number(b)
alert('The Area is ' + result)
}