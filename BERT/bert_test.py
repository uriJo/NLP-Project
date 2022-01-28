from transformers import BertModel, BertTokenizer
import torch

models = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = 'I love Paris'

tokens = tokenizer.tokenize(sentence)

tokens = ['[CLS]'] + tokens + ['[SEP]']
tokens = tokens + ['[PAD]'] + ['[PAD]']
print(tokens)

attention_mask = [1 if i!= '[PAD]' else 0 for i in tokens]
print(attention_mask)

token_ids = tokenizer.convert_tokens_to_ids(tokens)

print(token_ids)

token_ids = torch.tensor(token_ids).unsqueeze(0)
attention_mask = torch.tensor(attention_mask).unsqueeze(0)

last_hidden_state, pooler_output, hidden_states = models(token_ids, attention_mask = attention_mask)

print(last_hidden_state.shape)
print(pooler_output.shape)
print(hidden_states.shape)

