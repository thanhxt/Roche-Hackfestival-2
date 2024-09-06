// Handle form submission for CO2 calculation
document.getElementById('co2Form').addEventListener('submit', async function(event) {
    event.preventDefault();  // Prevent the default form submission behavior

    const employeeName = document.getElementById('employeeName').value;
    const co2Waste = document.getElementById('co2Waste').value;

    // Send POST request to the backend to save the data
    const response = await fetch('http://127.0.0.1:5000/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ employeeName, co2Waste })
    });

    if (response.ok) {
        alert('Employee CO2 data submitted successfully!');
    } else {
        alert('Error submitting the form');
    }
});

// Handle redirection to the Employees page when the "View All Employees" button is clicked
document.getElementById('viewEmployeesBtn').addEventListener('click', function() {
    window.location.href = '/employees';  // Redirect to the /employees route
});
