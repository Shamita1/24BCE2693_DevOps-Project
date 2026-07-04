# ---- Stage 1: Nginx web server serving static ABC Technologies website ----
FROM nginx:1.27-alpine

# Remove default nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy our website files into nginx html folder
COPY src/ /usr/share/nginx/html/

# Copy custom nginx config (adds /health endpoint + status page for monitoring)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
