import React, { useState, useEffect } from 'react';
import ListItem from '../components/ListItem';

const BookListPage = () => {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getBooks = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/');
        const data = await response.json();

        if (Array.isArray(data) && data.length > 0) {
          setBooks(data);
        } else {
          console.log('Invalid or Missing Data:', data);
          setBooks([]);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        setBooks([]);
      } finally {
        setLoading(false);
      }
    };

    getBooks(); 
  }, []); 

  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="product-container">
            {books.map((book) => (
            <ListItem key={book.id} book={book} />
            ))}
        </div>
      )}
    </div>
  );
};

export default BookListPage;
