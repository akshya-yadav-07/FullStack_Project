import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Login from './components/Login';
import Signup from './components/Signup'
import Dashboard from './components/Dashboard'
function App() {
  return (
    <div className="App">
       <Router>
        <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Signup />} />
        <Route path="/dashboard" element={<Dashboard />} /> {/* Protect this route */}
        </Routes>
       </Router>
    </div>
  );
}

export default App;
