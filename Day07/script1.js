


var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["facName"] = document.getElementById("facName").value;
  formData["facAge"] = document.getElementById("facAge").value;
  formData["facMobileNumber"] = document.getElementById("facMobileNumber").value;
  formData["facMailId"] = document.getElementById("facMailId").value;
  formData["facCource"] = document.getElementById("facCourse").value;
  return formData;
}
function resetForm() {
  document.getElementById("facName").value = "";
  document.getElementById("facAge").value = "";
  document.getElementById("facMobileNumber").value = "";
  document.getElementById("facMailId").value = "";
  document.getElementById("facCourse").value = "";
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("faclist")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.facName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.facAge;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.facMobileNumber;
  cell4 = newRow.insertCell(3);
  cell4.innerHTML = data.facMailId;
  cell5 = newRow.insertCell(4);
  cell5.innerHTML = data.facCourse;
  cell6 = newRow.insertCell(5);
  cell6.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("facName").value=selectedRow.cells[0].innerHTML;
document.getElementById("facAge").value=selectedRow.cells[1].innerHTML;
document.getElementById("facMobileNumber").value=selectedRow.cells[2].innerHTML;
document.getElementById("facMailId").value=selectedRow.cells[3].innerHTML;
document.getElementById("facCourse").value=selectedRow.cells[4].innerHTML;}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.facName;
selectedRow.cells[1].innerHTML=formData.facAge;
selectedRow.cells[2].innerHTML=formData.facMobileNuber;
selectedRow.cells[3].innerHTML=formData.facMailId;
selectedRow.cells[4].innerHTML=formData.facCourse;
}
function onDelete(td)
{
if(confirm("are you want to delete this record")){
  row=td.parentElement.parentElement;
  document.getElementById("faclist").deleteRow(row.rowIndex);
  resetForm();
}
}

function isValid(){
var a=document.getElementById("facName").value;
// var  b = document.getElementById("facAeg").value;
// var c= document.getElementById("facMobileNumber").value;
// var d= document.getElementById("facMailId").value;
//  var e= document.getElementById("facCourse").value;
if(a==""|| a==null ){return false;}
else
{return true;}

}
 