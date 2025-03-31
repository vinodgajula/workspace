# Use Node.js as base
FROM node:18-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies separately
RUN npm install --legacy-peer-deps

# Copy the entire project and build it
COPY . .
RUN npm run build

# Use Nginx for serving React
FROM nginx:alpine

# Copy build output to Nginx HTML directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port
EXPOSE 3000

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
