FROM node:21-alpine as build
WORKDIR /app
COPY package*.json ./
RUN apk add --no-cache python3 make g++ && rm -rf /var/cache/apk/*
RUN npm rebuild node-sass
RUN npm install
RUN npm ci
COPY . ./
CMD npm run build
