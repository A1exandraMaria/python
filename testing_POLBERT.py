import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

class QnA:
    def __init__(self):
        # Use POLBERT model
        self.model_name = 'dkleczek/bert-base-polish-uncased-v1'
        self.model = AutoModelForQuestionAnswering.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def get_answer(self, question, context):
        # Encode the question and context
        inputs = self.tokenizer.encode_plus(question, context, return_tensors="pt", add_special_tokens=True, truncation=True, max_length=512)
        input_ids = inputs["input_ids"].tolist()[0]

        # Get model outputs
        outputs = self.model(**inputs)
        answer_start_scores, answer_end_scores = outputs.start_logits, outputs.end_logits

        # Determine the start and end positions of the answer
        answer_start = torch.argmax(answer_start_scores, dim=1).item()
        answer_end = torch.argmax(answer_end_scores, dim=1).item() + 1

        # Convert tokens to the answer string
        answer = self.tokenizer.convert_tokens_to_string(self.tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
        return answer

# Load context from a file
with open('context.txt', 'r', encoding='utf-8') as file:
    context = file.read()

# Example question
question = "czy chomiki są malutkie i urocze?"

# Initialize and test the QnA system
qna_system = QnA()
print("Answer:", qna_system.get_answer(question, context))
