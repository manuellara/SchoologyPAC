# get base image
FROM zenika/alpine-chrome:with-puppeteer

# install dotenv
RUN npm install dotenv

# copy script into image (note: you will need to supply env file to run)
# COPY getPAC.js .
RUN wget https://raw.githubusercontent.com/manuellara/SchoologyPAC/master/javascript/getPAC.js

# execute script
CMD [ "node", "getPAC.js" ]