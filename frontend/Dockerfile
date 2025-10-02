FROM node:18-alpine
WORKDIR /app

# Mock files
RUN mkdir -p src
RUN echo "console.log('Hello Frontend');" > src/index.js
RUN echo '{"name": "mock-frontend"}' > package.json

# Install serve to serve a static page
RUN npm install -g serve

# Create a simple build folder
RUN mkdir build && echo "<h1>Mock Frontend</h1>" > build/index.html

EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
