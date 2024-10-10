function Palindrome(mystring){ 

   var input = mystring.replace(/[^A-Z0-9]/ig, "").toLowerCase();

   var reversedInput = input.spilt('').reverse().join('');

   if (input === reversedInput){
      document.write("<div>"+mystring+"is a palindrome <div>")
    }
   else {
       document.write("<div>" + myString + " is not a palindrome <div>")
   }

}
Palindrome("madam")