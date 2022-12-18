CREATE TABLE books
(
    id                              INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    title                           VARCHAR,
    author                          VARCHAR,
    lang                            VARCHAR(100),
    document_size                   VARCHAR(200),
    year_of_publication             INTEGER,
    publishing_house                VARCHAR(200),
    country                         VARCHAR(200),
    number_of_pages                 INTEGER,
    availability_in_the_library     VARCHAR(50),
    availability_in_electronic_form VARCHAR(50),
    added                           VARCHAR(200),
    classification_id               INT,
    document_type                   VARCHAR(200),
    link_to_book                    VARCHAR(200),
    sub_category                    INT,
    global_category                 INT
);


drop table books;
INSERT INTO books (title, author, lang, document_size, year_of_publication, publishing_house, country,
                   number_of_pages, availability_in_the_library, availability_in_electronic_form, added, classification,
                   document_type, link_to_book)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?), ('2', 'a', 'a',  'a', 0,  'a',  'a', 9,  'a',  'a',  'a',  'a', 'a', 'a');


select * from books WHERE title='Язык программирования С++. Лекции и упражнения. 5-е издание';


SELECT * FROM books WHERE title LIKE '%C++%'; -- Engl 11
SELECT * FROM books WHERE title LIKE '%С++%'; -- RU   10


SELECT * FROM books WHERE title LIKE '%C#%';
SELECT * FROM books WHERE title LIKE '%С#%';

select * from books;
select * from books_final;


-- UPDATE Person Set fullName=?, yearOfBirth=? WHERE person_id=?
-- SELECT classification, COUNT(*) as count FROM books  GROUP BY classification ;


UPDATE books SET title = REPLACE(title ,'С++', 'C++' ) WHERE title LIKE '%С++%';
UPDATE books SET title = REPLACE(title ,'С#', 'C#' ) WHERE title LIKE '%С#%';


UPDATE books SET title='Самоучитель C++' where id =67;

UPDATE books Set title=? WHERE id=? ('Операционная система Linux!!!', 3);
select * from books WHERE id=364;


CREATE TABLE query(
      id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
      search_string VARCHAR,
      string_books_id VARCHAR

);

select * from query;

SELECT * FROM books WHERE LOWER(title) LIKE 'dfdfdf';



CREATE TABLE users(
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY

);

SELECT * FROM books WHERE LOWER(title) LIKE '%c++%';

SELECT * FROM books WHERE LOWER(title) LIKE '%c++%';

drop TABLE global_category;
drop table sub_category;


select * from global_category;
CREATE TABLE global_category(
    id                  INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    category_title      VARCHAR UNIQUE NOT NULL
);

CREATE TABLE sub_category(
    id                  INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    sub_title           VARCHAR UNIQUE NOT NULL ,
    global_id           INT references global_category(id)
);

select * from sub_category;

INSERT INTO global_category (category_title) values('андрей');
INSERT INTO sub_category (sub_title, global_id) values('андрей_sub', 1);
INSERT INTO sub_category (sub_title, global_id) values('андрей_sub2', 1);


SELECT * from sub_category WHERE global_id = 2

SELECT * from global_category