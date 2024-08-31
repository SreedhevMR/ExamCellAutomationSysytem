
function redirectToPage() {
    const role = document.getElementById('role').value;
    let url = '';

    if (role === 'admin') {
        url = 'admin.html';
    } else if (role === 'student') {
        url = 'student.html';
    } else if (role === 'teacher') {
        url = 'teacher.html';
    }

    if (url) {
        window.location.href = url;
    } else {
        alert('Please select a role to continue.');
    }
        }
    