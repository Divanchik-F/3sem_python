CREATE TABLE Books (
    id INTEGER PRIMARY KEY,
    author TEXT,
    title TEXT,
    publish_year INTEGER 
);

INSERT INTO Books (author, title, publish_year)
VALUES
    ("Marcel Proust", "In Search of Lost Time", 1913),
    ("James Joyce", "Ulysses", 1922),
    ("Joanne Rowling", "Harry potter and the philosopher's stone", 1997),
    ("John Ronald Reuel Tolkien", "The Lord of the Rings: The Two Towers", "1954"),
    ("John Ronald Reuel Tolkien", "The Lord of the Rings: The Fellowship of the Ring", "1954");

CREATE TABLE Readers (
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO Readers (name)
VALUES
    ("Dwayne Johnson"),
    ("Kevin Hart"),
    ("Peter Parker");

CREATE TABLE Records (
    id INTEGER PRIMARY KEY,
  	reader_id INTEGER,
  	book_id INTEGER,
    taking_date TEXT,
    returning_date TEXT,
    FOREIGN KEY (reader_id) REFERENCES Reader (id),
    FOREIGN KEY (book_id) REFERENCES Books (id)
);

INSERT INTO Records (reader_id, book_id, taking_date, returning_date)
VALUES
    (1, 1, "2017-12-05 10:03:00", "2018-03-06 17:34:00"),
    (1, 3, "2022-03-09 15:32:00", NULL),
    (2, 2, "2021-10-10 12:46:00", "2021-05-12 14:06:00"),
    (3, 4, "2023-03-10 12:46:00", NULL);