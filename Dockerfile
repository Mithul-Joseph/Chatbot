#download python from dockerhub
FROM python:3.8.10

#set the working directory
WORKDIR /my_chatbot_dir

#copy the requirements file
COPY requirements.txt .

#installing the dependencies
RUN pip install -r requirements.txt

#copying the code to our directory
COPY src/ .

# expose a port
EXPOSE 8080

#running the program using cmd
CMD ["python", "app.py", "serve"]