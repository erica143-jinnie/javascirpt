var myForm = document.getElementById("myForm");
var myInput = document.getElementById("myInput");
var myItem = document.getElementById("myItem");

myform.addEventListener("submit",
function(event){
   event.preventDefault()
createItem(myInput.value)
})
 function createItem(InputItems){
   var items = <li>${InputItems}
   <button onclick ="deleteElement(this)">Delete</button>
   myItem.insertAdjacentHTML("beforeend",items)
   myInput.value = ""
   myInput.focus()
 }
 function deleteElement(ElementtoDelete){
   ElementtoDelete.parentElement.remove()
  }