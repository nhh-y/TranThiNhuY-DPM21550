import { Link } from 'react-router-dom';

function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Hệ thống hỗ trợ giáo viên ra đề kiểm tra</h1>
      <nav>
        <ul>
          <li><Link to="/login">Đăng nhập</Link></li>
          <li><Link to="/create-question">Nhập câu hỏi</Link></li>
          <li><Link to="/create-exam">Tạo đề kiểm tra</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;