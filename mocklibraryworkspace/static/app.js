document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/books')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('books-table-body');
            data.forEach(book => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${book.title}</td>
                    <td>${book.author}</td>
                    <td>${book.publisher}</td>
                    <td>${book.publishing_date}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching books:', error));
});