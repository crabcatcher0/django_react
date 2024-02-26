import React from 'react';

const ListItem = ({ book }) => {
  // Check if 'book' is defined and has expected properties
  if (!book || !book.book_name || !book.description || !book.image) {
    return null;
  }

  return (
     <div className="custom-card">
        <div className="card-body">
        <img src={book.image} alt={book.book_name} className="img-fluid" />
        <h5 className="card-title">{book.book_name}</h5>
        <p className="card-text">{book.description}</p>
        </div>
     </div>
    
  );
};
 
export default ListItem;
