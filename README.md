# LabaBoba v2: have a talk with me!

A tiny conversational server app with a language generation model for fun.

Powered by `streamlit`. Based on **GPT-2**.

## Implementation details
+ Based on pretrained HF [GPT-2 model](https://huggingface.co/sberbank-ai/rugpt3small_based_on_gpt2)
+ Trained on texts from [poetry dataset](https://www.kaggle.com/datasets/grafstor/19-000-russian-poems)

## Features
+ Inference caching for performance optimization
+ Last incomplete sentence (if not the only one) is discarded [manually](https://github.com/natasha/razdel#usage)
+ AMAZING kitties and best front-end design ever!

**New feature**: the net is much less offensive than [v1](https://github.com/Mathematician2000/lababoba)!
Although poems might be quite different...
