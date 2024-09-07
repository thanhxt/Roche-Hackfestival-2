// Handle form submission for CO2 calculation
document.getElementById('searchEmployee').addEventListener('submit', async function(event) {
    event.preventDefault();  // Prevent the default form submission behavior

    const employeeName = document.getElementById('employeeName').value;

    // Send GET request to the backend to get Data
    const response = await fetch('http://127.0.0.1:5000/calculate', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ employeeName })
    });

    if (response.ok) {
        alert('Employee CO2 data submitted successfully!');
    } else {
        alert('Error submitting the form');
    }
});

function consumption(employee) {
    return employee.distance + employee.food_emission + employee.room_emi;
}

// get Top employees
document.getElementById('fetchEmployeesBtn').addEventListener('click', async function() {
    // Send GET request to fetch employee data
    const response = await fetch('http://127.0.0.1:5000/employees', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        const employees = await response.json();

        // Sort the employees basen on total CO2 consumption in descending order
        const sortedEmployees = employees.sort((a, b) => {
            return consumption(b) - consumption(a);
        })

        // Get the top 10 employees
        const topEmployees = sortedEmployees.slice(0,10);

        // Display the employee data in the "employeeData" div
        const topEmployeeDiv = document.getElementById('topEmployeeData');
        topEmployeeDiv.innerHTML = '<h3>Top 10 Employees:</h3>';
        topEmployees.forEach(employee => {
            const totalconsumption = consumption(employee)
            topEmployeeDiv.innerHTML += `
                <p></strong> ${employee.name}`;
        });
    } else {
        alert('Error fetching employee data');
    }
});

// trigger button to fetch employee2 with 1
document.getElementById('fetchingEmployees').addEventListener('click', function() {
    // Send a POST request to the Flask backend
    fetch('/trigger-function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // You can send data to the backend if needed
    })
    .then(response => response.json())
    .then(data => {
        // Update the page with the response
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
})


document.getElementById('fetchingEmployees').addEventListener('click', function() {
    // Send a POST request to the Flask backend
    fetch('/trigger-function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // You can send data to the backend if needed
    })
    .then(response => response.json())
    .then(data => {
        // Update the page with the response
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
})

document.getElementById('fetchingEmployees').addEventListener('click', function() {
    // Send a POST request to the Flask backend
    fetch('/trigger-function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // You can send data to the backend if needed
    })
    .then(response => response.json())
    .then(data => {
        // Update the page with the response
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
})

document.getElementById('fetchingEmployees').addEventListener('click', function() {
    // Send a POST request to the Flask backend
    fetch('/trigger-function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})  // You can send data to the backend if needed
    })
    .then(response => response.json())
    .then(data => {
        // Update the page with the response
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
})



// Handle redirection to the Employees page when the "View All Employees" button is clicked
document.getElementById('viewEmployeesBtn').addEventListener('click', function() {
    window.location.href = '/employees';  // Redirect to the /employees route
});