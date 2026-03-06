import pandas as pd

# Load dataset
df = pd.read_csv("financial_data.csv")

def simple_chatbot(user_query):
    
    user_query = user_query.lower()
    
    if user_query == "what is microsoft's total revenue in 2025?":
        value = df[(df["Company"] == "Microsoft") & 
                   (df["Year"] == 2025)]["Total Revenue"].values[0]
        return f"Microsoft's total revenue in 2025 was {value} million USD."
    
    elif user_query == "what is tesla's net income in 2025?":
        value = df[(df["Company"] == "Tesla") & 
                   (df["Year"] == 2025)]["Net Income"].values[0]
        return f"Tesla's net income in 2025 was {value} million USD."
    
    elif user_query == "compare microsoft and tesla revenue in 2025.":
        ms_rev = df[(df["Company"] == "Microsoft") & 
                    (df["Year"] == 2025)]["Total Revenue"].values[0]
        
        ts_rev = df[(df["Company"] == "Tesla") & 
                    (df["Year"] == 2025)]["Total Revenue"].values[0]
        
        if ms_rev > ts_rev:
            return f"In 2025, Microsoft generated higher revenue ({ms_rev} million USD) compared to Tesla ({ts_rev} million USD)."
        else:
            return f"In 2025, Tesla generated higher revenue ({ts_rev} million USD) compared to Microsoft ({ms_rev} million USD)."
    
    elif user_query == "what are microsoft's total liabilities in 2024?":
        value = df[(df["Company"] == "Microsoft") & 
                   (df["Year"] == 2024)]["Total Liabilities"].values[0]
        return f"Microsoft's total liabilities in 2024 were {value} million USD."
    
    elif user_query == "how has tesla's revenue changed from 2024 to 2025?":
        rev_2024 = df[(df["Company"] == "Tesla") & 
                      (df["Year"] == 2024)]["Total Revenue"].values[0]
        
        rev_2025 = df[(df["Company"] == "Tesla") & 
                      (df["Year"] == 2025)]["Total Revenue"].values[0]
        
        change = rev_2025 - rev_2024
        
        if change > 0:
            return f"Tesla's revenue increased by {change} million USD from 2024 to 2025."
        else:
            return f"Tesla's revenue decreased by {abs(change)} million USD from 2024 to 2025."
    
    else:
        return "Sorry, I can only respond to predefined financial queries."


print("Financial Chatbot Prototype")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Chatbot:", response)