class student:
   def __init__(self,name):
     self.name = name
   def __init__(self,name,email):
     self.name = name
     self.email = email

st=student("anu","anu@gmail.com")
print("Name:",st.name)
print("Email id:",st.email)