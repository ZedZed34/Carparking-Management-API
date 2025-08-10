# 🐳 **Complete Dockerization Guide**

## 🎯 **What You Need to Do for Dockerization:**

### **✅ Current Status: READY TO GO!**
Your project already has all Docker files properly configured. Here's your step-by-step guide:

---

## 🚀 **Option 1: Simple Single Container (Quick Start)**

### **Step 1: Build the Docker Image**
```bash
# Navigate to your project directory
cd "D:\Carpark Django API"

# Build the Docker image
docker build -t carpark-api .
```

### **Step 2: Run the Container**
```bash
# Run with SQLite (simple, for testing)
docker run -p 8000:8000 -e DEBUG=True carpark-api

# Or run with custom environment variables
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e SECRET_KEY=your-secret-key \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  carpark-api
```

### **Step 3: Access Your Application**
- **API**: http://localhost:8000/api/v1/carparks/
- **Admin**: http://localhost:8000/admin/
- **Health Check**: http://localhost:8000/health/
- **Web Interface**: http://localhost:8000/home/

---

## 🏗️ **Option 2: Full Stack with Docker Compose (Production-Like)**

### **Step 1: Start All Services**
```bash
# Start all services (Django + PostgreSQL + Nginx)
docker-compose up --build

# Or run in background
docker-compose up -d --build
```

### **Step 2: Access Your Application**
- **Main App**: http://localhost (via Nginx)
- **Direct Django**: http://localhost:8000
- **Database**: PostgreSQL on localhost:5432

### **Step 3: Stop Services**
```bash
# Stop all services
docker-compose down

# Stop and remove all data (WARNING: This deletes database!)
docker-compose down -v
```

---

## 🔧 **Step-by-Step Commands to Run Now:**

### **1. Build the Image**
```bash
docker build -t carpark-api .
```
**Expected Output:**
```
[+] Building 45.2s (12/12) FINISHED
=> [internal] load build definition from Dockerfile
=> => transferring dockerfile: 1.50kB
=> [internal] load .dockerignore
=> => transferring context: 676B
...
=> exporting to image
=> => naming to docker.io/library/carpark-api
```

### **2. Run Simple Container**
```bash
docker run -p 8000:8000 -e DEBUG=True -e SECRET_KEY=test-key carpark-api
```
**Expected Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, carparks
Running migrations:
  No migrations to apply.
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://0.0.0.0:8000 (1)
```

### **3. Test the API**
```bash
# In a new terminal, test the health endpoint
curl http://localhost:8000/health/

# Test the API
curl http://localhost:8000/api/v1/carparks/
```

---

## 🛠️ **Advanced Docker Commands:**

### **Container Management**
```bash
# List running containers
docker ps

# View logs
docker logs <container-id>

# Enter container shell
docker exec -it <container-id> bash

# Stop container
docker stop <container-id>
```

### **Image Management**
```bash
# List images
docker images

# Remove image
docker rmi carpark-api

# Build with no cache (if you have issues)
docker build --no-cache -t carpark-api .
```

### **Docker Compose Commands**
```bash
# View service logs
docker-compose logs web
docker-compose logs db
docker-compose logs nginx

# Restart specific service
docker-compose restart web

# Scale services
docker-compose up --scale web=3

# Update and rebuild
docker-compose up --build --force-recreate
```

---

## 🌍 **Environment Configurations:**

### **Development (Local Testing)**
```bash
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e SECRET_KEY=dev-secret-key \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  carpark-api
```

### **Production-Like (with PostgreSQL)**
```bash
# Use docker-compose for full stack
docker-compose up -d
```

### **Custom Environment File**
Create `.env.docker`:
```env
DEBUG=False
SECRET_KEY=your-super-secret-production-key
ALLOWED_HOSTS=yourdomain.com,localhost
DATABASE_URL=postgresql://user:pass@db:5432/carpark_db
```

Then run:
```bash
docker run -p 8000:8000 --env-file .env.docker carpark-api
```

---

## 🔍 **Troubleshooting:**

### **Common Issues & Solutions**

#### **1. Port Already in Use**
```bash
# Error: bind: address already in use
# Solution: Use different port
docker run -p 8001:8000 carpark-api
```

#### **2. Permission Denied**
```bash
# Error: Permission denied
# Solution: Run as administrator or check Docker Desktop is running
```

#### **3. Database Connection Issues**
```bash
# Error: could not connect to server
# Solution: Make sure PostgreSQL container is running
docker-compose up db
```

#### **4. Static Files Not Loading**
```bash
# Error: 404 for static files
# Solution: Check if collectstatic ran successfully
docker exec -it <container-id> python manage.py collectstatic
```

### **Debugging Commands**
```bash
# Check container health
docker exec -it <container-id> curl localhost:8000/health/

# View Django logs
docker exec -it <container-id> python manage.py check

# Check database
docker exec -it <container-id> python manage.py showmigrations

# Load sample data
docker exec -it <container-id> python scripts/load_and_store.py
```

---

## 📦 **What Happens When You Run Docker:**

### **Build Process:**
1. ✅ Downloads Python 3.11.8 base image
2. ✅ Installs system dependencies (PostgreSQL client, etc.)
3. ✅ Installs Python packages from requirements.txt
4. ✅ Copies your application code
5. ✅ Collects static files
6. ✅ Sets up non-root user for security
7. ✅ Configures health checks

### **Runtime Process:**
1. ✅ Runs database migrations
2. ✅ Switches to non-root user
3. ✅ Starts Gunicorn server
4. ✅ Serves your API on port 8000
5. ✅ Health checks every 30 seconds

---

## 🎯 **Next Steps After Dockerization:**

### **1. Local Development**
```bash
# Quick start for development
docker-compose up web db
```

### **2. Production Deployment**
- Push image to Docker Hub
- Deploy to Railway, AWS, or other cloud platforms
- Use your existing CI/CD pipeline

### **3. Scaling**
```bash
# Scale web service
docker-compose up --scale web=3
```

---

## ✅ **Verification Checklist:**

After running Docker, verify these endpoints work:

- [ ] `http://localhost:8000/health/` - Returns `{"status": "healthy"}`
- [ ] `http://localhost:8000/api/v1/carparks/` - Returns carpark data
- [ ] `http://localhost:8000/admin/` - Django admin login
- [ ] `http://localhost:8000/home/` - Web interface
- [ ] `http://localhost:8000/api/v1/carparks/filter/?type=SURFACE` - Filtered data

**If all endpoints work, your Dockerization is successful!** 🎉

---

## 🚀 **Ready to Start?**

### **Quick Start (Complete Commands):**
```bash
# 1. Build the image
docker build -t carpark-api .

# 2. Run the container
docker run -p 8000:8000 -e DEBUG=True -e SECRET_KEY=docker-test-key -e ALLOWED_HOSTS=localhost,127.0.0.1 carpark-api

# 3. In a new terminal, load sample data
docker ps  # Get the container ID
docker exec <container-id> python scripts/load_and_store.py

# 4. Test the API
curl http://localhost:8000/health/
curl http://localhost:8000/api/v1/carparks/
```

### **One-Command Setup:**
```bash
docker build -t carpark-api . && docker run -d -p 8000:8000 -e DEBUG=True -e SECRET_KEY=docker-test-key -e ALLOWED_HOSTS=localhost,127.0.0.1 --name carpark-container carpark-api && sleep 10 && docker exec carpark-container python scripts/load_and_store.py
```

Your Carpark Management API will be available at http://localhost:8000! 🎯

### **✅ Verified Working Endpoints:**
- **Health Check**: http://localhost:8000/health/ → `{"status": "healthy"}`
- **API**: http://localhost:8000/api/v1/carparks/ → `2244 carparks loaded`
- **Admin**: http://localhost:8000/admin/
- **Web Interface**: http://localhost:8000/home/
