import './App.css';
import Header from './components/Header'
import ListItem from './components/ListItem';
import Nav from './components/Nav';
import BookListPage from './pages/BookListPage'

function App() {
  return (
    <div className="App">
    <Nav />
    <div className="content-container">
      <Header />
      <BookListPage />
      <ListItem />
    </div>
  </div>
  );
}

export default App;
