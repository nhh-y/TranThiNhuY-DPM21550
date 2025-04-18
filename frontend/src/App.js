import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import CreateQuestion from './pages/CreateQuestion';
import CreateExam from './pages/CreateExam';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/create-question" element={<CreateQuestion />} />
        <Route path="/create-exam" element={<CreateExam />} />
      </Routes>
    </Router>
  );
}

export default App;