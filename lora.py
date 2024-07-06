import transformers
import finetuna as ft
import bitsandbytes as bnb
import torch as t

model_name = 'HuggingFaceH4/zephyr-7b-beta'
base_model = transformers.AutoModelForCausalLM.from_pretrained(model_name)

model_1 = ft.new_finetuned(base_model)

model_2 = ft.new_finetuned(
    base_model,
    adapt_layers = {'embed_tokens', 'embed_posotions', 'q_proj', 'v_proj'},
    embedding_config=ft.EmbeddingAdapterConfig(r=4, alpha=1),
    linear_config={
        'q_proj': ft.LinearAdapterConfig(r=8, alpha=1, dropout=0.0, bias=False),
        'v_proj': ft.LinearAdapterConfig(r=4, alpha=1, dropout=0.1, bias=True),
    },
)

opt = bnb.optim.AdamW(model_1.parameters())

with t.cuda.amp.autocast():
    opt.zero_grad()
    loss = mse_loss(model_1(prompt) - target) 
    model_1.backward(loss)
    opt.step()



t.save(model_1.state_dict(), "/save/path.pt")

t.save(ft.state_dict(model_1), "/save/path_finetuned.pt")

model_2.load_state_dict("/save/path.pt")

model_2.load_state_dict("/save/path_finetuned.pt", strict=False)