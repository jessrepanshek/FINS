// Function to toggle active class based on URL hash
function toggleActiveTab() {
    var currentHash = window.location.hash;
    var createAccountTab = document.getElementById("createAccountTab");
    var loginTab = document.getElementById("loginTab");

    if (currentHash === "#loginTab") {
        createAccountTab.classList.remove("active");
        loginTab.classList.add("active");
        document.getElementById("createAccountForm").style.display = "none";
        document.getElementById("loginForm").style.display = "block";
    } else {
        createAccountTab.classList.add("active");
        loginTab.classList.remove("active");
        document.getElementById("createAccountForm").style.display = "block";
        document.getElementById("loginForm").style.display = "none";
    }
}

// Add event listener to handle hash changes
window.addEventListener("hashchange", toggleActiveTab);

// Add click listener to handle tab changes
document.getElementById("createAccountTab").addEventListener("click", function () {
    document.getElementById("createAccountTab").classList.add("active");
    document.getElementById("loginTab").classList.remove("active");
    document.getElementById("createAccountForm").style.display = "block";
    document.getElementById("loginForm").style.display = "none";
});

document.getElementById("loginTab").addEventListener("click", function () {
    document.getElementById("loginTab").classList.add("active");
    document.getElementById("createAccountTab").classList.remove("active");
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("createAccountForm").style.display = "none";
});

// Function to clear input fields
function clearForm() {
    document.getElementById("userName").value = '';
    document.getElementById("email").value = '';
    document.getElementById("confirmEmail").value = '';
    document.getElementById("passwordHash").value = '';
    document.getElementById("confirmPassword").value = '';
}

// Add a click event listener to the "Cancel" button
document.getElementById("clearFormButton").addEventListener("click", clearForm);

// Initial toggle based on the current URL hash
toggleActiveTab();