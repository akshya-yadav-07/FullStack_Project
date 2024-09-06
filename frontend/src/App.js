import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Login from './components/Login';
import Signup from './components/Signup'

function App() {
  return (
    <div className="App">
       <Router>
        <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Signup />} />
        </Routes>
       </Router>
    </div>
  );
}

export default App;
