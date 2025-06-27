Function validateName(name) {
    const namePattern=/^[a-zA-Z\s'-]+s/;
    return namepattern.test(name);
  }
Function validateMobileNumber(MobileNumber) {
    const namePattern=/^[0-9]\b{9} $/;
    return Mobilepattern.test(MobileNumber);
  }
Function containsOnlyDigit(str) {
    const regex=/^\d+$/;
    return regex.test(str);
  }
Function containsOnlyAlphabets(str) {
    const regex=/^[a-zA-Z]+$/;
    return regex.test(str);
  }
Function containsOnlyAlphanumaric(str) {
    const regex=/^[a-zA-Z0-9]+$/;
    return regex.test(str);
  }