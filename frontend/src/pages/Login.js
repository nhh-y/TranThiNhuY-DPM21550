import { useState } from 'react';
import API from '../api';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await API.post('auth/token/', { username, password });
      // Lưu token vào localStorage
      localStorage.setItem('token', response.data.access);
      alert('Đăng nhập thành công!');
      navigate('/');
    } catch (error) {
      console.error(error);
      alert('Đăng nhập thất bại!');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Đăng nhập</h2>
      <form onSubmit={handleLogin}>
        <div>
          <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
        </div>
        <div>
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required />
        </div>
        <button type="submit">Đăng nhập</button>
      </form>
    </div>
  );
}

export default Login;