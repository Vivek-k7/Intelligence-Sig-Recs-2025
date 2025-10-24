from translate import predict_translate


context = input("|Enter the context|: ")
question = input("\n|Enter the question|: ")

ans = predict_translate(question, context, "en", "fr")
if(ans == ''):
    print("Cannot find relevant answer in the context provided")
else:
    print(f"\n|Answer|: {ans}")



