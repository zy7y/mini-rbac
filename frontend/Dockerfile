FROM node:16.15-alpine
COPY ./ /app
WORKDIR /app
RUN npm config set registry https://registry.npmjs.org
RUN npm install
RUN npm run build

FROM nginx:1.15.2-alpine
RUN mkdir /app
COPY --from=0 /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
