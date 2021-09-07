# get base image
FROM python:3

# copy requirements.txt file
# COPY requirements.txt .
RUN wget https://raw.githubusercontent.com/manuellara/SchoologyPAC/master/python/requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# download python src file
# COPY editPAC.py .
RUN wget https://raw.githubusercontent.com/manuellara/SchoologyPAC/master/python/editPAC.py

# create downloads directory
RUN mkdir downloads

# execute script
CMD [ "python", "./editPAC.py" ]