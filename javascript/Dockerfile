# get base image
FROM zenika/alpine-chrome:with-puppeteer

# install dotenv
RUN npm install dotenv

# create downloads folder
RUN mkdir downloads

# copy script into image (note: you will need to supply env file to run)
COPY getPAC.js .

# execute script
CMD [ "node", "getPAC.js" ]