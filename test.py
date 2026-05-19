import joblib
model=joblib.load('model.samash.xlsx.pkl')

print("chatbot Ready!")
print("type 'exit' to stop.\n")


while True:
 user_input=input("You:")
 if user_input.lower() == 'exit':
  print("chatbot:goodbye!")
  break
 response = model.predict([user_input])
 print("chatbot:", response[0])