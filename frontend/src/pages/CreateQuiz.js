import { useState, useEffect } from 'react';
import API from '../api';

function CreateExam() {
  const [name, setName] = useState('');
  const [duration, setDuration] = useState('');
  const [allQuestions, setAllQuestions] = useState([]);
  const [selectedQuestions, setSelectedQuestions] = useState([]);

  // Lấy danh sách câu hỏi từ backend
  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await API.get('questions/');
        setAllQuestions(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchQuestions();
  }, []);

  const handleQuestionSelect = (questionId) => {
    setSelectedQuestions(prev => {
      if (prev.includes(questionId)) {
        return prev.filter(id => id !== questionId);
      } else {
        return [...prev, questionId];
      }
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await API.post('exams/', { name, duration, questions: selectedQuestions });
      alert('Tạo đề kiểm tra thành công!');
      setName('');
      setDuration('');
      setSelectedQuestions([]);
    } catch (error) {
      console.error(error);
      alert('Tạo đề kiểm tra thất bại!');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Tạo đề kiểm tra</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <input 
            type="text" 
            placeholder="Tên đề kiểm tra" 
            value={name} 
            onChange={e => setName(e.target.value)} 
            required 
          />
        </div>
        <div>
          <input 
            type="number" 
            placeholder="Thời gian làm bài (phút)" 
            value={duration} 
            onChange={e => setDuration(e.target.value)} 
            required 
          />
        </div>
        <div>
          <h3>Chọn câu hỏi cho đề kiểm tra</h3>
          {allQuestions.length === 0 && <p>Chưa có câu hỏi nào!</p>}
          {allQuestions.map(question => (
            <div key={question.id}>
              <label>
                <input 
                  type="checkbox" 
                  checked={selectedQuestions.includes(question.id)} 
                  onChange={() => handleQuestionSelect(question.id)} 
                />
                {question.content} ({question.question_type})
              </label>
            </div>
          ))}
        </div>
        <button type="submit">Tạo đề kiểm tra</button>
      </form>
    </div>
  );
}

export default CreateExam;