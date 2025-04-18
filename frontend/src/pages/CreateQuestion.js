import { useState } from 'react';
import API from '../api';

function CreateQuestion() {
  const [content, setContent] = useState('');
  const [questionType, setQuestionType] = useState('MCQ'); // 'MCQ' hoặc 'Essay'
  const [answer, setAnswer] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Nếu cần, bạn có thể thêm dữ liệu khác theo model
      await API.post('questions/', { content, question_type: questionType, answer });
      alert('Thêm câu hỏi thành công!');
      setContent('');
      setAnswer('');
    } catch (error) {
      console.error(error);
      alert('Thêm câu hỏi thất bại!');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Nhập câu hỏi</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <textarea 
            placeholder="Nội dung câu hỏi" 
            value={content} 
            onChange={e => setContent(e.target.value)} 
            required 
          />
        </div>
        <div>
          <select value={questionType} onChange={e => setQuestionType(e.target.value)}>
            <option value="MCQ">Trắc nghiệm</option>
            <option value="Essay">Tự luận</option>
          </select>
        </div>
        <div>
          <input 
            type="text" 
            placeholder="Đáp án (nếu trắc nghiệm)" 
            value={answer} 
            onChange={e => setAnswer(e.target.value)} 
          />
        </div>
        <button type="submit">Lưu câu hỏi</button>
      </form>
    </div>
  );
}

export default CreateQuestion;