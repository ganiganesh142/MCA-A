function onFormSubmit() {
  const name = document.getElementById("Name").value.trim();
  const age = document.getElementById("Age").value.trim();
  const mobile = document.getElementById("MobileNumber").value.trim();
  const email = document.getElementById("E-MailId").value.trim();
  const course = document.getElementById("Course").value.trim();

  if (isValid(name, age, mobile, email, course)) {
    alert("Your details are saved successfully!");
    clearForm();
  }
}

function isValid(Name, Age, MobileNumber, E-mail, Course) {
  // Name: Only alphabets and spaces
  const namePattern = /^[a-zA-Z\s]+$/;
  if (!namePattern.test(name)) {
    alert("Please enter a valid Name (letters and spaces only).");
    return false;
  }

  // Age: Must be number between 01 and 100
  const ageValue = parseInt(age);
  if (isNaN(ageValue) || ageValue <01 || ageValue > 100) {
    alert("Please enter a valid Age between 01 and 100.");
    return false;
  }

  // Mobile: 10-digit number starting with 6-9
  const mobilePattern = /^[6-9]\d{9}$/;
  if (!mobilePattern.test(mobile)) {
    alert("Please enter a valid 10-digit Mobile number starting with 6, 7, 8, or 9.");
    return false;
  }

  // Email: Standard email pattern
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    alert("Please enter a valid Email ID.");
    return false;
  }

  // Course: Only letters and spaces
  const coursePattern = /^[a-zA-Z\s]+$/;
  if (!coursePattern.test(course)) {
    alert("Please enter a valid Course name (letters and spaces only).");
    return false;
 }
  return true;
}
function clearForm() {
  document.getElementById("Name").value = "";
  document.getElementById("Age").value = "";
  document.getElementById("MobileNumber").value = "";
  document.getElementById("E-MailId").value = "";
  document.getElementById("Course").value = "";
}
}