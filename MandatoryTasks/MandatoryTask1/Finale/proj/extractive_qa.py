import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

model_path = r"" #fine tuned model path

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

qa_pipeline = pipeline(
    "question-answering",
    model = model,
    tokenizer = tokenizer,
    device = device,
    return_offsets = False
)


def predict_answer(question, context):
    results = qa_pipeline(question = question, context = context)
    if results["score"]<0.1:
        return{
            "answer": "Could not answer",
            "score": results["score"]
        }
    return{
        "answer": results["answer"],
        "score": results["score"]
    }


