// Function to show content depending on menu item clicked
function showTab(tabName) {
    const tabs = document.querySelectorAll(".tab-content");
    tabs.forEach(tab => {
        tab.style.display = "none";
    });

    const activeTab = document.getElementById(tabName);
    if (activeTab) {
        activeTab.style.display = "block";
    }
}

//Function to update menu item formatting when clicked
// Get all the tab links
const tabLinks = document.querySelectorAll('.tab-selector');

// Function to remove bold styling from all links
function clearStyling() {
    tabLinks.forEach(link => {
        link.style.fontWeight = 'bold';
        link.style.color = 'white';
    });
}

// Event listeners for each tab link
tabLinks.forEach(link => {
    link.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default link behavior

        // Remove bold styling from all links
        clearStyling();

        // Add bold styling to the clicked link
        this.style.fontWeight = 'bold';
        this.style.color = 'yellow';
    });
});

// Function to update the content of the <p> tag with the current time
function updateCurrentTime() {
    const currentTimeElement = document.getElementById('current-time');
    const currentTime = new Date(); // Get the current date and time
    const formattedTime = currentTime.toLocaleTimeString(); // Format the time as a string
    currentTimeElement.textContent = `The current time is ${formattedTime}`; // Update the <p> tag's content
}

// Add an event listener to run the function when the page finishes loading
window.addEventListener('load', updateCurrentTime);


// JavaScript code to handle the search functionality
document.addEventListener("DOMContentLoaded", function () {
    // Get references to the date input fields and the search button
    const startDateInput = document.getElementById('start-date-input');
    const endDateInput = document.getElementById('end-date-input');
    const searchButton = document.getElementById('search-button');

    // Event handler for the search button
    searchButton.addEventListener('click', function () {
        // Get the selected start and end dates
        const startDate = startDateInput.value;
        const endDate = endDateInput.value;

        // Perform the date range search based on the selected dates
        // You can add your search logic here

        // For this example, we'll just display the selected dates
        alert(`Start Date: ${startDate}\nEnd Date: ${endDate}`);
    });
});

// Templates section code
// Get references to the text editor, cancel button, and save button
    const templateEditor = document.getElementById('template-editor');
    const cancelButton = document.getElementById('cancel-button');
    const saveButton = document.getElementById('save-button');

    // Event handler for the cancel button
    cancelButton.addEventListener('click', function () {
        // Clear the text editor
        templateEditor.value = '';
    });

    // Event handler for the save button
    saveButton.addEventListener('click', function () {
        // Get the edited template from the text editor
        const editedTemplate = templateEditor.value;

        // You can perform further actions here, such as saving the template to a database or displaying it elsewhere.

        // For this example, we'll simply display an alert with the edited content.
        alert('Template saved:\n' + editedTemplate);
    });

showTab('dashboard');