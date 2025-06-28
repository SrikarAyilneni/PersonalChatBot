import os
import google.generativeai as genai

class Chat:
    def __init__(self):
        pass
        
    def bot(self, prompt):
        api_key = os.environ.get('GENAI')
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content({
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        })

        rs = response.text
        try:
            idx = rs.index("</think>")+8
            rs = rs[idx:]
        except ValueError:
            pass  # If </think> tag is not found, return the full response
        return rs
