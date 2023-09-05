from transformers import pipeline

# sentiment analysis
sent = pipeline("sentiment-analysis")
sent("I've been waiting for a HuggingFace course my whole life.")