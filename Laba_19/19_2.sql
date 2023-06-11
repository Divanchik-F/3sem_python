SELECT books.id, title
FROM Books books
    JOIN Records records ON books.id = records.book_id
WHERE records.returning_date IS NULL; 

SELECT readers.name, books.title
FROM Books books
    JOIN Readers readers ON readers.id = records.reader_id
    JOIN Records records ON books.id = records.book_id;

SELECT author, COUNT(*) AS Quantity
FROM Books
GROUP BY author;