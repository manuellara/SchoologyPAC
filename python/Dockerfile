# get base image
FROM python:3

# copy requirements.txt file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy src file
COPY editPAC.py .

# create downloads directory
RUN mkdir downloads

# execute script
CMD [ "python", "./editPAC.py" ]