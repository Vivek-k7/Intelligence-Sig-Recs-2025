import torch
from transformers import MarianMTModel, MarianTokenizer, pipeline
from extractive_qa import predict_answer


model_path = r""  # fine tuned model path

tokenizer = MarianTokenizer.from_pretrained(model_path)
model = MarianMTModel.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

translator_pipeline = pipeline(
    "translation",
    model = model,
    tokenizer = tokenizer,
    device = device
)

def predict_translate(question, context, src_lang, tgt_lang):
    payload = predict_answer(question, context)
    input_text = payload['answer']
    translated = translator_pipeline(input_text, src_lang = src_lang, tgt_lang = tgt_lang)
    return translated[0]["translation_text"]

