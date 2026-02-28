document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('csv-upload');
    const filenameText = document.getElementById('filename-text');
    const btnSubmit = document.getElementById('btn-submit');
    const errorMessage = document.getElementById('error-message');

    // Listen for file selection
    fileInput.addEventListener('change', (e) => {
        errorMessage.style.display = 'none'; // Hide error if user selects a file after an error

        if (e.target.files && e.target.files.length > 0) {
            const fileName = e.target.files[0].name;
            filenameText.textContent = fileName;
        } else {
            filenameText.textContent = '';
        }
    });

    // Handle submit
    btnSubmit.addEventListener('click', (e) => {
        e.preventDefault();

        const isFileSelected = fileInput.files && fileInput.files.length > 0;

        if (!isFileSelected) {
            // Show error message
            errorMessage.style.display = 'block';
        } else {
            // Store filename in sessionStorage and redirect
            const fileName = fileInput.files[0].name;
            sessionStorage.setItem('uploadedFile', fileName);
            // Assuming dashboard.html is in the same directory
            window.location.href = 'dashboard.html';
        }
    });
});
