import google.generativeai as genai
API_KEY = 'AIzaSyCgE8tZoTw8DrT4z7_GyQ_Yg8kkcPlQjbw'

genai.configure(api_key=API_KEY)

def generate_questions_from_text(text):
    model = genai.GenerativeModel(model_name='models/gemini-1.0-pro')
    prompt = f"Tạo 5 câu hỏi trắc nghiệm có đáp án từ nội dung sau:\n\n{text}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Lỗi khi sinh câu hỏi: {e}"
