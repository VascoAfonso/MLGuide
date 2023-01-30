import logo from './logo.svg';
import './App.css';
import MainContainer from './components/MainContainer';

function App() {
  return (
    <Routes>
      <Route path="/" element={<MainContainer />}></Route>
      <Route path="/about" element={<h1>About</h1>}></Route>
      <Route path="/contact" element={<h1>Contacts</h1>}></Route>
    </Routes>
  );
}

export default App;
