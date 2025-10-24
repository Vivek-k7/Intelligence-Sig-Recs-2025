# Finale Pipeline:
- A pretty straightforward pipeline
- Take question and context as inputs,
- Pass through the fine tuned Extractive_QA model: Fine tuned on roBERTa Base on the SQuAD v2 dataset,
- Then pass through a fined tuned English to French model(Helsinki-NLP/opus-mt-en-fr)
- To finally get the answer in French.

<img width="940" height="105" alt="image" src="https://github.com/user-attachments/assets/bcf2d697-6da0-4c32-aa03-c177f044d8bc" />

  

### Future Improvements:
- Need to manage time better and focus more on quality more than quantity
- The unanswerable questions could have been handled better instead of a hardcoded threshold
- Maybe in the fine tuning of the Extractive_QA model, could include a small penalty for not correctly getting the no_answer (i.e if target is no_answer but our model outputs non zero end index)
- But again we would have to be careful with it as it would push the model towards giving empty answers and in a dataset like SquadV2 which has lot of unanswerable questions, could backfire.
- So we would have to find a trade off; this trade-off is similar to adjusting the class-imbalance weight between answerable and unanswerable examples during training.

### What I learnt:
- Overall it gave a lot of exposure in the field of applied ML.
- This was the first time I properly tried to apply my ML skills
- Debugging loads of code with patience
- Made me aware of how much more there is for me to learn

### Papers and Documentations I referred to:
- _Attention is all you need_
- _Know What You Don’t Know: Unanswerable Questions for SQuAD_
- _Swin Transformer: Hierarchical Vision Transformer using Shifted Windows_ (for non mandatory task)
- Documentations of huggingface models
- AI for conceptual understanding and code debugging
