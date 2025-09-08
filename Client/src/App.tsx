import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Components/Login/Login';
import { SignUp } from './Components/SignUp/SignUp';
import Navbar from './Components/Navbar/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route element={<Login />}>
          <Route path="/" />
          <Route path="/login" />
        </Route>
        <Route path='/SignUp' element={<SignUp />} />
      </Routes>
    </Router>
  );
}

export default App;

