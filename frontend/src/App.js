import './App.css';
import MainContainer from './components/MainContainer';
import { Route, Routes} from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="/" element={<h1>Home</h1>}></Route>
      <Route path="/about" element={<h1>About</h1>}></Route>
      <Route path="/contact" element={<h1>Contacts</h1>}></Route>
    </Routes>
  );
}

export default App;
