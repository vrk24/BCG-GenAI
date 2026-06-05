from Task2.data_store import financial_data

def simple_chatbot(user_input):
    user_input = user_input.lower()
    
    # Simple keyword matching logic
    if "revenue" in user_input:
        for company in financial_data:
            if company.lower() in user_input:
                return f"{company}'s total revenue is {financial_data[company]['revenue']}."
                
    elif "income" in user_input:
        for company in financial_data:
            if company.lower() in user_input:
                return f"{company}'s net income has {financial_data[company]['income_change']} over the last year."
                
    else:
        return "Sorry, I can only provide information on revenue or net income for Apple, Microsoft, or Tesla."

# Command-line loop
print("Financial Bot: Hello! Ask me about Apple, Microsoft, or Tesla revenue/income.")
while True:
    query = input("You: ")
    if query.lower() == "exit": break
    print("Bot:", simple_chatbot(query))